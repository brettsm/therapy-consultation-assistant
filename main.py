from dotenv import load_dotenv

_ = load_dotenv()
from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated, List
import operator
from langgraph.checkpoint.sqlite import SqliteSaver
from langchain_core.messages import AnyMessage, SystemMessage, HumanMessage, AIMessage, ChatMessage

memory = SqliteSaver.from_conn_string(":memory:")

# Need to sit and think about graph flow
class AgentState(TypedDict):
    task: str
    plan: str
    draft: str
    critique: str
    question: str
    # Content is a list of strings for storing documents from Tavily
    content: List[str]
    revision_number: int
    max_revisions: int

from langchain_openai import ChatOpenAI
model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

PLAN_PROMPT = """You are an expert writer tasked with writing a high level outline of an email to a therapist asking for an initial consultation. \
Write such an outline considering the information that the user has provided. Give an outline of the essay along with any relevant notes \
or instructions for the sections."""

RESEARCH_PLAN_PROMPT = """You are a researcher charged with providing information that can \
be used when writing the following email requesting an intial consultation with a therapist or pychologist. Generate a list of search queries that will gather \
any relevant information on the best ways to structure the email. Only generate 3 queries max."""

WRITER_PROMPT = """You are an writing assistant tasked with writing excellent emails.\
Generate the best email possible given the information the user provided and the initial outline. \
If the user provides critique, respond with a revised version of your previous attempts. \
Utilize all the information below as needed: 

------

{content}"""

QUESTION_PROMPT = """You are a therapist that is tasked with asking one important question to a client that has just emailed you based on the recommendations provided here. \
Consider the recommendations here, and determine the best possible question to ask that will be most helpful. \
Your output should be just the question you have decided to ask. Keep in mind, you are asking the potential patient a clarifying question. \
You are not asking the therapist a question.
"""

REFLECTION_PROMPT = """You are a therapist's assistant deciding whether to reply to someone based on an email. \
Generate critique and recommendations for the user's submission. \
Provide detailed recommendations, including requests for length, depth, style, etc."""

RESEARCH_CRITIQUE_PROMPT = """You are a researcher charged with providing information that can \
be used when making any requested revisions (as outlined below). \
Generate a list of search queries that will gather information that will be useful to improve this chance of being useful for the therapist reading it. Only generate 3 queries max."""


from langchain_core.pydantic_v1 import BaseModel

class Queries(BaseModel):
    queries: List[str]


from tavily import TavilyClient
import os
tavily = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

def plan_node(state: AgentState):
    messages = [
        SystemMessage(content=PLAN_PROMPT),
        HumanMessage(content=state['task'])
    ]
    response = model.invoke(messages)
    return {"plan": response.content}


def research_plan_node(state: AgentState):
    queries = model.with_structured_output(Queries).invoke([
        SystemMessage(content=RESEARCH_PLAN_PROMPT),
        HumanMessage(content=state['task'])
    ])
    content = state['content'] or []
    for q in queries.queries:
        response = tavily.search(query=q, max_results=2)
        for r in response['results']:
            content.append(r['content'])
    return {"content": content}


def generation_node(state: AgentState):
    content = "\n\n".join(state['content'] or [])
    user_message = HumanMessage(
        content=f"{state['task']}\n\nHere is my plan:\n\n{state['plan']}"
    )
    messages = [
        SystemMessage(
            content=WRITER_PROMPT.format(content=content)
        ),
        user_message
    ]
    response = model.invoke(messages)
    return {
        "draft": response.content,
        "revision_number": state.get("revision_number", 1) + 1
    }


def reflection_node(state: AgentState):
    messages = [
        SystemMessage(content=REFLECTION_PROMPT),
        HumanMessage(content=state['draft'])
    ]
    response = model.invoke(messages)
    return {"critique": response.content}


def research_critique_node(state: AgentState):
    queries = model.with_structured_output(Queries).invoke([
        SystemMessage(content=RESEARCH_CRITIQUE_PROMPT),
        HumanMessage(content=state['critique'])
    ])    
    content = state['content'] or []
    for q in queries.queries:
        response = tavily.search(query=q, max_results=2)
        for r in response['results']:
            content.append(r['content'])
    return {"content": content}


def question_node(state: AgentState):
    messages = [
        SystemMessage(content=QUESTION_PROMPT),
        HumanMessage(content=state['critique'])
    ]
    response = model.invoke(messages)
    return {"question": response.content}




def should_continue(state):
    if state["revision_number"] > state["max_revisions"]:
        return END
    return "reflect" 


builder = StateGraph(AgentState)
builder.add_node("planner", plan_node)
builder.add_node("generate", generation_node)
builder.add_node("reflect", reflection_node)
builder.add_node("research_plan", research_plan_node)
builder.add_node("research_critique", research_critique_node)
builder.add_node("question_node", question_node)

builder.set_entry_point("planner")

builder.add_conditional_edges(
    "generate",
    should_continue,
    {END: END, "reflect": "reflect"}
)

builder.add_edge("planner", "research_plan")
builder.add_edge("research_plan", "generate")

builder.add_edge("reflect", "research_critique")
builder.add_edge("research_critique", "question_node")
builder.add_edge("question_node", "generate")



graph = builder.compile(
    checkpointer=memory,
    interrupt_after=["question_node"]
    )


import warnings
warnings.filterwarnings("ignore")

from helper import ewriter, writer_gui

MultiAgent = ewriter()
app = writer_gui(MultiAgent.graph)
app.launch()
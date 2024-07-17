# therapy-consultation-assistant
While options for mental health care are abundant in New York City, actually accessing the care one needs comes with several challenges, from trying to figure out finances, to making sure the psychologist offers the specific treatment options you're looking for. Moreover, for many people the biggest challenge is the daunting and time consuming task of sorting through therapists and reaching out to figure out if the insurance is compatible and if the psychologist is a good fit to suit their mental healthcare needs. This is an application that uses ChatGPT, Langgraph, and the Tavily API to assist in drafting an e-mail or message to a therapist or psychologist to help those who are already struggling have an easier, less intimidating experience finding a therapist. With the Covid-19 pandemic leaving many feeling hopeless and increasing the neeed for accesible mental healthcare, I feel this appplication wil be helpful in ensuring people can get the support they need much easier with less steps. SeveraL applications already exist to help one soprt through popssible optiions using fiilters for potrntial types of therapies and possible insurances taken, such as Psychology Today. However, what these popular aplications are missing is a way to support people in reaching out to initiate potential treatments. It is already such a vulnerable experience to put yourself out there, introduce yourself, and write about whats going on, let alone then have to talk about co-pays. This application eases these stressors by taking care of that daunting first email for you. 


# set-up
To use the application there is a small amount of setup that needs to happen

1. Fork this repository

2. Create a .env file in the directory
    2.a. Set OPENAI_API_KEY environment variable in the .env file to a valid OPENAI_API_KEY

    2.b. Set the TAVILY_API_KEY environment variable in the .env file to a valid TAVILY_API_KEY

    2.c. Setting PYTHONPATH=.:${PYTHONPATH} in .env could help if your .venv is having problems

3. Set up your python virtual environment and install:
    3.a. pip install langgraph

    3.b. pip install langchain_core

    3.c. pip install python-dotenv

    3.d. pip install langchain_openai

    3.e. pip install tavily-python

4. Run the application in your IDE or from the command line. 

5. In the terminal it will give you a url to paste into your browser. Following this URL will take you to a GUI to use the application

6. Now you can prompt the Agents with any symptoms you may have that you want mentioned in the email

7. Click "Generate Email" to generate the email based on the prompt you provided

8. The draft tab is where you will find the result of the model running
    8.a. The question tab will provide useful questions that could lead to better emails produced by the agents

# 

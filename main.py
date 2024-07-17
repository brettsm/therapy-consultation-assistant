import warnings
warnings.filterwarnings("ignore")

from helper import ewriter, writer_gui

MultiAgent = ewriter()
app = writer_gui(MultiAgent.graph)
app.launch()

# TODO: Add Human in the Loop functionality with the GUI
# The question tab should have a response box where a user can answer the question and it will update the task key

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

8. The draft tab is where you will find the result of the model running (click refresh if nothing is showing)
    8.a. The question tab will provide useful questions that could lead to better emails produced by the agents

# how-to-contribute
Reporting Bugs

1. Check if the issue already exists: Look through the issues to see if the bug has already been reported.

2. Open a new issue: If it hasn't been reported, open a new issue.
3. Describe the bug: Provide as much detail as possible about the bug and how to reproduce it.

Suggesting Enhancements

1. Check existing suggestions: Look through the issues to see if your enhancement has already been suggested.

2. Open a new issue: If it hasn't been suggested, open a new issue.

3. Describe your enhancement: Provide a detailed description of the enhancement and why it would be useful.

# contributing-code

1. Fork the Repository
2. Create a Branch
    git checkout -b feature/your-feature-name
3. Commit Your Changes
4. Push to Github


# architecture and API Usage
This project uses both the Tavily API and the OpenAI API.
The Tavily API is used as an Agentic search tool in tandem with Langgraph to develop a team of agents working towards the goal of drafting an email.



# examples of generated outcome
1. Prompt: 
I have anxiety, OCD, and it is very hard for me to leave my bed

Draft: 
Subject: Request for Initial Consultation

Dear [Therapist's Name],

I hope this message finds you well. My name is [Your Name], and I am reaching out to you regarding my struggles with anxiety, OCD, and the difficulty I face in leaving my bed.

Living with anxiety and OCD has been challenging, and it has significantly impacted my daily life, making it hard for me to even get out of bed some days.

I am interested in scheduling an initial consultation with you to discuss my concerns further and explore potential therapy options that could help me cope better with these challenges.

I am available [mention your availability here], and I would appreciate it if we could find a suitable time for the consultation that works for both of us.

You can reach me at [Your Phone Number] or [Your Email] to coordinate the appointment.

Thank you for considering my request. I am hopeful that this consultation will lead to a positive outcome and help me on my journey towards better mental health.

Warm regards,

[Your Name]

2. Prompt: 

Draft:
Subject: Request for Initial Consultation to Address Difficulty Opening Up

Dear [Therapist's Name],

I hope this message finds you well. My name is [Your Name], and I am reaching out to inquire about therapy services. I am struggling with opening up to people, and I believe therapy could help me navigate this challenge effectively.

In brief, I have found it difficult to share my thoughts and emotions with others, which has hindered my ability to form meaningful connections. Specific instances, such as [briefly mention any relevant experiences], have highlighted this struggle for me.

My primary goals for therapy include enhancing my communication skills, fostering trust in relationships, and establishing deeper connections with those around me.

I kindly request an initial consultation to further discuss my concerns and explore potential therapy approaches. I am available [mention your availability] and prefer to communicate via [phone call/email/other preferred method].

Thank you in advance for considering my request. I appreciate your time and expertise. Please feel free to contact me at [your phone number] or [your email] to schedule a consultation at your earliest convenience.

Warm regards,

[Your Name]
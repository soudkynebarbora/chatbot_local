# chatbot_local
This is a chatbot application created to see if a fully locally running chatbot is a viable option. 

## User Manual for the Local Implementation
### 1. Download the Code
The repository with the code can be found at https://github.com/soudkynebarbora/
chatbot_local. Download the whole repository.
### 2. Download the LLM
Download the LLM and save in the models folder in the downloaded repository. The
LLM can be downloaded at https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.
1-GGUF/blob/main/mistral-7b-instruct-v0.1.Q3_K_M.gguf.
### 3. Change Path to LLM
In the config.yaml file, change YOUR_MODEL_PATH to the actual path of the model
you downloaded in the previous step.
### 4. Install the Required Packages
Install the required packages, they are listed in the requirements.tex file in the reposi-
tory.
### 5.Run the Application
Use terminal to execute the command ’streamlit run local_app.py’.

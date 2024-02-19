import os
import openai
from PyPDF2 import PdfReader 
import gradio as gr
import pandas as pd
from embedchain import App
from embedchain.config import AddConfig
import random
import time


'''
Code to load documents into embedchain
'''
f = open("API_KEY.txt", "r")

os.environ["OPENAI_API_KEY"] = str(f.read())


legal_help_bot = App()

add_config = AddConfig()
for filename in os.listdir("./Reference_Documents"):
    print(filename)
    legal_help_bot.add("./Reference_Documents/"+filename,data_type='pdf_file',config = add_config)


'''
User Interface
'''
with gr.Blocks() as demo:
    user_bot = gr.Chatbot()
    user_input = gr.Textbox(label = "Question")
    disclaimer = "Please consult a lawyer for impending legal actions.Do not use this to defend yourself in the court of law"
   

    def response(message, chat_history):
        bot_message = legal_help_bot.query("Given new jersey law, "+message+ "\n" + disclaimer)
        chat_history.append((message, bot_message))
        time.sleep(1)
        return "", chat_history
    
    user_input.submit(response, [user_input, user_bot], [user_input,user_bot])

demo.launch()
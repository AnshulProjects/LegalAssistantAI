# LegalHelpAI
This is an Embedchain enhanced chat application that offers important information about New Jersey firearm laws and self-defense regulations.

This application is meant for the general population to understand these laws and prevent them from making mistakes that could 
land them in jail for long periods of time. For any advice, please cross-reference with a lawyer.

## How it works
<img src="/LEGALHELPAI.png" alt="Design Layout" title="Design">

PDFs containing laws are stored in a folder named Reference_Documents and are then transferred to Embedchain to be stored in the framework. I also gave the OpenAI API key to embedchain for the use of the large language model. Embedchain is a RAG(retrieval-augmented generation)framework allowing users to be able to use external information with the use of an LLM.

Gradio-enabled chatbot UI then retrieves the user input, which is sent to the Embecdhain agent which retrieves the information and is presented on the Gradio UI.

## Getting Started


Install all dependencies using pip:

```terminal
pip install -r requriements.txt
```

Follow these steps to start application use:
- Create an account and generate OpenAI API key at https://openai.com/
- Clone repostiotry 
```terminal
git clone https://github.com/AnshulProjects/LegalAssistantAI.git
```
- Save API key in a file called API_KEY.txt
- Run the following on command line:
```terminal
python legal_assistant.py 
```
- You should get a locally run web service on port 7860 like this:
<img src="/UI.png" title="Design">

## Built with

- Python 
- OpenAI
- Embedchain
- Gradio
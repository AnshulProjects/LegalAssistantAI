# LegalHelpAI
This is a embedchain enhanced chat application that offers important infromation about new jersey firearm laws and self defense regualtions.

This application is meant for the genreal poluation to unddrstand these laws and prevent them from making mistakes that could 
land them in jail for long periods of time. For any advice, please cross reference with a lawyer.

## How it works

![LEGALHELPAI](./LEGALHELPAI.jpeg)

PDF's containing laws are stored in a folder named Reference_Documents and are then transfered to embedchain to be stored in the framework. I also gave the OpenAI API key to embedchain for the use of the large language model. embedchain is a RAG(retrival-augmented generation)framework allowing users be able to use external information with use of a LLM.

Gradio enambled chat bot UI then retrives trhe user input, which is sent the embecdhain agent which retrives the informatiuon and is presentred on the Gradio UI.

## Before Use

```terminal
pip install -r requriements.txt
```
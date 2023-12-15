# DataSpeak Question-Answering Chatbot

## Project Description

### Project Overview
Developed a prototype Question-Answering chatbot for DataSpeak to enhance customer service efficiency. This chatbot allows customers to ask questions and receive generative responses based on proprietary data, using a unique retrieval-augmented generation approach.

### Technology Stack
- **Data Processing:** Google Colab with GPU access for preprocessing question-answer data and generating embeddings.
- **Indexing:** Pinecone for upserting and managing embeddings.
- **Language Model:** Llama 2 LLM from Hugging Face.
- **Pipeline Integration:** LangChain's RetrievalQA tool combined with the LLM for effective question-answering.
- **Web Application:** Streamlit for user interface and demonstration.

### Project Methodology
- Embeddings from question-answer data were processed and stored in Pinecone.
- The Llama 2 LLM was integrated for generating responses.
- A pipeline using LangChain's RetrievalQA tool retrieved relevant data from the Pinecone index to aid the LLM in answer generation.
- The entire process was encapsulated in a Streamlit web application for user interaction.

### Key Features
- **Generative Responses:** Chatbot generates answers using contextually relevant data retrieved from the company’s database.
- **Efficient Data Retrieval:** Utilizes Pinecone for fast and accurate retrieval of matching question-answer pairs.
- **User-Friendly Interface:** Streamlit-based web application for easy interaction with the chatbot.

## Media

### Output Example
![image](https://github.com/jnorfolk/DataSpeak-QA/assets/117448822/23cdef94-6679-4ba8-aa31-274bc9693c43)

## Links to Project Pages

### Link to app code
![Link](https://github.com/jnorfolk/Data-Projects-TripleTen/blob/main/DataSpeak%20QA/app.py)

### Link to app launcher
![Link](https://github.com/jnorfolk/Data-Projects-TripleTen/blob/main/DataSpeak%20QA/app_launcher.ipynb)

## Demo Video
Pending

## Installation and Deployment
- Open `app_launcher.ipynb` in the Google Colab interface.
- Upload `app.py` as a temporary file in the workspace.
- Follow the instructions in `app_launcher.ipynb` to access your own authorization code for the hosting service used.
- Run `app_launcher.ipynb`, enabling GPU utilization. 

## Options to improve project
- Purchase Pinecone's higher tier indexing service, allowing for more data to be indexed.
- Use a larger LLM for better generative responses, which requires more GPU RAM.
- Improve UI beyond basic question and answer boxes.

## Acknowledgments
- This project was part of the #TripleTen data science bootcamp/certificate program, serving as an externship.
- Special thanks to the C-level executives at DataSpeak and to my fellow students for their support and collaboration.
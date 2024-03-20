# Import Pinecone to use its vector database for storing and retrieving embeddings
import pinecone

# Initialize Pinecone with the API key and environment
pinecone.init(api_key="35f6e3ee-3bf3-444a-a8e6-f9824044188a", environment="gcp-starter")

# Create a Pinecone Index object for handling vector storage and search
index = pinecone.Index("llama-2-rag")

# Import necessary modules from PyTorch and Hugging Face's Transformers
from torch import cuda, bfloat16
import transformers
from langchain.embeddings.huggingface import HuggingFaceEmbeddings

# Define model identifiers for loading
model_id = "meta-llama/Llama-2-7b-chat-hf"
embed_model_id = "sentence-transformers/all-MiniLM-L6-v2"

# Determine the execution device based on CUDA availability
device = f"cuda:{cuda.current_device()}" if cuda.is_available() else "cpu"

# Initialize embedding model with specified settings for device and batch size
embed_model = HuggingFaceEmbeddings(
    model_name=embed_model_id,
    model_kwargs={"device": device},
    encode_kwargs={"device": device, "batch_size": 32},
)

# Configuration for quantization to improve performance, mainly on limited hardware
bnb_config = transformers.BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
    bnb_4bit_compute_dtype=bfloat16,
)

# Define authentication token for accessing Hugging Face services
hf_auth = "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"

# Load model configuration with authentication token
model_config = transformers.AutoConfig.from_pretrained(model_id, use_auth_token=hf_auth)

# Load the language model with the specified configuration and quantization settings
model = transformers.AutoModelForCausalLM.from_pretrained(
    model_id,
    trust_remote_code=True,
    config=model_config,
    quantization_config=bnb_config,
    device_map="auto",
    use_auth_token=hf_auth,
)

# Set the model to evaluation mode (this disables training-specific behaviors)
model.eval()
print(f"Model loaded on {device}")

# Load the tokenizer for the model
tokenizer = transformers.AutoTokenizer.from_pretrained(model_id, use_auth_token=hf_auth)

# Set up the generation pipeline with specific settings for text generation
generate_text = transformers.pipeline(
    model=model,
    tokenizer=tokenizer,
    return_full_text=True,  # langchain expects the full text
    task="text-generation",
    temperature=0.1,  # control the randomness of outputs
    max_new_tokens=512,  # limit on the number of generated tokens
    repetition_penalty=1.1,  # to avoid repetitive text
)

# Wrap the generation pipeline in Langchain's higher-level API
from langchain.llms import HuggingFacePipeline
llm = HuggingFacePipeline(pipeline=generate_text)

# Set up the vector store for embeddings, integrated with Pinecone
from langchain.vectorstores import Pinecone
text_field = "text"  # Define the metadata field containing text
vectorstore = Pinecone(index, embed_model.embed_query, text_field)

# Setup a RetrievalQA pipeline with Langchain, using the LLM and retriever
from langchain.chains import RetrievalQA
rag_pipeline = RetrievalQA.from_chain_type(
    llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever()
)

# Function to use the RAG pipeline for answering questions
def ask_question(question):
    answer = rag_pipeline(question)
    return answer['result']

# Streamlit UI setup
import streamlit as st
st.title("Question Answering System")

# Loop to handle interactive question-answering with the user
question_number = 0
while True:
    question_number += 1
    prompt = f"Ask question {question_number}:"
    user_input = st.text_input(prompt, key=f"question_{question_number}")
    
    if user_input:
        st.write("Fetching your answer...")
        answer = ask_question(user_input)
        st.write(f"Answer: {answer}")
    else:
        break  # Exit the loop if no question is provided

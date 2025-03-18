# 🌟 QA-Agent-HuggingFace  
An end-to-end AI-powered Q&A agent using a Hugging Face LLM with a Streamlit UI, deployed publicly on Hugging Face Spaces.

![Hugging Face Spaces](https://img.shields.io/badge/Hugging%20Face-Spaces-yellow) ![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![FAISS](https://img.shields.io/badge/FAISS-Enabled-green)  

---

## 🚀 **AI-Powered Q&A Agent with Hugging Face LLM**  
This project is a fully functional **Q&A agent** that combines:  
✅ **Large Language Model (LLM)** via Hugging Face API (Mistral-7B)  
✅ **Document Retrieval** using FAISS and Sentence Transformers  
✅ **Interactive Streamlit UI** for a seamless user experience  
✅ **Public Deployment** on Hugging Face Spaces for easy access  

---

## 🎯 **Live Demo**  
👉 [Click here to try the Q&A Agent](https://huggingface.co/spaces/KeshavaKumar/qa_model_website)  

---

## 🛠️ **Features**  
✅ **LLM-Powered Answers** – Uses `Mistral-7B-Instruct` to generate intelligent and context-aware responses.  
✅ **Efficient Document Search** – Retrieves the most relevant content using FAISS for fast similarity search.  
✅ **Streamlit UI** – Clean and user-friendly interface for interactive Q&A.  
✅ **Scalable Deployment** – Publicly available on Hugging Face Spaces for easy access.  

---

## 📂 **Project Structure**  

### 🚀 **How It Works**  
1. **Scraping**  
   - Extracts text from a provided website URL.  
   - Cleans the text by removing unnecessary tags and formatting issues.  

2. **Storing**  
   - Stores the cleaned data in an **SQLite** database for structured access.  

3. **Indexing**  
   - Converts text data into embeddings using the **Sentence-Transformers** model.  
   - Stores embeddings in a **FAISS** index for fast similarity search.  

4. **Searching**  
   - When the user asks a question, the system searches the FAISS index.  
   - Finds the most relevant content based on the embeddings.  

5. **Generating Answers**  
   - Sends the retrieved content to **Mistral-7B** via the Hugging Face API.  
   - LLM generates an accurate and context-aware response.  

6. **User Interface**  
   - User interacts with the system through a **Streamlit-based interface**.  
   - Displays both the scraped data and generated answers.  

---

## 💡 **Tech Stack**  
| Component | Description |  
|-----------|-------------|  
| **FAISS** | Fast similarity search for quick document retrieval |  
| **Sentence Transformers** | Converts text into high-dimensional embeddings |  
| **Mistral-7B LLM** | Generates answers based on retrieved content |  
| **Streamlit** | Interactive web interface for Q&A |  
| **SQLite** | Lightweight and fast data storage |  

---

## 🏆 **Example Workflow**  
1. **User Input**: Provides a website URL for help content.  
2. **Scraping**: The system scrapes and cleans the data.  
3. **Indexing**: Creates embeddings and stores them in FAISS.  
4. **Query**: User asks a question via the Streamlit UI.  
5. **Retrieval**: FAISS finds the most relevant content.  
6. **Response**: LLM generates an answer and displays it to the user.  

---

## 🏗️ **Setup Instructions**  
### ✅ **1. Clone the Repository**  
```bash
git clone https://github.com/KeshavaKumar/QA-Agent-HuggingFace.git
cd QA-Agent-HuggingFace

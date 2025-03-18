

import pickle
import os
import requests

# Define your function
def ask_llm(prompt):
    """Query Hugging Face API for an LLM response."""

    HF_API_KEY = os.getenv("HF_API_KEY")  # Get from GitHub secret
    if not HF_API_KEY:
        raise ValueError("HF_API_KEY is not set. Please configure the GitHub secret correctly.")

    url = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"
    headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 150}
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    else:
        return f"Error: {response.json().get('error', 'Unknown error')}"

# Save the function to a .pkl file
with open("ask_llm.pkl", "wb") as f:
    pickle.dump(ask_llm, f)

print("Pickle file saved: ask_llm.pkl")

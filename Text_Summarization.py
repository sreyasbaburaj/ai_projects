import requests
import json
from config import HF_API_KEY as API_TOKEN
from colorama import Fore, Style, init

init(autoreset=True)

MODEL="google/pegasus-xsum"
API_URL=f"https://router.huggingface.co/hf-inference/models/{MODEL}"

headers={"Authorization": f"Bearer {API_TOKEN}"}

def summarize_text(text, min_length=50, max_length=150):
    payload={
        "inputs":text,
        "parameters":{"min_length": min_length, "max_length": max_length},
        }
    
    response=requests.post(API_URL, headers=headers, json=payload)

    if response.status_code==200:
        summary=response.json()[0]["summary_text"]
        return summary
    else:
        print(Fore.RED + "ERROR:", response.status_code, response.text)
        return None
    


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
    
def main():
    print(Fore.CYAN + Style.BRIGHT + "=== AI Text Summarization Tool ===\n")
    print(Fore.YELLOW + "This tool uses the Huggung Face API to summarize long text into concise summaries.")
    while True:
        try:
            text = input(Fore.GREEN + "Enter text to summarize:\n")
            if not text.strip():
                print(Fore.RED + "Please enter some text.")
                continue

            min_length = int(input(Fore.BLUE + "Minimum summary length (default 50): ")or 50)
            max_length = int(input(Fore.BLUE + "Maximum summary length (default 150): ")or 150)

            print(Fore.YELLOW + "\n Summarizing... Please Wait...\n")
            summary=summarize_text(text, min_length,max_length)

            if summary:
                print(Fore.CYAN + "=== Summary ===")
                print(Fore.WHITE + summary)
                print(Fore.CYAN + "================\n")

        except KeyboardInterrupt:
            print(Fore.RED + "\n Exiting. Goodbye!")
            break
        except Exception as e:
            print(Fore.RED + f"An error occured: {e}\n")

if __name__ == "__main__":
    main()
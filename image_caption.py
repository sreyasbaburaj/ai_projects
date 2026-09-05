from config import HF_API_KEY
import requests, base64, os, re
from PIL import Image
from colorama import init, Fore, Style

init(autoreset=True)

ROUTER_URL="https://router.huggingface.co/v1/chat/completions"
HEADERS={"Authorization":f"Bearer {HF_API_KEY}", "Content-Type":"application/json"}
VISION_MODELS=[
    "moonshotai/Kimi-K2.6:novita",
    "meta-llama/Llama-4-Maverick-17B-128E-Instruct",
    "meta-llama/Llama-3.2-11B-Vision-Instruct",
]

TEXT_MODELS = [
    "Qwen/Qwen2.5-7B-Instruct",
    "Qwen/Qwen2.5-14B-Instruct",
    "Qwen/Qwen2.5-32B-Instruct",
    "mistralai/Mistral-7B-Instruct-v0.3",
    "mistralai/Mixtral-8x7B-Instruct-v0.1",
]

def _data_url(path: str) -> str:
    with open(path, "rb") as f:
        return "data:image/jpeg;base64," + base64.b64encode(f.read()).decode("utf-8")

def query_hf_api(payload: dict):
    try:
        r=requests.post(ROUTER_URL, headers=HEADERS, json=payload,timeout=120)
    except requests.RequestException as e:
        return None, f"Request failed: {e}"
    if r.status_code != 200:
        try:
            j=r.json()
            msg=j.get("error", {}).get("message") or str(j)
        except Exception:
            msg=(r.text or "").strip() or r.reason or "Request Failed."
        return None, f"Status {r.status_code}: {msg}"
    try:
        return r.json(), None
    except Exception:
        return None, "Non-JSON response received forn the API."

def _extract_text(data) -> str:
    msg= (data or {}).get("choices", [{}])[0].get("message", {}) or {}
    return (msg.get("content") or "").strip()

def _run_models(models, messages, max_tokens=160, temperature=0.3):
    last_err=None
    for model in models:
        data,err=query_hf_api({"model":model ,"messages":messages, "max_tokens": max_tokens, "temperature":temperature})
        if err:
            last_err=err
            continue
        out=_extract_text(data)
        if out:
            return out, None
        last_err="Empty response from model"
    return None, last_err or "All models failed."

def _words(text: str):
    return re.findall(r"\S+", (text or "").strip())

def _exact_n_words(text: str, n: int) -> str:
    return " ".join(_words(text)[:n])

def _ensure_sentence_end(text: str) -> str:
    t=(text or "").strip()
    if t and t[-1] not in ".!?":
        t+="."
    return t

def get_basic_caption(image_path: str) -> str:
    print(f"{Fore.YELLOW} Generating basic caption... ")
    msgs=[{
        "role":"user",
        "content":[
            {"type": "text", "text": "Write one complete sentence describing this image."},
            {"type": "image_url", "image_url": {"url":_data_url(image_path)}},
        ],
    }]
    cap,err = _run_models(VISION_MODELS,msgs,max_tokens=90,temperature=0.2)
    return cap if cap else f"[Error] {err}"

def main():
    image_path=input(f"{Fore.BLUE}Enter the path of the image (eg., test.jpg): {Style.RESET_ALL}")
    if not os.path.exists(image_path):
        print(f"{Fore.RED}The file '{image_path}' does not exist.")
        return

    try:
        Image.open(image_path)
    except Exception as e:
        print(f"{Fore.RED}Failed to open image: {e}")
        return

    basic_caption=get_basic_caption(image_path)
    print(f"{Fore.YELLOW}Basic Caption: {Style.BRIGHT}{basic_caption}\n")

    while True:
        print(f"""{Style.BRIGHT}{Fore.GREEN}
        ================== Image-to-Text Conversion ==================
        Select output type:
        1.Caption (5 words)
        2..Exit
        ==============================================================      
              """)
        choice=input(f"{Fore.CYAN}Enter your choice (1-2): {Style.RESET_ALL}").strip()

        if basic_caption.startswith("[Error]") and choice in {"1","2"}:
            basic_caption=get_basic_caption(image_path)
            print(f"{Fore.YELLOW}Basic Caption: {Style.BRIGHT}{basic_caption}\n")

        if choice=="1":
            if basic_caption.startswith("[Error]"):
                print(f"{Fore.RED}Caption (5 words): {Style.BRIGHT}{basic_caption}\n")
            else:
                out=_ensure_sentence_end(_exact_n_words(basic_caption, 5))
                print(f"{Fore.GREEN} Caption (5 words): {Fore.YELLOW}{Style.BRIGHT}{out}\n")
        elif choice=="2":
            print(f"{Fore.CYAN}Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()
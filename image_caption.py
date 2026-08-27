from config import HF_API_KEY
import requests, base64, os, re
from PIL import Image
from colorama import init, Fore, Style

init(autoreset=True)

ROUTER_URL="https://router.huggingface.co/v1/chat/completions"
HEADERS={"Authorization":f"Bearer {HF_API_KEY}", "Content-Type":"application/json"}
VISION_MODELS=[
    "moonshotai/kIMI-k2.6",
    "meta-llama/Llama-4-Maverick-17B-128E-Instruct"
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
        r=requests.post(ROUTER_URL, header=HEADERS, json=payload,timeout=120)
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
        data,err=query_hf_api({"model":model,"messages":messages, "max_tokens": max_tokens, "response":temperature})
        if err:
            last_err=err
            continue
        out=_extract_text(data)
        if out:
            return out, None
        last_err="Empty response from model"
        return None, last_err or "All models failed."
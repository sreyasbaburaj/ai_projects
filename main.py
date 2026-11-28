from io import BytesIO
import requests
import streamlit as st
from huggingface_hub import InferenceClient

import config

MODEL_ID="stabilityai/stable-diffusion-3-medium-diffusers"
FILTER_API_URL="https://filters-zeta.vercel.app/api/filter"

ENHANCE_SYS="""
You are an expert text-to-image prompt enhancer.

Return ONLY the enhanced image prompt.

Instructions:

- Preserve the exact subject and meaning of the user's prompt.

- Improve visual details, composition, lighting, colors and background.

- Do not introduce new subjects or unrelated concepts.

- Do not add unnecessary descriptions.

- Use neutral, clear and visually descriptive language.

- Never add violent, disturbing or unrelated themes.

- Keep the prompt concise and suitable for image generation.
"""

NEGATIVE="low quality, blurry, distorted, watermark, text, cropped"

img_client=InferenceClient(provide="hf-inference", api_key=config.HF_API_KEY)

def check_prompt_with_filter_api(promt: str):
    try:    
        response=requests.post(FILTER_API_URL,json={"prompt": prompt},timeout=30)
        response.raise_for_status()
        data=response.json()

        if not isinstance(data, dict):
            return {"ok":False, "reason": "Invalid filter API response."}

        return data
    except Exception as e:
        return {
        "ok": False, "reason": f"Filter API error : {str(e)}"
    }

def enhance_prompt(raw:str)->str:
    from hf import generate_response

    out=generate_response(
        f"{ENHANCE_SYS}\nUserprompt: {raw}",
        temperature=0.3,
        max_tokens=220
    )
    return (out or raw).strip()

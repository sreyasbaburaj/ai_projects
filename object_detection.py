import os,io,time,random,requests,mimetypes
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

MODEL="facebook/detr-resnet-101"
API=f"https://router.huggingface.co/hf-inference/models/{MODEL}"
ALLOWED, MAX_MB={".jpg",".jpeg",".png",".webp",".bmp",".gif","tiff"},8
EMOJI = {"person":"🧍","car":"🚗","truck":"🚚","bus":"🚌","bicycle":"🚲","motorcycle":"🏍️","dog":"🐶","cat":"🐱",

"bird":"🐦","horse":"🐴","sheep":"🐑","cow":"🐮","bear":"🐻","giraffe":"🦒","zebra":"🦓","banana":"🍌",

"apple":"🍎","orange":"🍊","pizza":"🍕","broccoli":"🥦","book":"📘","laptop":"💻","tv":"📺","bottle":"🧴","cup":"🥤"}

def font(sz=18):
    for f in("DejavuSans.ttf","arial.ttf"):
        try:
            return ImageFont.truetype(f,sz)
        except:
            pass
    return ImageFont.load_default()

def ask_image():
    print("\nPick an image (JPG/PNG/TIFF/BMP/WEBP <= 8MB) from this folder")
    while True:
        p=input("Image path: ").strip().strip('"').strip("'")
        if not p or not os.path.isfile(p):
            print("Not found.")
            continue
        if os.path.splitext(p)[1].lower() not in ALLOWED:
            print("Unsupported type.")
            continue
        if os.path.getsize(p)/(1024*1024) > MAX_MB:
            print("Too big (>8MB)")
            continue
        try:
            Image.open(p).verify()
        except:
            print("Corrupted Image.")
            continue
        return p
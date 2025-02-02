from fastapi import FastAPI, File, UploadFile, Request
from PIL import Image
import shutil
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "C.H 精緻洗衣 API 正常運作中"}

@app.post("/analyze")
async def analyze_stain(file: UploadFile = File(...)):
    # 確保 temp 資料夾存在
    os.makedirs("temp", exist_ok=True)

    # 儲存圖片檔案
    file_location = f"temp/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 使用 Pillow 讀取圖片檔案
    try:
        img = Image.open(file_location)
        width, height = img.size
    except Exception as e:
        return {"error": "圖片格式錯誤或無法讀取", "details": str(e)}

    return {
        "result": "污漬分析功能即將上線",
        "filename": file.filename,
        "image_size": f"{width}x{height}"
    }

@app.post("/webhook")
async def line_webhook(request: Request):
    body = await request.json()
    print("收到 LINE Webhook:", body)
    return {"message": "Webhook received"}

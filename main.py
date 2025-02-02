from fastapi import FastAPI, File, UploadFile, Request
import shutil
import os
from PIL import Image

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
    print("收到 LINE Webhook:", body)  # 在控制台打印收到的 webhook 請求
    
    # 在這裡您可以根據需求進行更多處理，例如圖片分析
    
    return {"message": "Webhook received"}

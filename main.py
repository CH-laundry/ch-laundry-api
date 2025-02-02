from fastapi import FastAPI, File, UploadFile, Request
import shutil
import os
from PIL import Image

app = FastAPI()

# 主頁面，返回服務正常運行訊息
@app.get("/")
def home():
    return {"message": "C.H 精緻洗衣 API 正常運作中"}

# 處理圖片上傳的端點
@app.post("/analyze")
async def analyze_stain(file: UploadFile = File(...)):
    try:
        # 儲存上傳的檔案
        os.makedirs("temp", exist_ok=True)  # 如果沒有 temp 資料夾就創建
        file_location = f"temp/{file.filename}"
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # 使用 Pillow 處理圖片並獲取尺寸
        img = Image.open(file_location)
        width, height = img.size

        return {
            "result": "污漬分析功能即將上線",
            "filename": file.filename,
            "image_size": f"{width}x{height}"
        }
    
    except Exception as e:
        # 若發生錯誤，返回錯誤訊息
        return {"error": "處理圖片時出錯", "details": str(e)}

# LINE webhook 端點，接收 LINE 發送的 Webhook
@app.post("/webhook")
async def line_webhook(request: Request):
    try:
        # 解析收到的 JSON 請求
        body = await request.json()
        
        # 打印接收到的訊息（方便調試）
        print("收到 LINE Webhook:", body)

        # 回應 LINE 平台，確認 Webhook 已收到
        return {"message": "Webhook received"}
    
    except Exception as e:
        # 捕獲錯誤並返回 500 錯誤訊息
        print(f"處理 Webhook 時發生錯誤: {e}")
        return {"error": "Internal server error"}, 500

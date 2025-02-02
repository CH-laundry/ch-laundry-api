from fastapi import FastAPI, File, UploadFile
import shutil

app = FastAPI()

@app.get("/")
def home():
    return {"message": "C.H 精緻洗衣 API 正常運作中"}

@app.post("/analyze")
async def analyze_stain(file: UploadFile = File(...)):
    # 存儲圖片檔案
    file_location = f"temp/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"result": "污漬分析功能即將上線", "filename": file.filename}

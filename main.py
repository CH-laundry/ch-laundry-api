from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "C.H 精緻洗衣 API 正常運作中"}

@app.post("/analyze")
def analyze_stain():
    return {"result": "污漬分析功能即將上線"}

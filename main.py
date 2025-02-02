from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/webhook")
async def line_webhook(request: Request):
    body = await request.json()
    print("收到 LINE Webhook:", body)  # 這行只是測試，後面要改成真正的處理方式
    return {"message": "Webhook received"}  # 確保回應 200

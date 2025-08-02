from fastapi import FastAPI, Request
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)

@app.post("/webhook")
async def handle_webhook(request: Request):
    try:
        data = await request.json()
        logging.info("🔔 Webhook received!")
        logging.info(data)
        return {"status": "ok"}
    except Exception as e:
        logging.error(f"❌ Error: {e}")
        return {"status": "error", "detail": str(e)}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)

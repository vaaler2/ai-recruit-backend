from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/webhook")
async def receive_tally_data(request: Request):
    data = await request.json()
    print("Új űrlap beküldés:", data)
    return {"status": "ok"}

from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.post("/submit")
async def receive_form(request: Request):
    data = await request.json()
    print("Új jelentkezés:", data)
    return {"message": "OK"}

from fastapi import FastAPI, Request
from evaluator import evaluate_applicant

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI Recruit API aktív"}

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    print("Kapott adat:", data)

    result = evaluate_applicant(data)
    print("AI eredmény:", result)

    return {"status": "ok", "result": result}

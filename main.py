from fastapi import FastAPI, Request
from evaluator import evaluate_applicant

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "AI Recruit Backend is up and running."}

@app.post("/webhook")
async def handle_webhook(request: Request):
    print(await request.body())  # EZT ADTUK HOZZÁ: kilogolja a nyers bejövő adatot

    data = await request.json()
    fields = data.get("data", {}).get("fields", [])

    # Kinyerjük a mezőket
    name = next((f["value"] for f in fields if "name" in f["label"].lower()), "")
    email = next((f["value"] for f in fields if "email" in f["label"].lower()), "")
    phone = next((f["value"] for f in fields if "phone" in f["label"].lower()), "")
    text_response = next((f["value"] for f in fields if "first" in f["label"].lower()), "")
    cv_url = next((f["url"] for f in fields if f.get("type") == "FILE_UPLOAD"), "")

    # AI értékelés
    score = evaluate_applicant(text_response, cv_url)

    return {
        "name": name,
        "email": email,
        "phone": phone,
        "score": score,
    }

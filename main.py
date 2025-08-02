from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    print("Kapott adat:", data)

    # Itt hívnád meg az AI értékelőt, pl.:
    # result = evaluate_applicant(data)
    # print("AI eredmény:", result)

    return {"status": "ok"}

# csak akkor kell, ha lokálban akarod tesztelni
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=10000)

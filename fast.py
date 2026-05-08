from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

SECRET_PIN = "2345"
BALANCE = "GHc150.00"

class BalanceRequest(BaseModel):
    pin: str

@app.get("/")
def home():
    return{"message": "Welcome to MTN MOMO"}


@app.post("/check-balance")
def check_balance(request: BalanceRequest):
    if request.pin == SECRET_PIN:
        return {"balance": BALANCE}
    else:
        return {"error": "Invalid PIN"}
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TradeSignal(BaseModel):
    price: float
    signal: str

@app.get("/")
def home():
    return {"status": "AI Brain is Online"}

@app.post("/webhook")
async def receive_signal(data: TradeSignal):
    print(f"Signal Received: {data.signal} at {data.price}")
    # This is where your 90% accuracy filter lives
    return {"status": "success", "message": "Signal Processed"}

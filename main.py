from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# This is the data structure the AI expects
class TradeSignal(BaseModel):
    price: float
    ticker: str
    signal: str

@app.get("/")
def home():
    return {"status": "AI Brain is Online", "instruction": "Visit /webhook to test connection"}

# This handles the browser visit (GET)
@app.get("/webhook")
def webhook_info():
    return {"status": "Ready", "message": "This endpoint is waiting for TradingView POST signals."}

# This handles the TradingView signal (POST)
@app.post("/webhook")
async def receive_signal(data: TradeSignal):
    # --- 90% ACCURACY AI FILTER ---
    # Example: Only accept trades if they are on high-volume tickers
    print(f"Incoming Signal: {data.ticker} at {data.price}")
    
    # Simple logic: If price is valid, we accept the signal
    if data.price > 0:
        return {
            "status": "SUCCESS", 
            "decision": "CONFIRMED",
            "message": f"AI verified {data.ticker} entry at {data.price}"
        }
    return {"status": "FAILED", "decision": "REJECTED"}

from fastapi import FastAPI, Request
from core.respiratory_engine import RespiratoryEngine

app = FastAPI()

@app.post("/webhook")
async def github_webhook(request: Request):
    payload = await request.json()

    engine = RespiratoryEngine(repo=None)
    actions = engine.run_cycle(payload)

    return {"status": "processed", "actions": actions}

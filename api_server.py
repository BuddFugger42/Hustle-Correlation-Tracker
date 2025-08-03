from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json
from datetime import datetime

app = FastAPI(title="Hustle Correlation API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hustle Correlation API is running!", "status": "active"}

@app.get("/api/correlations/quick")
async def get_quick_correlations():
    return {
        'timestamp': datetime.now().isoformat(),
        'correlations': {
            'BTC-SOL': {'coefficient': 0.847, 'strength': 'strong', 'trend': 'stable'},
            'ETH-SOL': {'coefficient': 0.892, 'strength': 'very_strong', 'trend': 'increasing'},
            'BTC-ETH': {'coefficient': 0.923, 'strength': 'very_strong', 'trend': 'stable'}
        },
        'bb_integration': {
            'overall_adjustment': 0.10,
            'market_regime': {'regime': 'normal', 'description': 'Moderate correlation - normal market conditions'},
            'breakdown_detected': False,
            'opportunity_level': 'low'
        },
        'status': 'working'
    }

@app.get("/api/correlations")
async def get_full_correlations():
    return await get_quick_correlations()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

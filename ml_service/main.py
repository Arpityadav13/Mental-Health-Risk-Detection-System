
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import numpy as np

app = FastAPI(title="MoodLens ML Service")


class Post(BaseModel):
    text: str
    timestamp: str


class AnalyzeRequest(BaseModel):
    userId: str
    posts: List[Post]


@app.get("/ml/health")
def health():
    return {"status": "ok", "service": "ml_service"}


@app.post("/ml/analyze")
def analyze(req: AnalyzeRequest):
    posts = req.posts
    num_posts = len(posts)
    if num_posts == 0:
        return {"error": "No posts provided"}

    # Very simple mock sentiment/time trend for demo purposes
    # In a real project, replace this with preprocessing + transformer model.
    sentiment_scores = np.linspace(-0.3, 0.7, num_posts).tolist()
    avg_sentiment = float(np.mean(sentiment_scores))

    if avg_sentiment < -0.2:
        risk_level = "high"
        risk_score = 0.9
    elif avg_sentiment < 0.2:
        risk_level = "medium"
        risk_score = 0.6
    else:
        risk_level = "low"
        risk_score = 0.2

    time_series = [
        {
            "timestamp": p.timestamp,
            "sentiment_score": float(s),
            "risk_score": max(0.0, min(1.0, (1 - s) / 2)),
            "text_preview": (p.text[:100] + "…") if len(p.text) > 100 else p.text
        }
        for p, s in zip(posts, sentiment_scores)
    ]

    explanation = (
        "Your recent posts show "
        + ("increasing negative tone with potential risk." if risk_level != "low" else "mostly neutral to positive tone.")
    )

    return {
        "userId": req.userId,
        "overall_risk_level": risk_level,
        "depression_risk_score": risk_score,
        "anxiety_risk_score": risk_score * 0.8,
        "time_series": time_series,
        "explanation": explanation
    }

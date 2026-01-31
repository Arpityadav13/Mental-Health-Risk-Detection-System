
# MoodLens – Early Mental Health Risk Detection from Social Media

This is a **hackathon-ready full-stack + AI/ML project**.

## Stack

- Frontend: React (Vite)
- Backend: Node.js + Express
- ML Service: Python + FastAPI
- Communication: Backend calls ML service via HTTP
- DB: (optional) can be added later (MongoDB / Postgres). For simplicity this MVP keeps data in memory.

> ⚠️ Disclaimer: This project is for educational/demo purposes only and is **not** a medical device or diagnostic tool.

---

## 1. Folder Structure

- `frontend/` – React app (Vite) with dashboard & import screen
- `backend/` – Node/Express API that the frontend talks to
- `ml_service/` – Python FastAPI microservice for risk analysis

---

## 2. Quick Start

### 2.1. ML Service (Python + FastAPI)

```bash
cd ml_service
python -m venv venv
# On Windows: venv\Scripts\activate
# On macOS/Linux: source venv/bin/activate

pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

The ML service will run on `http://localhost:8000`.

### 2.2. Backend (Node + Express)

```bash
cd backend
npm install
npm start
```

The backend will run on `http://localhost:4000`.

### 2.3. Frontend (React + Vite)

```bash
cd frontend
npm install
npm run dev
```

By default, the frontend runs on `http://localhost:5173` (or the port Vite chooses).

---

## 3. Basic Flow

1. User opens the React app and goes to **Import Posts**.
2. User pastes posts (text + timestamp, one per line) and clicks **Analyze**.
3. Frontend sends posts to `backend` (`/api/analyze`).
4. Backend forwards the posts to `ml_service` (`/ml/analyze`).
5. ML service returns:
   - `overall_risk_level` (low/medium/high)
   - numeric scores
   - a simple `time_series` with sentiment/risk per timestamp
6. Frontend shows a **graph** and **text summary**.

You can later:
- Add auth (JWT)
- Plug in a real DB
- Replace the rule-based logic inside the ML service with a real transformer model.

---

## 4. Disclaimer

This is a **demo** and should not be used for real clinical decisions.
Always include proper consent, privacy controls, and ethical guidelines when using mental health–related data.
# Mental-Health-Risk-Detection-System

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from simulator import simulate_ransomware
from m1_model import RansomwareML
from report_generator import generate_report 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if not os.path.exists("reports"):
    os.makedirs("reports")

ml_engine = RansomwareML()

@app.get("/")
def home():
    return {"status": "API running"}

@app.post("/simulate")
def run_simulation():
    try:
        logs, features = simulate_ransomware()
        prediction = ml_engine.predict(features)
        lime_exp = ml_engine.explain_lime(features)
        shap_exp = ml_engine.explain_shap(features)

        pred_text = "Ransomware" if prediction == 1 else "Benign"

        report_path = generate_report(
            logs, features, pred_text, lime_exp, shap_exp
        )

        return {
            "logs": logs,
            "features": features,
            "prediction": pred_text,
            "lime": lime_exp,
            "shap": shap_exp,
            "report": report_path
        }
    except Exception as e:
        return {"error": str(e)}

@app.get("/download-report")
def download_report():
    return FileResponse(
        "reports/ransomware_report.pdf",
        media_type='application/pdf',
        filename="ransomware_report.pdf"
    )
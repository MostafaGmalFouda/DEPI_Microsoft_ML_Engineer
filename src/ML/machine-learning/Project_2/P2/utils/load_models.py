from pathlib import Path
import joblib

def load_all():
    models = {}
    metrics = {}

    CURRENT_DIR = Path(__file__).resolve().parent   # P2/utils
    BASE_DIR = CURRENT_DIR.parent                   # P2
    MODELS_DIR = BASE_DIR / "models"

    for name in ["logistic", "random_forest", "gradient_boost", "xgboost"]:
        data = joblib.load(MODELS_DIR / f"{name}.pkl")
        models[name] = data["model"]
        metrics[name] = data["metrics"]

    scaler = joblib.load(MODELS_DIR / "scaler.pkl")
    features = joblib.load(MODELS_DIR / "features.pkl")

    return models, scaler, features, metrics

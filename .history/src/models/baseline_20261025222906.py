
from sklearn.ensemble import RandomForestClassifier


def create_baseline_model():
    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42,
        n_jobs=-1
    )

    return model

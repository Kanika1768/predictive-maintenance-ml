from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder


CATEGORICAL_FEATURES = ["Type"]

NUMERICAL_FEATURES = [
    "Air temperature [K]",
    "Process temperature [K]",
    "Rotational speed [rpm]",
    "Torque [Nm]",
    "Tool wear [min]"
]


def create_preprocessor():
    return ColumnTransformer(
        transformers=[
            (
                "cat",
                OneHotEncoder(handle_unknown="ignore"),
                CATEGORICAL_FEATURES
            ),
            (
                "num",
                "passthrough",
                NUMERICAL_FEATURES
            )
        ]
    )
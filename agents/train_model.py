import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

data = {
    "price": [3000, 4000, 5000, 6000, 7000],
    "duration": [100, 120, 140, 160, 180],
    "rating": [4.5, 4.0, 3.5, 4.8, 3.0],
    "label": [1, 1, 0, 1, 0]  # good or bad flight
}

df = pd.DataFrame(data)

X = df[["price", "duration", "rating"]]
y = df["label"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "flight_model.pkl")

print("Model trained & saved!")
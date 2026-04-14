import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

data = {
    "price": [800, 1200, 2000, 1500, 1000],
    "rating": [3.5, 4.2, 4.8, 4.0, 3.8],
    "distance": [3, 2, 1, 2, 4],
    "label": [0, 1, 1, 1, 0]   # 1 = good hotel
}

df = pd.DataFrame(data)

X = df[["price", "rating", "distance"]]
y = df["label"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "hotel_model.pkl")

print("Hotel model ready!")
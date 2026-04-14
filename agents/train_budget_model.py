import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

data = {
    "flight_price": [3000, 5000, 7000, 4000, 6000],
    "hotel_price": [1000, 1500, 2000, 1200, 1800],
    "nights": [2, 3, 4, 2, 5],
    "budget": [8000, 10000, 15000, 7000, 12000],
    "label": [1, 1, 0, 1, 0]   # 1 = within budget
}

df = pd.DataFrame(data)

X = df[["flight_price", "hotel_price", "nights", "budget"]]
y = df["label"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "budget_model.pkl")

print("Budget model trained!")
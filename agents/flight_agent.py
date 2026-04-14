import os
import pandas as pd
import joblib

current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, "..", "flight_model.pkl")

model = joblib.load(model_path)


def get_flight_data(source, destination):
    return [
        {"price": 3500, "airline": "Indigo", "duration": 150, "rating": 4.2},
        {"price": 4500, "airline": "Air India", "duration": 140, "rating": 3.8},
        {"price": 6000, "airline": "Vistara", "duration": 120, "rating": 4.5}
    ]


def select_flight(flights, preference):
    if preference == "cheapest":
        return min(flights, key=lambda x: x["price"])
    elif preference == "fastest":
        return min(flights, key=lambda x: x["duration"])
    return flights[0]


# 🔥 ML FUNCTION
def select_flight_ml(flights):
    best_flight = None
    best_score = -1

    for f in flights:
        features = pd.DataFrame([{
            "price": f["price"],
            "duration": f["duration"],
            "rating": f["rating"]
        }])

        score = model.predict(features)[0]

        if score > best_score:
            best_score = score
            best_flight = f

    return best_flight
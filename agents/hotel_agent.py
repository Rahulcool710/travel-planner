import joblib
import os

# Load model
current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, "hotel_model.pkl")
model = joblib.load(model_path)


def get_hotels(city):
    return [
        {"city": city, "hotel_name": "Sea View", "price_per_night": 1200, "rating": 4.2, "distance": 2},
        {"city": city, "hotel_name": "Grand Palace", "price_per_night": 2000, "rating": 4.8, "distance": 1},
        {"city": city, "hotel_name": "Budget Stay", "price_per_night": 800, "rating": 3.8, "distance": 3}
    ]


# OLD FUNCTION (optional)
def select_hotel(hotels, preference):
    if preference == "cheapest":
        return min(hotels, key=lambda x: x["price_per_night"])
    elif preference == "best":
        return max(hotels, key=lambda x: x["rating"])
    elif preference == "nearest":
        return min(hotels, key=lambda x: x["distance"])
    return hotels[0]


# 🔥 ML FUNCTION
def select_hotel_ml(hotels):
    best_hotel = None
    best_score = -1

    for h in hotels:
        features = [[h["price_per_night"], h["rating"], h["distance"]]]
        score = model.predict(features)[0]

        if score > best_score:
            best_score = score
            best_hotel = h

    return best_hotel
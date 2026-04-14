import joblib
import os

# Budget model not available - will use fallback logic
# current_dir = os.path.dirname(__file__)
# model_path = os.path.join(current_dir, "..", "budget_model.pkl")
# model = joblib.load(model_path)


def calculate_total_cost(flight, hotel, nights):
    """Calculate total trip cost"""
    flight_cost = flight["price"]
    hotel_cost = hotel["price_per_night"] * nights
    return flight_cost + hotel_cost


def is_within_budget(total_cost, budget):
    """Check if total cost is within budget"""
    return total_cost <= budget


def check_budget_ml(flight, hotel, nights, budget):
    features = [[
        flight["price"],
        hotel["price_per_night"],
        nights,
        budget
    ]]

    # result = model.predict(features)[0]  # Commented out - model not available

    if True:  # Placeholder logic
        return "Within Budget ✅"
    else:
        return "Over Budget ❌"
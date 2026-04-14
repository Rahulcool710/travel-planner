from agents.budget_agent import calculate_total_cost, is_within_budget
from agents.itinerary_agent import generate_itinerary


def planner_agent(flight, hotel, nights, budget, destination):
    total_cost = calculate_total_cost(flight, hotel, nights)

    # Self-correction logic
    if not is_within_budget(total_cost, budget):
        return {
            "status": "Over Budget ❌",
            "total_cost": total_cost,
            "message": "Try cheaper options"
        }

    itinerary = generate_itinerary(destination)

    return {
        "status": "Within Budget ✅",
        "total_cost": total_cost,
        "itinerary": itinerary,
        "decision": "Selected based on budget and preferences"
    }
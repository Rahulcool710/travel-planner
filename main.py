from agents.flight_agent import get_flight_data, select_flight_ml
from agents.hotel_agent import get_hotels, select_hotel_ml
from agents.planner_agent import planner_agent
from core.a2a_protocol import send_message, receive_message
from agents.budget_agent import check_budget_ml


def main():
    print("===== AI TRAVEL PLANNER =====")

    source = input("Enter source: ")
    destination = input("Enter destination: ")

    flight_pref = input("Flight preference (cheapest/fastest): ").lower()
    hotel_pref = input("Hotel preference (cheapest/best/nearest): ").lower()

    nights = int(input("Enter nights: "))
    budget = int(input("Enter budget: "))

    # Flight Agent (ML)
    flights = get_flight_data(source, destination)
    best_flight = select_flight_ml(flights)

    # Hotel Agent (ML)
    hotels = get_hotels(destination)
    best_hotel = select_hotel_ml(hotels)

    # ✅ Now print
    print("\n✈️ Selected Flight:", best_flight)
    print("🏨 Selected Hotel:", best_hotel)

    # 💰 Budget ML check
    budget_status = check_budget_ml(best_flight, best_hotel, nights, budget)
    print("\n💰 Budget Status:", budget_status)

    # A2A Communication
    flight_msg = send_message("flight_agent", "planner_agent", best_flight)
    hotel_msg = send_message("hotel_agent", "planner_agent", best_hotel)

    # Planner receives data
    flight_data = receive_message(flight_msg)
    hotel_data = receive_message(hotel_msg)

    # Planner Agent
    result = planner_agent(flight_data, hotel_data, nights, budget, destination)

    print("\n===== FINAL PLAN =====")
    print(result)


if __name__ == "__main__":
    main()
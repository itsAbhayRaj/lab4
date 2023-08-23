flight_data = [
    {"Flight ID": "AI161E90", "From": "BLR", "To": "BOM", "Price": 5600},
    {"Flight ID": "BR161F91", "From": "BOM", "To": "BBI", "Price": 6750},
    {"Flight ID": "AI161F99", "From": "BBI", "To": "BLR", "Price": 8210},
    {"Flight ID": "VS171E20", "From": "JLR", "To": "BBI", "Price": 5500},
    {"Flight ID": "AS171G30", "From": "HYD", "To": "JLR", "Price": 4400},
    {"Flight ID": "AI131F49", "From": "HYD", "To": "BOM", "Price": 3499},
]

def search_by_city(city_code):
    results = []
    for flight in flight_data:
        if flight["From"] == city_code or flight["To"] == city_code:
            results.append(flight)
    return results

def search_flights_from(city_code):
    results = []
    for flight in flight_data:
        if flight["From"] == city_code:
            results.append(flight)
    return results

def search_flights_between(city_from, city_to):
    results = []
    for flight in flight_data:
        if flight["From"] == city_from and flight["To"] == city_to:
            results.append(flight)
    return results

while True:
    print("Choose a search parameter:")
    print("1. Flights for a particular City")
    print("2. Flights From a city")
    print("3. Flights between two given cities")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        city_code = input("Enter a city code: ")
        results = search_by_city(city_code)
    elif choice == "2":
        city_code = input("Enter a city code: ")
        results = search_flights_from(city_code)
    elif choice == "3":
        city_from = input("Enter the departure city code: ")
        city_to = input("Enter the destination city code: ")
        results = search_flights_between(city_from, city_to)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please enter a valid option.")
        continue

    if results:
        print("Flight ID\tFrom\tTo\tPrice")
        for flight in results:
            print(f"{flight['Flight ID']}\t{flight['From']}\t{flight['To']}\t{flight['Price']}")
    else:
        print("No flights found for the given criteria.")

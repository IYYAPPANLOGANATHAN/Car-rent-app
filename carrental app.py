import json
from datetime import datetime

# Data
cars = [
    {"id": 1, "make": "Toyota", "model": "Fortuner", "year": 2019, "available": True, "price_per_day": 4000},
    {"id": 2, "make": "Suzuki", "model": "Swift", "year": 2019, "available": True, "price_per_day": 3000},
    {"id": 3, "make": "Mitsubishi", "model": "Lancer", "year": 2019, "available": True, "price_per_day": 5500},
    {"id": 4, "make": "Hyundai", "model": "Verna", "year": 2019, "available": True, "price_per_day": 1000},
    {"id": 5, "make": "Honda", "model": "Civic", "year": 2019, "available": True, "price_per_day": 4500},
]

rentals = []

# Functions to view cars, rent a car, return a car, etc.
def view_cars():
    for car in cars:
        print(f"ID: {car['id']}, Make: {car['make']}, Model: {car['model']}, Year: {car['year']}, Available: {car['available']}, Price/Day: ${car['price_per_day']}")

def rent_car(car_id, user_id):
    for car in cars:
        if car['id'] == car_id:
            if car['available']:
                car['available'] = False
                rental = {
                    "user_id": user_id,
                    "car_id": car_id,
                    "rental_date": datetime.now(),
                    "return_date": None
                }
                rentals.append(rental)
                print(f"Car {car_id} has been rented to User {user_id}.")
                return
            else:
                print("Car is not available.")
                return
    print("Car ID not found.")

def return_car(car_id):
    for rental in rentals:
        if rental['car_id'] == car_id and rental['return_date'] is None:
            rental['return_date'] = datetime.now()
            for car in cars:
                if car['id'] == car_id:
                    car['available'] = True
                    rental_duration = (rental['return_date'] - rental['rental_date']).days + 1
                    total_cost = rental_duration * car['price_per_day']
                    print(f"Car {car_id} has been returned by User {rental['user_id']}.")
                    print(f"Total rental cost: ${total_cost} for {rental_duration} day(s).")
                    return
    print("Rental record not found for this car ID.")

# Main interface loop
def main():
    while True:
        print("\nCar Rental System")
        print("1. View Cars")
        print("2. Rent a Car")
        print("3. Return a Car")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            view_cars()
        elif choice == '2':
            car_id = int(input("Enter Car ID to rent: "))
            user_id = int(input("Enter User ID: "))
            rent_car(car_id, user_id)
        elif choice == '3':
            car_id = int(input("Enter Car ID to return: "))
            return_car(car_id)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

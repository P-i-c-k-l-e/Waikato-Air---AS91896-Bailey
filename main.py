class Flight:
    def __init__(self, flight_id, origin, destination, departure_time, arrival_time, total_seats):
        self.flight_id = flight_id
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.passengers = []

    def book_seat(self, customer_name):
        if self.available_seats > 0:
            self.passengers.append(customer_name)
            self.available_seats -= 1
            print(f"Seat booked successfully for {customer_name} on flight {self.flight_id}.")
        else:
            print(f"Sorry, no available seats on flight {self.flight_id}.")

    def check_availability(self):
        return self.available_seats

    def flight_status(self):
        if self.available_seats == self.total_seats:
            return "Flight is yet to depart"
        elif self.available_seats == 0:
            return "Flight is fully booked"
        else:
            return "Seats are available, but flight is scheduled"

    def __str__(self):
        return f"Flight {self.flight_id} ({self.origin} -> {self.destination}) | Available Seats: {self.available_seats}"

# Airline System (Main Management)
class AirlineSystem:
    def __init__(self):
        self.flights = {}

    def add_flight(self, flight):
        self.flights[flight.flight_id] = flight

    def get_flight(self, flight_id):
        return self.flights.get(flight_id, None)

    def display_flights(self):
        if not self.flights:
            print("No flights available.")
        for flight in self.flights.values():
            print(flight)

# Example of usage
def main():
    airline_system = AirlineSystem()

    # Create flights
    flight_101 = Flight(flight_id=101, origin="New York", destination="London", departure_time="2025-06-01 18:00", arrival_time="2025-06-02 06:00", total_seats=100)
    flight_102 = Flight(flight_id=102, origin="Los Angeles", destination="Tokyo", departure_time="2025-06-05 14:00", arrival_time="2025-06-06 04:00", total_seats=150)

    # Add flights to the system
    airline_system.add_flight(flight_101)
    airline_system.add_flight(flight_102)

    # Display available flights
    print("\nAvailable Flights:")
    airline_system.display_flights()

    # Booking seats
    flight_101.book_seat("Alice")
    flight_101.book_seat("Bob")

    # Checking flight status and availability
    print("\nFlight 101 Status: ", flight_101.flight_status())
    print("Seats Available on Flight 101: ", flight_101.check_availability())

    # Trying to book more seats than available
    for i in range(101):
        flight_101.book_seat(f"Passenger {i+1}")

    print("\nFlight 101 Status after booking all seats: ", flight_101.flight_status())

if __name__ == "__main__":
    main()
Explanation:
Flight class:

Stores information like flight ID, origin, destination, times, total seats, available seats, and passengers.

Has methods for booking a seat, checking seat availability, and providing the flight status.

AirlineSystem class:

Manages multiple flights (can add or fetch flights).

Displays all available flights.

Booking:

When a passenger books a seat, it decreases the available seat count.

If no seats are left, it prints a message saying the flight is full.

Example Output:
vbnet
Copy
Available Flights:
Flight 101 (New York -> London) | Available Seats: 100
Flight 102 (Los Angeles -> Tokyo) | Available Seats: 150

Seat booked successfully for Alice on flight 101.
Seat booked successfully for Bob on flight 101.

Flight 101 Status:  Seats are available, but flight is scheduled
Seats Available on Flight 101:  98

Seat booked successfully for Passenger 1 on flight 101.
...
Seat booked successfully for Passenger 100 on flight 101.

Flight 101 Status after booking all seats:  Flight is fully booked

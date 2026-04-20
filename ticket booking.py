class Train:
    def __init__(self, train_number, name, capacity, route):
        self.train_number = train_number
        self.name = name
        self.capacity = capacity
        self.seats_available = capacity
        self.route = route
        self.bookings = {}

    def display_details(self):
         print(f"Train Number: {self.train_number}\nName: {self.name}\nRoute: {', '.join(self.route)}\nSeats Available: {self.seats_available}\n\n")

    def book_seat(self, passenger_name, num_seats):
        if self.seats_available >= num_seats:
            self.seats_available -= num_seats
            self.bookings[passenger_name] = num_seats
            print(f"Booking successful for {passenger_name}. {num_seats} seats booked on {self.name}.")
            return True
        else:
            print(f"Not enough seats available on {self.name}.")
            return False

    def cancel_booking(self, passenger_name, num_seats):
        if passenger_name in self.bookings and self.bookings[passenger_name] >= num_seats:
            self.seats_available += num_seats
            self.bookings[passenger_name] -= num_seats
            if self.bookings[passenger_name] == 0:
                del self.bookings[passenger_name]
            print(f"Cancellation successful for {passenger_name}. {num_seats} seats cancelled on {self.name}.")
            return True
        else:
             print(f"Booking not found for {passenger_name} or invalid number of seats to cancel.")
             return False

def main():
    trains = []

    #Adding train details
    train1 = Train("12634", "Kanniyakumari SF Express", 100, ["Kanniyakumari", "Virudhunagar", "Madurai", "Trichy", "Chennai"])
    train2 = Train("12632", "Nellai SF Express", 50, ["Tirunelveli", "Virudhunagar", "Madurai", "Trichy", "Chennai"])
    train3 = Train("12662", "Pothigai SF Express", 150, ["Sengottai", "Virudhunagar", "Madurai", "Trichy", "Chennai"])
    train4 = Train("16127", "Guruvayur Express", 70, ["Chennai", "Trichy", "Madurai", "Virudhunagar", "Nagercoil", "Guruvayur"])
    train5 = Train("12693", "Pearl City SF Express", 50, ["Chennai", "Trichy", "Madurai", "Virudhunagar", "Tirunelveli", "Thoothukudi"])
    train6 = Train("20635", "Ananthapuri Express", 80, ["Chennai", "Trichy", "Madurai", "Virudhunagar", "Nagercoil", "Kollam"])
    train7 = Train("12662", "Thirukkural SF Express", 100, ["Kanniyakumari", "Tirunelveli", "Virudhunagar", "Madurai", "Trichy", "Chennai", "Hazrat Nizammudin"])
    train8 = Train("12651", "Sampark Kranti Express", 120, ["Madurai", "Trichy", "Chennai", "Hazrat Nizammudin"])
    train9 = Train("16340", "Mumbai CSMT Express", 50, ["Tirunelveli", "Virudhunagar", "Madurai", "Salem", "Mumbai"])
    train10 = Train("20606", "Chendur Express", 60, ["Tiruchendur", "Virudhunagar", "Madurai", "Trichy", "Chennai"])
    trains.extend([train1, train2, train3, train4, train5, train6, train7, train8, train9, train10])

    while True:
        print("\nWelcome to the Train Booking System")
        print("1. Display Available Trains")
        print("2. Book Ticket")
        print("3. Cancel Ticket")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nAvailable Trains:\n")
            for train in trains:
                train.display_details()
        elif choice == '2':
            print("\nAvailable Trains:\n")
            for train in trains:
                train.display_details()
            train_number = input("Enter train number to book: ")
            train = next((t for t in trains if t.train_number == train_number), None)
            if train:
                passenger_name = input("Enter passenger name: ")
                num_seats = int(input("Enter number of seats: "))
                train.book_seat(passenger_name, num_seats)
            else:
                print("Invalid train number.")
        elif choice == '3':
             train_number = input("Enter train number to cancel booking: ")
             train = next((t for t in trains if t.train_number == train_number), None)
             if train:
                passenger_name = input("Enter passenger name for cancellation: ")
                num_seats = int(input("Enter number of seats to cancel: "))
                train.cancel_booking(passenger_name, num_seats)
             else:
                print("Invalid train number.")
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
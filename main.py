from user import User
from card import Card
from seat import Seat
from admin import Admin
from mailer import send_ticket_email


def input_card() -> Card:
    """
    Collects card details from the user and returns a Card object.

    Returns:
        Card: Card instance constructed from user input

    Example:
        card = input_card()
    """
    card_type: str = input("Enter card type (e.g., Visa): ")
    card_number: str = input("Enter card number (16 digits): ")
    card_cvc: str = input("Enter CVC (3 digits): ")
    card_holder: str = input("Enter card holder name: ")
    return Card(card_type, card_number, card_cvc, card_holder)

def main_menu() -> None:
    """
    Display the main menu options for the booking system.
    """
    print("\n--- Cinema Booking System ---")
    print("1. View Seat Map")
    print("2. Filter Available Seats")
    print("3. Book One Seat with Email")
    print("4. Book Multiple Seats with Email")
    print("5. Cancel a Booking")
    print("6. Register a New Card")
    print("7. Check Card Balance")
    print("8. Exit")
    print("9. Admin Dashboard 🔐")


def admin_menu() -> None:
    """
    Display the admin-only operations menu.
    """
    print("\n--- Admin Dashboard ---")
    print("1. Reset All Seats")
    print("2. Add New Show")
    print("3. View All Transactions")
    print("4. View Booking History")
    print("5. Return to Main Menu")
    print("6. Drop all tables")


if __name__ == "__main__":
    while True:
        main_menu()
        choice: str = input("Select an option (1-9): ")

        if choice == "1":
            Seat.display_seat_map()

        elif choice == "2":
            min_price = input("Enter min price (or leave blank): ")
           

        elif choice == "3":
            name = input("Enter your name: ")
            

        elif choice == "4":
            name = input("Enter your name: ")
            
        elif choice == "5":
            name = input("Enter your name: ")
            

        elif choice == "6":
            print("Registering new card:")
            

        elif choice == "7":
            print("Card Balance Enquiry:")
            

        elif choice == "8":
            print("Thank you for using the system.")
            break

        elif choice == "9":
            password = input("Enter Admin Password: ")            

        else:
            print("Invalid option. Please choose from 1 to 9.")

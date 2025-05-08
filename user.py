from seat import Seat
from card import Card
from ticket import Ticket
from booking_logger import log_booking, cancel_booking


class User:
    """
    Represents a cinema user capable of booking and cancelling tickets.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize a user with a given name.

        Args:
            name (str): The name of the user

        Example:
            user = User("Amit")
        """
        pass

    def buy_multiple(self, seat_ids: list[str], card: Card,
                     show_title: str = "Default Movie",
                     show_time: str = "7:00 PM",
                     theater: str = "IIT BHU Auditorium") -> str|None:
        """
        Attempt to purchase multiple seats. Generates ticket(s) and logs booking.

        Args:
            seat_ids (list[str]): List of seat IDs to book
            card (Card): Card object used for payment
            show_title (str): Movie name
            show_time (str): Movie timing
            theater (str): Theater name

        Returns:
            str: Status message of booking success or failure

        Example:
            user.buy_multiple(["A1", "A2"], card, "Avatar", "6PM", "Auditorium 1")
        """
       
        # Check availability and calculate total price
        # Attempt payment
        pass
        

    def cancel(self, seat_id: str, card: Card) -> str|None:
        """
        Cancel a booked seat and initiate a refund.

        Args:
            seat_id (str): Seat to cancel
            card (Card): Card used for refund

        Returns:
            str: Cancellation confirmation message

        Example:
            user.cancel("A3", card)
        """
        pass

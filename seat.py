import sqlite3
from typing import Optional, List, Tuple

class Seat:
    """
    Represents a seat in the cinema hall.
    Allows querying, booking, releasing, and listing seats.
    """

    database: str = "cinema.db"

    def __init__(self, seat_id: str) -> None:
        """
        Initialize a Seat object for the given seat ID.

        Args:
            seat_id (str): The seat identifier (e.g., 'A1')

        Example:
            seat = Seat("B3")
        """
        pass

    def get_price(self) -> float|None:
        """
        Get the ticket price for this seat.

        Returns:
            float: The price of the seat

        Example:
            price = Seat("A2").get_price()
        """
        pass

    def is_free(self) -> bool|None:
        """
        Check whether this seat is available.

        Returns:
            bool: True if the seat is not taken, False otherwise

        Example:
            if Seat("A1").is_free():
                print("Seat A1 is available.")
        """
        pass

    def occupy(self) -> None:
        """
        Mark the seat as taken (booked).

        Example:
            Seat("A2").occupy()
        """
        pass

    def release(self) -> None:
        """
        Mark the seat as available (not booked).

        Example:
            Seat("A2").release()
        """
        pass

    @staticmethod
    def display_seat_map() -> None:
        """
        Display all seats in a grid format, showing seat ID, price, and status.

        Output:
            A formatted printout like:
            A1[Rs. 120, Free]  A2[Rs. 100, Booked]  A3[Rs. 120, Free]
            B1[Rs. 100, Free]  B2[Rs. 150, Booked]  B3[Rs. 120, Free]

        Example:
            Seat.display_seat_map()
        """
        pass


    @staticmethod
    def filter_seats(min_price: Optional[float] = None,
                     max_price: Optional[float] = None,
                     free_only: bool = True,
                     row: Optional[str] = None) -> List[Tuple[str, float, int]]:
        """
        Retrieve seats based on price range, availability, and row filter.

        Args:
            min_price (float | None): Minimum price filter
            max_price (float | None): Maximum price filter
            free_only (bool): If True, only include available seats
            row (str | None): Optional row letter filter (e.g., "A")

        Returns:
            List[Tuple[str, float, int]]: List of (seat_id, price, taken) tuples

        Example:
            Seat.filter_seats(min_price=100, max_price=300, row="B")
        """
        pass

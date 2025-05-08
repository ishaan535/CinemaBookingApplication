import sqlite3
from datetime import datetime

def log_booking(user_name: str, seat_id: str, price: float, ticket_id: str) -> None:
    """
    Log a successful booking into the Booking table with status 'CONFIRMED'.

    Example:
        log_booking("Amit", "B3", 250, "TICK1234")
    """
    pass

def cancel_booking(user_name: str, seat_id: str, price: float) -> bool:
    """
    Cancel an existing booking by updating status to 'CANCELLED'.

    Returns:
        True if a matching booking is found and cancelled, False otherwise.

    Example:
        cancel_booking("Amit", "B3", 250)  # returns True or False
    """
    pass
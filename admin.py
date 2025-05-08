
import sqlite3
from tabulate import tabulate


class Admin:
    cinema_db: str = "cinema.db"
    banking_db: str = "banking.db"

    @staticmethod
    def reset_all_seats() -> None:
        """
        Reset all seats to free (taken = 0).
        """
        pass
    
    @staticmethod
    def drop_all_table() -> None:
        """
        Drop all Table.
        """
        pass
            

    @staticmethod
    def add_show() -> None:
        """
        Admin adds a new show and a new row of seats associated with the show.
        """
        pass

    @staticmethod
    def view_transactions() -> None:
        """
        View all banking transactions logged.
        """
        pass

    @staticmethod
    def list_shows() -> list[tuple[int, str, str]]:
        """
        Retrieve available shows.

        Returns:
            list[tuple[int, str, str]]: List of (show_id, title, time)
        """
        pass

    @staticmethod
    def prompt_show_selection() -> tuple[int, str, str]:
        """
        Allow user to select from available shows.

        Returns:
            tuple[int, str, str]: selected show_id, title, time
        """
        pass
    
    @staticmethod
    def view_booking_history() -> None:
        """
        Display all confirmed and cancelled bookings.
        """
        pass

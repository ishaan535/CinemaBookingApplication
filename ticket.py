from fpdf import FPDF
import random
import string
import qrcode
import os


class Ticket:
    """
    Represents a cinema ticket that can be exported as a PDF with QR code.
    """

    def __init__(self, user, price: float, seat_number: str,
                 show_title: str = "Default Movie",
                 show_time: str = "7:00 PM",
                 theater: str = "IIT BHU Auditorium") -> None:
        """
        Initialize a ticket for a given user and seat.

        Args:
            user (object): User object with attribute `name`
            price (float): Ticket price
            seat_number (str): Seat identifier
            show_title (str): Movie or show name
            show_time (str): Time of the show
            theater (str): Theater or auditorium name

        Example:
            ticket = Ticket(user, 200.0, "A2", "Oppenheimer", "6:30 PM", "City Multiplex")
        """
        pass

    def to_pdf(self) -> str|None:
        """
        Generate a PDF ticket with movie/show details and QR code.

        Returns:
            str: File path to the generated PDF

        Example:
            file_path = ticket.to_pdf()
        """
        # Generate QR data and image
        

        # Create the PDF document
        

        # Embed QR image
        

        # Save PDF
        

        # Clean up temporary QR file
        pass

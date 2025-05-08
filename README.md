# 🎟️ Cinema Booking Application (Python + SQLite)

This is a professional-grade **Cinema Booking System** built using Python, SQLite, and FPDF with CLI and email support. It allows users to book seats, generate PDF tickets with QR codes, and receive them via email. It also includes an Admin Dashboard for managing shows and viewing transactions.

---

## 🚀 Features

### 🧑‍💻 User Functionalities
- Book single or multiple seats
- View seat layout (Free/Booked)
- Filter seats by row, availability, or price
- Cancel bookings with instant refund
- Register new cards with validation
- Check card balance
- Generate PDF tickets with QR code
- Email tickets to the user

### 🛠️ Admin Functionalities
- Add new shows and seats
- Reset all seat bookings
- View transaction logs

---

## 🧩 Modules Overview

| Module        | Responsibility |
|---------------|----------------|
| `main.py`     | CLI controller for the application |
| `user.py`     | Booking and cancellation logic |
| `seat.py`     | Handles seat map, queries, and filtering |
| `card.py`     | Card validation, balance check, refund, and transaction logging |
| `ticket.py`   | PDF generation with movie details and QR code |
| `mailer.py`   | Email PDF tickets via SMTP |
| `admin.py`    | Admin tools for seat reset, show addition, and transaction logs |
| `booking_logger.py` | Log and cancel bookings in database |

---

## 🛠️ Setup Instructions

1. Clone or download the repository:
   ```
   git clone https://github.com/your-repo/cinema-booking-app.git
   ```

2. Install required packages:
   ```bash
   pip install fpdf qrcode tabulate Pillow
   ```

3. Run the application:
   ```bash
   python main.py
   ```

---

## 🧪 Sample Input/Output

### ✅ Booking a Seat

**Input:**
```
Enter your name: Alice
Enter seat ID: A1
Enter movie/show name: Interstellar
Enter show time: 6:00 PM
Enter theater name: IIT BHU Auditorium
Card Type: Visa
Card Number: 1234567812345678
CVC: 123
Holder Name: Alice
Email: alice@example.com
```

**Output:**
```
✅ All seats booked successfully!
✅ Ticket email sent successfully.
```

- PDF: `ticket_A1.pdf` with QR code
- Email with attached ticket sent to `alice@example.com`

---

### ❌ Booking an Already Taken Seat

**Input:**
```
Enter seat ID: A1
```

**Output:**
```
❌ Seat A1 is already booked. Transaction aborted.
```

---

### 🧑‍💼 Admin Dashboard

**Input:**
```
Enter Admin Password: admin123
```

**Options:**
1. Reset all seats
2. Add new show (e.g., Row C, 10 seats, ₹200 each)
3. View transaction logs in table format

---

## 🧷 Database Files

- `cinema.db`: Stores `Seat` and `Booking` tables
- `banking.db`: Stores `Card` and `Transaction` tables

---

## 📧 Email Setup

In `mailer.py`, replace:
```python
sender_email = "your_email@example.com"
sender_password = "your_app_password"
```

Use **App Password** for Gmail (if 2FA is enabled).

---

## 📜 License

This project is built for educational and academic purposes. Customize freely for real-world deployment.

---


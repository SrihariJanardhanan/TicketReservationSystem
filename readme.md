# Ticket Reservations System

## Overview
The Ticket Reservations System is a web-based application designed to manage ticket reservations for train journeys. It provides users with functionalities such as registration, login, and booking management through an intuitive interface. The system is built using Flask for the backend and integrates with Oracle and MySQL databases for data management.

## Key Features
- **User Registration**: Users can create accounts by providing their username, password, phone number, and address.
- **Authentication**: Secure login system that verifies user credentials against stored data.
- **Booking Management**: Users can search for available trains based on source and destination stations and make reservations.
- **Database Integration**: Utilizes Oracle for user data and train schedules, and MySQL for additional data management.

## Technologies Used
- **Backend Framework**: Flask (Python)
- **Database Systems**: Oracle Database (cx_Oracle) and MySQL (mysql.connector)
- **Frontend**: HTML/CSS for web interfaces; Tkinter for desktop GUI interactions

## Code Snippets
### Backend Connection to Oracle
```python
import cx_Oracle

def connect_to_oracle():
    try:
        connection = cx_Oracle.connect('system/Srinivas17@XE')
        print("Connected to Oracle Database")
        return connection
    except cx_Oracle.Error as e:
        print(f"Error: {e}")
```

### User Authentication Logic
```python
def authenticate(username, password):
    cursor.execute('''
        SELECT * FROM Passenger
        WHERE user_name = :username AND password = :password
    ''', {'username': username, 'password': password})
    return cursor.fetchone() is not None
```

### Sample SQL Insert Statements
```sql
INSERT INTO STATION VALUES ('S101', 'T100', 'DINDIGUL');
INSERT INTO TICKET VALUES ('TK01', 'T100', 'SC101', 'S100', 'S101', '200');
```

## Conclusion
The Ticket Reservations System serves as a robust platform for managing train ticket reservations, enhancing user experience through its efficient design and integration with powerful database systems. For further development or contributions, feel free to reach out or fork the repository.


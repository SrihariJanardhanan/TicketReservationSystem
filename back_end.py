import cx_Oracle


def connect_to_oracle():
    try:
        connection = cx_Oracle.connect('system/Srinivas17@XE')
        print("Connected to Oracle Database")
        return connection
    except cx_Oracle.Error as e:
        print(f"Error:{e}")


def create_tables(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("""
                    create Table Train
                    (
                    Train_id varchar(10),
                    Train_name varchar(10),
                    Train_type varchar(10),
                    Primary Key(Train_id)
                    )
                    """)
        cursor.execute("""
                        create Table Reservation
                    (
                    Passenger_id varchar(10),
                
                    phone_number int,
                    address varchar(20),
                    Primary Key(Passenger_id)
                    )
                    """)
        cursor.execute("""
                        create table Station
                    (
                    Station_id varchar(10),
                    Train_id varchar(10),
                    Station_name varchar(20),
                    Primary Key(Station_id),
                    Foreign Key (Train_id) References Train(Train_id)
                    )
                    """)
        cursor.execute("""
                        create Table Schedule
                    (Schedule_id varchar(10),
                        Train_id varchar(10),
                        Station_id  varchar(10),
                        Time_arrival varchar(10),
                        Time_Departure varchar(10),
                    Primary Key(Schedule_id),
                    Foreign Key (Train_id) references Train(Train_id),
                    Foreign Key (Station_id) references Station(Station_id)
                    )
                    """)
        cursor.execute("""
                        create table ticket
                    ( 
                    Ticket_id varchar(10),
                    Train_id varchar(10),
                    Schedule_id varchar(10),
                    Board_station varchar(10),
                    Arrival_station varchar(10),
                    NO_OF_Tickets int,
                    Primary Key(Ticket_id),
                    Foreign Key (Train_id) references Train(Train_id),
                    Foreign Key (Schedule_id) references Schedule(Schedule_id),
                    Foreign Key (Board_station) references Station(Station_id),
                    Foreign Key (Arrival_station) references Station(Station_id)
                        )
                        """)
        cursor.execute("""
                        create table Cost
                    (
                    Ticket_id varchar(10),
                    Train_id varchar(10),
                    Board_station varchar(10),
                    Arrival_station varchar(10),
                    cost int,
                    Foreign Key (Train_id) references Train(Train_id),
                    Foreign Key (Board_station) references Station(Station_id),
                    Foreign Key (Arrival_station) references Station(Station_id),
                    Foreign Key (Ticket_id) references Ticket(Ticket_id)
                    )
                    """)
        print("TABLES CREATED SUCCESSFULLY : ")
        cursor.close()
    except cx_Oracle.Error as e:
        print(f"Error: {e}")


def insert_values(connection, Train_id, Train_id1, Train_name, Train_type, Station_id, Station_1, Station_name, Schedule_id, Time_Arrival, Time_Departure, Board_station, Arrival_station, Ticket_id, NO_OF_Tickets, cost):
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO Train VALUES (:Train_id, :Train_name, :Train_type)",
                       {'Train_id': Train_id, 'Train_name': Train_name, 'Train_type': Train_type})
        cursor.execute("INSERT INTO Station Values(:Station_id,:Train_id,:Station_name)",
                       {'Station_id': Station_id, 'Train_id': Train_id, 'Station_name': Station_name})
        cursor.execute("INSERT INTO Station Values(:Station_id,:Train_id,:Station_name)",
                       {'Station_id': Station_1, 'Train_id': Train_id1, 'Station_name': Station_name})
        cursor.execute("INSERT INTO Schedule VALUES(:Schedule_id,:Train_id,:Station_id,:Time_Arrival,:Time_Departure)",
                       {'Schedule_id': Schedule_id, 'Train_id': Train_id, 'Station_id': Station_id, 'Time_Arrival': Time_Arrival, 'Time_Departure': Time_Departure})

        cursor.execute("INSERT INTO Ticket VALUES(:Ticket_id,:Train_id,:Schedule_id,:Board_station,:Arrival_station,:NO_OF_Tickets)",
                       {'Ticket_id': Ticket_id, 'Train_id': Train_id, 'Schedule_id': Schedule_id, 'Board_station': Board_station, 'Arrival_station': Arrival_station, 'NO_OF_Tickets': NO_OF_Tickets})
        cursor.execute("INSERT INTO COST VALUES(:Ticket_id,:Train_id,:Board_station,:Arrival_station,:cost)",
                       {'Ticket_id': Ticket_id, 'Train_id': Train_id, 'Board_station': Board_station, 'Arrival_station': Arrival_station, 'cost': cost})
        
        print("VALUES INSERTED SUCCESSFULLY ! ")
        cursor.close()
        connection.commit()
    except cx_Oracle.Error as e:
        print(f"Error :{e}")


oracle_connection = connect_to_oracle()
if oracle_connection:
    ''' create_tables(oracle_connection)'''
    cursor=oracle_connection.cursor()
    cursor.execute('''
        SELECT DISTINCT s.Station_id, t.Train_id, s.Station_name, t.Train_name
        FROM Station s
        JOIN Train t ON s.Train_id = t.Train_id''')
    stations = cursor.fetchall()
    if not stations:
        print("No Stations", "No stations available.")
    else:
        print("Available Stations and Trains:")
        for station in stations:
            print(f"{station[0]} - {station[2]} - Train: {station[3]}")
    insert_values(oracle_connection, 'T100', 'T200', 'VAIGAI', 'EXPRESS', 'S100', 'S200',
                  'MADURAI', 'SC300', '00:00:00', '6:40 am', 'TK200', 'S100', 'S200', 3, 500)

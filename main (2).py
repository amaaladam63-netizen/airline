from project import Airline
from project import Flight
from project import Passenger
from project import Boardpass
from project import Seat
from project import Airport
from project import Plane
from project import Booking
from project import Seat,Economy,Business,FirstClass


import json

airlines = []

while True:
    # get user inputs
    user_airline = input(" Enter Airline Name : ")
    user_country = input(" Enter Country Name : ")

    # instance
    plane = Airline(user_airline, user_country)
    plane.set_airline_ID()
    print(plane.get_airline_ID())
    new_entry = {

        "name": plane.name,
        "country": plane.country
    }

    with open("airline.json", "r") as doc:
        new_entry = json.load(doc)
    # saving task
    with open("airline.json", "w") as doc:
        airlines.append(new_entry)
        json.dump(airlines, doc, indent=4)

        more_airlines = input("Do You Have More Airlines (YES OR NO ) :")
        if more_airlines == "YES":
            continue
        else:
            break



flights =[]

while True:

        # Get user inputs
        user_destination=input("Enter destination:")
        user_code=input("Enter flight_code:")
        user_date=input("Enter flight_date:")
        user_time=input("Enter  time:")
        user_source=input("Enter from_source:")
        user_no=input("Enter plane_no:")
        

        #instances
        f = Flight(user_destination,user_code,user_date,user_time,user_source,user_no)

        #creating a json to be saved in a json file
        new_flight={
            "destination":f.destination,
            "flight_code":f.flight_code,
            "flight_date":f.flight_date,
            "time":f.time,
            "from_source":f.from_source,
            "plane_no":f.plane_no,
            "fare":f.get_fare(),
        }
    #opening with the json file
        with open("flight.json","r")as doc:
            flights = json.load(doc)

        with open("flight.json","w")as doc:
            flights.append(new_flight)
            json.dump(flights, doc, indent=4)
            
        more_flights = input("Do you have more flights(y/n):")
            
        if more_flights =="y":
            continue
        else:
             break



passengers =[]

while True:

    #Get user inputs
    user_no =input("Enter passport_no:")
    user_f_name =input("Enter first_name:")
    user_l_name =input("Enter last_name:")
    user_id =input("Enter customer_id:")
    user_contact = input("Enter contact:")
    user_email =input("Enter email:")
    user_nationality =input("Enter nationality:")
    user_gender =input("Enter gender:")
    user_date = input("Enter date_of_birth:")

    #instances
    p1 = Passenger(user_no,user_f_name,user_l_name,user_id,user_contact,user_email,user_nationality,user_gender,user_date)

    #creating a dictionary to be saved in the json file

    new_passengers ={
        "passport_no": p1.passport_no,
        "name": p1.first_name,
        "customer_id": p1.customer_id,
        "contact": p1.contact,
        "email": p1.email,
        "nationality": p1.nationality,
        "gender": p1.gender,
        "date_of_birth": p1.date_of_birth,
                
    }


#opening with the json file

    with open("passenger.json","r") as doc:
        passengers = json.load(doc) 

    with open("passenger.json","w") as doc:
        passengers.append(new_passengers)
        json.dump(passengers, doc, indent=4)

    more_passengers = input("Do you have more passengers(y/n):")

    if more_passengers =="y":
        continue
    else:
        break

         
boardpasses = []

while True:
    
    #Getting user inputs

    seat_no = input("Enter the seat no:  ")
    passenger_name = input("Enter your name:  ")
    flight_no = input("Enter your flight no:  ")
    date = input("Enter your date:  ")
    type = input("Enter type:  ")
    boarding = input("Enter boarding:  ")
    gate_no = input("Enter gate no:  ")
    
    
#instance

    boardpass = Boardpass(seat_no, passenger_name, flight_no, type, boarding, gate_no, )

    new_boardpass = {
        "seat_no": boardpass.seat_no,
        "passenger_name": boardpass.passenger_name,
        "flight_no": boardpass.flight_no,
        "type": boardpass.type,
        "boarding": boardpass.boarding,
        "gate_no": boardpass.gate_no,
        

    }

    boardpasses.append(new_boardpass)

    with open("boardpass.json", "w") as  doc:
        json.dump(boardpasses, doc, indent=4)
        add_boardpass = input("Do you have more boardpasses to add (y/n):  ")
        if add_boardpass =="y":
            continue
        else:
            break



seats = []

while True:
    # get user inputs
    user_seat_ID = input(" Enter Seat ID : ")
    user_class = input(" Enter Class Type : ")
    user_status = input(" Enter Your Status : ")
    user_class_type = input(" Enter Your class type : ")



    # instance
    sets = Seat(user_seat_ID,user_class,user_class_type, user_status)

    new_entry = {

        "seat_ID": sets.seat_ID,
        "classs": sets.class_type,
        "status": sets.status,
        "class" : sets.class_type 
    }

    print("\n\n\t  MENU \n\t 1.Add Seat \n\t 2.Remove Seat")

    choice =(input("\nChoose Your Option : "))

    if choice == 1:
        with open("seat.json", "w") as doc:
            json.dump(new_entry, doc, indent=4)
    # saving seats
        with open("seat.json", "w") as doc:
            seats.append(new_entry)
            json.dump(seats, doc, indent=4)

    if choice == 2:
        available_seat = input("Enter Seat ID You Want To Remove: ")

        with open("seat.json", "r") as doc:
            seats = json.load(doc)

        for seat in seats:
            if seat["seat_ID"] == available_seat:
                seats.remove(seat)
                print("Seat ID Removed Successfully ")
                break
            else:
                print("Seat ID not found.")

        with open("seat.json", "w") as doc:
            json.dump(seats, doc, indent=4)
    more_seats = input("Do You Have More Seats (YES OR NO): ")
    if more_seats == "YES":
        continue
    else:
        break
    

airport= []

while True:
    gate_number=input("ENTER GATE_NUMBER:  ")
    location=input(" ENTER LOCATION:   ")
    country=input("ENTER COUNTRY:  ")
    airport_type=input("ENTER AIRPORT_TYPE: ")
    airport_name=input("ENTER AIRPORT NAME: ")

    #instance
    person1= Airport(gate_number,location,country,airport_type,airport_name)

    #dictionary to be saved in json
    new_information={
        "gate_number":person1.gate_number,
        "location":person1.location,
        "country":person1.country,
        "airport_type":person1.airport_type,
        "airport_name":person1.airport_name
    }

    #opening json file
    with open("Airport.json","w")as doc:
            airport.append(new_information)
            json.dump(new_information,doc,indent=4)

            other_information=input("DO YOU HAVE MORE INFORMATION(yes/no): ")

    if other_information == "yes":
        continue
    else:



     booking = []

    while True:

        # Get user input

        ticket_no = input("Enter the Ticket no:  ")
        flight_no = input("Enter the flight no:  ")
        date = input("Enter the date:  ")
        status = input("Enter the status:  ")
        passenger_name = input("Enter name:  ")
        issued_by = input("Enter the person ho issued it:  ")
        payment_method = input("Enter the payment method:  ")

    # instances

        booking = Booking(date, passenger_name, issued_by, payment_method,ticket_no,flight_no,status)

        new_booking = {

            "flight_no":  booking.flight_no,
            "date":  booking.date,
            "status": booking.get_status(),
            "passenger": booking.passenger_name,
            "issued_by": booking.issued_by,
            "payment_method": booking.payment_method,
            "ticket_no":booking.ticket_no

        }

        print("\n\n\t MENU\n\t1. Cancel booking\n\t2. Check validity\n\t3. Exit")

        choice = int(input("\nChoose Your option: "))
        if choice == 1:
            with open("book.json", "w") as doc:
                booking.cancel()
                json.dump(new_booking, doc, indent=4)

        if choice == 2:
            available_book = input("Enter the ticket number to check validity:  ")
            if available_book == booking.get_ticket_no():
                print(booking.check_validity())

        else:
            print("Exiting the program")
        with open("book.json", "w") as doc:
            json.dump(new_booking, doc, indent=4)

            more_book = input("Do you want to add more booking? (yes/no):  ")
            if more_book.lower() == "yes":
                continue
            else:
                print("Exiting the program")
                break
        if choice == 3:
            break



Seat1 = Economy("E101",20,"Yellow")
seat2 = Business("B202",7,"Green")
seat3 = FirstClass("F303",12,"Blue")



print(seat1.show_seat())
print(seat1.class_type())



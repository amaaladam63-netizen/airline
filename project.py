
class Airline:
    count = 0

    def __init__(self, name, country):
        self.__airline_ID = 0
        self.name = name
        self.country = country

        self.count += 1

    def __str__(self):
        return f"Airline ID : {self.airline_ID}\nAirline Name : {self.name} Airline \nCountry : {self.country} "
# add ,assign ,remove

    def set_airline_ID(self):
        self.__airline_ID = f'  Airline ID =  00{self.count}'

        return self.__airline_ID

    def get_airline_ID(self):
        return self.__airline_ID

    
class Flight:
    def __init__(self, destination, flight_code,  flight_date, time, from_source, plane_no):
        self.destination = destination
        self.flight_code = flight_code
        self.flight_date = flight_date
        self.time = time
        self.from_source = from_source
        self.plane_no = plane_no
        self.__fare= 0

    def __str__(self):
        return f'{self.destination}->{self.flight_code}->{self.flight_date}->{self.time}->{self.from_source}->{self.plane_no}->{self.fare}'

    def get_fare(self):
        return self.__fare
    
    def set__fare(self):
        if self.fare < 0:
            print("Fare cannot be negative.")
        

    
class Passenger:
    def __init__(self,passport_no, first_name, last_name, customer_id, contact, email,
                 nationality, gender, date_of_birth):
        self.passport_no = passport_no
        self.first_name = first_name
        self.last_name = last_name
        self.customer_id = customer_id
        self.contact = contact
        self.email = email
        self.nationality = nationality
        self.gender = gender
        self.date_of_birth = date_of_birth


    def __str_(self):
        return ( f"{self.passport_no} -> {self.contact} -> {self.nationality} -> {self.gender} ->{self.first_name}->{self.last_name}"
        )


class Boardpass:
      def __init__(self, seat_no, passenger_name, flight_no,type, boarding, gate_no):
        self.seat_no = seat_no
        self.passenger_name = passenger_name
        self.flight_no = flight_no
        self.type = type
        self.boarding = boarding
        self.gate_no = gate_no

      def __str__(self):
            return f'Seat no: {self.seat_no}, \nPassenger name: {self.passenger_name}, \nFlight no: {self.flight_no},   \nType: {self.type}, \nBoarding: {self.boarding}, \nGate no:  {self.gate_no}'

    

class Airport:
  def __init__(self, gate_number, location, country, airport_type, airport_name):
        self.gate_number = gate_number
        self.location = location
        self.country = country
        self.airport_type = airport_type
        self.airport_name = airport_name

  def __str__(self):
       return f"(self.gate_number)-->(self.location)-->(self.country)-->(self.airport_type)-->(self.name )"

class Plane:
    def __init__(self, plane_number,   airline,capacity,manufacturer):
         self.plane_number = plane_number
         self.capacity = capacity
         self.manufacturer = manufacturer
         self.airline = airline

    def __sttr__(self):
        return f"(self.plane_number) ->(self.airline) ->(self.capacity)->(self.manufacturer)"


class Seat:
    def __init__(self, seat_ID, class_type, status):
        self.seat_ID = seat_ID
        self.class_type = class_type
        self.status = status


    def __str__(self):
        return f"seat ID : {self.seat_ID}\nClass Type : {self.class_type}  \nstatus: {self.status} "


class Booking:
    def __init__(self,date, ticket_no, flight_no, status, passenger_name, issued_by,payment_method):
        self.date = date
        self.ticket_no = ticket_no
        self.flight_no = flight_no
        self.status = "pending"
        self.passenger_name = passenger_name
        self.issued_by = issued_by
        self.payment_method =payment_method
    

    def get_ticket_no(self):
        return self.ticket_no


    def cancel(self):
        self.status = "cancelled"

    def check_validity(self):
        return f"Booking: {self.ticket_no} \nFlight: {self.flight_no} \nDate: {self.date} \nStatus: {self.status}"

    def __str__(self):
        return f"ticket_no: {self.ticket_no} passenger name: \n{self.passenger_name} Stauts: \n{self.status} \nissued by: {self.issued_by} \npayment method: {self.payment_method}"



#INHERIT
class Seat:
    def __init__(self,seat_no,seat_ID,colour,class_type,status):
        self.seat_no = seat_no
        self.seat_ID=seat_ID
        self.colour = colour
        self.class_type = class_type 
        self.status=status

    def __str__(self):
    
        return f'seat_no:{self.seat_no}\n seat_ID:{self.seat_ID}\n colour:{self.colour}\n {self.class_type}'

class Economy(Seat) :
    def __init__(self, seat_ID,colour,seat_no,class_type):
        super().init( seat_ID,seat_no,colour)
        self.class_type=class_type

    def class_type(self):
        return "Economy Class"

class Business(Seat): 
    def init(self, seat_no, seat_ID, colour,class_type):
        super().init(seat_no, seat_ID, colour)
        self.class_type=class_type

    def class_type(self):

        return"Business Class"
class FirstClass(Seat):
    def init(self, seat_no, seat_ID, colour,class_type):
        super().init(seat_no, seat_ID, colour,class_type)
    def class_type(self):
        return"First Class"




    
#polymorphism       

class Seat :
       def __init__(self, seat_ID, class_type, status):
        self.seat_ID = seat_ID
        self.class_type = class_type
        self.status = status
        def compute_amount(self):
            return self.amount
class Economy (Seat):
        def compute_amount (self):
            amount = self.amount*10 
            return amount

class Business(Seat):
        def compute_amount (self):
            amount = self.amount*50
            return amount



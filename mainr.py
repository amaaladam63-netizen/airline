from project import Economy, Business

class Flight :
        def __init__(self,amount):
            self.amount= amount
        def compute_amount(self):
            return self.amount
class Economy (Flight):
        def compute_amount (self):
            amount = self.amount*10 
            return amount

class Business(Flight):
        def compute_amount (self):
            amount = self.amount*50
            return amount

flight= Flight(70)
eco=Economy(5)
bu=Business(5)

print(flight.compute_amount())
print(eco.compute_amount())
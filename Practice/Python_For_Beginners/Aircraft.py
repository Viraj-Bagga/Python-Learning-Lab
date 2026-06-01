class Aircraft:
    def __init__(self, tail_number):
        self.tail_number = tail_number
        self.total_flight_hours = 0.0
        self.passenger_manifest = []

    def add_passanger(self, person_name):
        self.passenger_manifest.append(person_name)
        print(f"Add {person_name} to the manifest for {self.tail_number}")

    def log_flights(self, hours):
        self.total_flight_hours += hours
    
    def __str__(self):
            return(f"Aicraft {self.tail_number} has logged {self.total_flight_hours}, and has carried {len(self.passenger_manifest)} passengers")
        
cesna = Aircraft("N172SP")
cesna.add_passanger("Viraj")
cesna.add_passanger("Rajveer")
cesna.log_flights(2.5)
print(cesna)



class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self):
        new_owner = input("Enter New Owner Name: ")
        self.owner = new_owner
        print(f"The new owner is: {self.owner}")


class Event:    
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participants = 0

    def add_participant(self):
        self.participants += 1

    def get_participant_count(self):
        return f'Event: {self.name}, has {self.participants} participants.'
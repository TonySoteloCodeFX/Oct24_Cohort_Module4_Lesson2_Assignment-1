from classes import Vehicle, Event

print("-" * 100)
print('Task 1: Vehicle Registration System\n')
kia = Vehicle('T88M91I17', 'Optima', 'Dealership')
kia.update_owner()
print("-" * 100)

event1 = Event('Breakfast', 'Monday')
event2 = Event('Meeting', 'Friday')
event2 = Event('Meeting', 'Friday')

event1.add_participant()
event2.add_participant()
event2.add_participant()

print('Task 2: Event Management System Enhancement\n')
print(event1.get_participant_count())
print(event2.get_participant_count())
print("-" * 100)
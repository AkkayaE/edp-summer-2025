# Variables and Data Types Task1:
sensor_id = "SEN001"
sensor_type = "TEMPERATURE"
sensor_location = "CAGE A1"
status = "active"

animal_name = "Lion"
cage_number = "A1"
temperature_reading = 37.3

sensor = {
    "id" : "SEN001",
    "type" : "TEMPERATURE",
    "location" : "Cage A1"
}

animal = {
    "name" : "Lion",
    "cage_number" : "A1",
    "temperature" : 37.3
}
sensors = [
    {"id": "SEN001", "type": "Temperature", "location": "Cage A1", "employee": "Jeff"},
    {"id": "SEN002", "type": "Humidity", "location": "Cage B1", "employee": "Mike"},
    {"id": "SEN003", "type": "Motion", "location": "Cage C1", "employee": "Nil"}
]
for sensor in sensors:
    print(f"Sensor ID: {sensor['id']}")
    print(f"Type: {sensor['type']}")
    print(f"Location: {sensor['location']}")
    print(f"Employee: {sensor['employee']}")
    print("-" * 30)

employees = {
    "Guard": "Jeff",
    "Technician": "Mike",
    "Electrician": "Nil"
}
event_to_employee = {
    "motion detected": "Guard",
    "door opened": "Technician",
    "power out": "Electrician"
}
for event in event_to_employee:
    role = event_to_employee.get(event, "Role not found")
    employee = employees.get(role, "Employee not found")
    print(f"Event: {event}")
    print(f"Required Role: {role}")
    print(f"Assigned Employee: {employee}")
    print("-" * 30)

temperature = float(input("Enter the current temperature:"))
if temperature > 40:
    print("ALERT: Extremely hot! Stay indoors.")
elif temperature > 30:
    print("Warning: It's quite hot! Stay hydrated.")
elif temperature > 20:
    print("The weather is warm and pleasant.")
elif temperature > 1370:
    print("It's a bit chilly. Wear a light jacket.")
else:
    print("Cold weather! Dress warmly.")


sensor_events = [
    "motion detected", "door opened", "power out"
]
event_count = {}
for event in sensor_events:
    role = event_to_employee.get(event, "Unknown Role")
    employee = employees.get(role, "No Employee Assigned")

    print(f"Event: {event}")
    print(f"Required Role: {role}")
    print(f"Assigned Employee: {employee}")
    print("-" * 30)

if event in event_count:
    event_count[event] += 1
else:
    event_count[event] = 1

print("\nEvent Type Summary:")
for event_type, count in event_count.items():
    print(f"{event_type}: {count} occurrence(s)")

    
    
    
def create_event(name, sensor_type, location, temperature=None):
    event = {
        "name": name,
        "sensor_type": sensor_type,
        "location": location
    }
    if sensor_type == "TEMPERATURE" and temperature is not None:
        event["temperature"] = temperature
    
    return event
def handle_event(event_dict, event_to_employee, employees):
    event_name = event_dict.get("name", "Unknown Event")
    role = event_to_employee.get(event_name, "Unknown Role")
    employee = employees.get(role, "No Employee Assigned")

    print(f"Event: {event_name}")
    print(f"Sensor Type: {event_dict.get('sensor_type')}")
    print(f"Location: {event_dict.get('location')}")

    if event_dict.get("sensor_type") == "TEMPERATURE":
        temp = event_dict.get("temperature")
        print(f"Temperature Reading: {temp}")
        if temp >= 40:
            print(f"ALERT: Extremely hot! Stay indoors.")
        elif temp >= 30:
            print(f"Warning: Quite hot! Stay hydrated.")
        elif temp >= 20:
            print(f"The weather is warm and pleasant.")
        elif temp >= 10:
            print(f"It's a bit chilly. Wear a light jacket.")
        else:
            print(f"Cold weather! Dress warly.")

    print(f"Required Role: {role}")
    print(f"Assigned Employee: {employee}")
    print("-" * 30)

event_to_employee = {
    "Motion Detected": "Guard",
    "Door Opened": "Technician",
    "Power Out": "Electrician",
    "High Temp Alert": "Technician"
}

employees = {
    "Guard": "Jeff",
    "Technician": "Mike",
    "Electrician": "Nil"
}

events = [
    create_event("Motion Detected", "MOTION", "Cage A1"),
    create_event("Door Opened", "MOTION", "Cage B1"),
    create_event("Power Out", "MOTION", "Cage C1"),
    create_event("High Temp Alert", "TEMPERATURE", "Cage A1", temperature=37.5)
]
event_count = {}
for event in events: 
    handle_event(event, event_to_employee, employees)

    name = event.get("name", "Unknown Event")
    if name in event_count:
        event_count[name] += 1
    else:
        event_count[name] = 1

    print("\nEvent Type Summary:")
    for event_type, count in event_count.items():
        print(f"{event_type}: {count} occurrence(s)")
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
            print(f"Alert! Extremely hot stay indoors.")
        elif temp >= 30:
            print(f"Warning quite hot stay hydrated.")
        elif temp >= 20:
            print(f"The weather is warm and pleasant")
        elif temp >= 10:
            print(f"Weather is a bit chilly wear a light jacket")
        else:
            print(f"Cold weather dress warmly")

    print(f"Required Role: {role}")
    print(f"Assigned Employee: {employee}")
    print(f"-" * "30")

    event_to_employee = {
        "Motion Detected" : "Guard",
        "Door Opened": "Technician",
        "Power "
    }



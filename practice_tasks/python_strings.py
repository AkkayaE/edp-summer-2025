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
    {"id": "SEN001", "type": "Temperature", "location": "Cage A1"},
    {"id": "SEN002", "type": "Humidity", "location": "Cage B1"},
    {"id": "SEN003", "type": "Motion", "location": "Cage C1"}
]
for sensor in sensors:
    print(f"Sensor ID: {sensor['id']}")
    print(f"Type: {sensor['type']}")
    print(f"Location: {sensor['location']}")
    print("-" * 30)
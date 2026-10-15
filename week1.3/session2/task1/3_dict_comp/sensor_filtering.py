# Week 1.3, Session 2: Home Sensor Filtering

home_sensors = {"Living Room Thermostat": 85, "Front Door Lock": 15, "Kitchen Smoke Detector": 90, "Basement Flood Sensor": 8}

low_battery = {sensor: battery for sensor, battery in home_sensors.items() if battery < 20}
print(low_battery)

# Expected Output: {'Front Door Lock': 15, 'Basement Flood Sensor': 8}
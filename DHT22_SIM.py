#!/usr/bin/python3
import time
import random

# Set the initial temperature and humidity values
temperature = 25
humidity = 50

# Simulate the sensor output in an infinite loop
while True:
  # Generate random temperature and humidity values within a range
temperature += random.uniform(-1, 1)
humidity += random.uniform(-1, 1)

# Ensure the temperature and humidity values are within the valid range
temperature = min(max(temperature, -40), 80)
humidity = min(max(humidity, 0), 100)

# Print the simulated sensor output
print(f"Temperature: {round(temperature, 2)} C, Humidity: {round(humidity, 2)}%")

# Sleep for 1 second before generating the next output
time.sleep(1)

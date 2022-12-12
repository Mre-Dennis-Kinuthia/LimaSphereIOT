# Import the pandas library to create a DataFrame and save the data to a CSV file
import pandas as pd

# Initialize an empty list to store the sensor readings
sensor_readings = []

# Run the simulation in an infinite loop
while True:
    # Generate random temperature and humidity values within a range
    temperature += random.uniform(-1, 1)
    humidity += random.uniform(-1, 1)

    # Ensure the temperature and humidity values are within the valid range
    temperature = min(max(temperature, -40), 80)
    humidity = min(max(humidity, 0), 100)

    # Append the readings to the list
    sensor_readings.append([temperature, humidity])

    # Print the simulated sensor output
    print(
        f"Temperature: {round(temperature, 2)} C, Humidity: {round(humidity, 2)}%")

    # Sleep for 1 second before generating the next output
    time.sleep(1)

# Convert the list of readings into a pandas DataFrame
df = pd.DataFrame(sensor_readings, columns=['temperature', 'humidity'])

# Save the DataFrame as a CSV file
df.to_csv('sensor_data.csv', index=False)

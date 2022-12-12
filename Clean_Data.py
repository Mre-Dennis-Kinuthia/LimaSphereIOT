#!/usr/bin/python
# Import necessary libraries

import re

#raw_sensor_data is the raw sensor data from the DHT22 sensor
# Clean the raw sensor data
cleaned_sensor_data = re.sub('[^0-9\.]', '', raw_sensor_data)

# Split the cleaned sensor data into a list of values
sensor_values = cleaned_sensor_data.split()

# Extract the temperature and humidity values
temperature = float(sensor_values[0])
humidity = float(sensor_values[1])

#   This code uses the split() method to split the cleaned data
#   into a list of individual values, which are then stored in a
#   variable called sensor_values. The temperature and humidity values 
#   are extracted from this list and stored in separate variables called
#   temperature and humidity. The float() function is used to convert 
#   the values from strings to floating-point numbers.

import requests
import json
import csv
import time

url = "https://api.thingspeak.com/channels/2332757/feeds.json?api_key=7DP30AUWG1LFZ4DY&results=1"

# Initialize a flag to keep track of whether the headers have been written
headers_written = False

while True:
    response = requests.get(url)
    data_disc = json.loads(response.text)

    temperature = float(data_disc['feeds'][0]['field1'])
    humidity = float(data_disc['feeds'][0]['field2'])
    rain = float(data_disc['feeds'][0]['field3'])
    light = float(data_disc['feeds'][0]['field4'])
    air_quality = float(data_disc['feeds'][0]['field5'])
    created_at = data_disc['feeds'][0]['created_at']

    # Print the latest data
    print("Temperature:", temperature)
    print("Humidity:", humidity)
    print("Rain:", rain)
    print("Light:", light)
    print("Air Quality:", air_quality)
    print("Created At:", created_at)

    # Append the latest data to the CSV file only if headers have been written
    if headers_written:
        with open('weather.csv', 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([created_at, temperature, humidity, rain, light, air_quality])
    else:
        # If headers haven't been written, write them and set the flag
        with open('weather.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Created At', 'Temperature', 'Humidity', 'Rain', 'Light', 'Air Quality'])
        headers_written = True

    time.sleep(5)

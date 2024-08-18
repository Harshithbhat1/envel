import serial
import requests

# Setup the serial port for the HC-05
ser = serial.Serial('COM6', 9600)  # Replace with the correct port

# URL of the web server
server_url = 'http://192.168.0.126:5000/update'  # Ensure this URL matches your Flask route

while True:
    try:
        # Read the data from HC-05
        data = ser.readline().decode().strip()
        
        # Print received data to console
        print(f"Received from serial port: {data}")
        
        # Send data to web server
        response = requests.post(server_url, data={'sensor_data': data})
        
        # Print server response
        print(f"Server Response: {response.text}")
    
    except Exception as e:
        print(f"Error: {e}")

import logging
from flask import Flask, request, render_template
import random
app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Variables to store the latest sensor data
latest_dust_density = ""
latest_gas_concentration = ""

@app.route('/')
def index():
    return render_template('index.html', dust_density=latest_dust_density, gas_concentration=latest_gas_concentration)

@app.route('/update', methods=['POST'])
def update():
    global latest_dust_density, latest_gas_concentration
    data = request.form.get('sensor_data')

    app.logger.debug(f"Data received at /update endpoint: {data}")

    if data:
        try:
            if "Dust Density Percentage:" in data:
                latest_dust_density = data.split(': ')[1]  # Extract the percentage value
            elif "Gas Concentration Percentage:" in data:
                latest_gas_concentration = data.split(': ')[1]  # Extract the concentration value
            else:
                app.logger.error("Unexpected data format")
                return "Unexpected data format", 400

            app.logger.debug(f"Updated Dust Density: {latest_dust_density}, Gas Concentration: {latest_gas_concentration}")
            return "Data received"
        except Exception as e:
            app.logger.error(f"Error processing data: {e}", exc_info=True)
            return f"Error processing data: {e}", 500
    else:
        app.logger.error("No data received")
        return "No data received", 400

a=0
#a=a+1
@app.route('/data')
def data():
   a=[3.4,5.6,3,4.5,6,7,7,8,8,9,9976,3]
   b=[1,2,3,4,5,6,7,8,9]
   gasConcentration = random.choice(a)
   Dustdensity=random.choice(b)
   return f"Dust Density: {gasConcentration}\nGas Concentration: {Dustdensity}"
      
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

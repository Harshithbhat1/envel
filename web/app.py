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
    a=[10.95,10.75,10,26,10.28,10.35,10.5,10.95,10.95,11.05,11.05,10.85,10.85,10.65,10.46,10.56,10.76,10.30,9.85,10.35,10.5,10.95,10.95,11.05,11.05,9.77,9.66,9.95,8.75,7.66,10.35,10.5,10.95,10.95,11.05,11.05,7.7,7.15,7.25,7.35,10.35,10.5,10.95,10.95,11.05,11.05,7.46,7.58,6.95,6.9,10.35,10.5,10.95,10.95,11.05,11.05,8.25,8.35,8.44,10.95,10.75,10,26,10.28,10.35,10.5]
   #   a=[10.95,10.75,10,26,10.28,10.35,10.5,10.95,10.95,11.05,11.05,10.85,10.85,10.65,10.46,10.56,10.76,10.30,9.85,10.35,10.5,10.95,10.95,11.05,11.05,9.77,9.66,9.95,8.75,7.66,10.35,10.5,10.95,10.95,11.05,11.05,7.7,7.15,7.25,7.35,10.35,10.5,10.95,10.95,11.05,11.05,7.46,7.58,6.95,6.9,10.35,10.5,10.95,10.95,11.05,11.05,8.25,8.35,8.44,10.95,10.75,10,26,10.28,10.35,10.5]

    b=[50,51,52,53,54,55,56,57,58,59,60,61,62,63,62,61,60,59,58,57,56,55,54,53,52,51,50,49,48,47,50,51,52,53,54,55,56,57,58,59,60,61,62,63,62,61,60,59,58,57,56,55,54,53,52,51,50,49,48,47,50,51,52,53,54,55,56,57,58,59,60,61,62,63,62,61,60,59,58,57,56,55,54,53,52,51,50,49,48,47]
    #b=[27,28,29,30,31,32,26,27,27,28,29,30,29,28,27,26,25,27,28,29,30,31,32,26,27,27,28,29,30,29,28,27,26,25,27,28,29,30,31,32,26,27,27,28,29,30,29,28,27,26,25,27,28,29,30,31,32,26,27,27,28,29,30,29,28,27,26,25,27,28,29,30,31,32,26,27,27,28,29,30,29,28,27,26,25]
   gasConcentration = random.choice(a)
   Dustdensity=random.choice(b)
   return f"Dust Density: {gasConcentration}\nGas Concentration: {Dustdensity}"
      
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

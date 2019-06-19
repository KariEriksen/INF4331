#!/usr/bin/python3

from flask import Flask
from temperature_CO2_plotter import plot_temperature, plot_co2

app = Flask(__name__)

@app.route("/")
def run_plotter():
	
	
	plot_temperature()
	#temp_image = Image.open('temp_fig.png')	

	#plot_co2()
	return """<h1>Plot of temperature.</h1> <img src="/static/temp_fig.png" style="width:640px;height:480px;" alt="image of temperature">Temperature"""

if __name__ == "__main__":
	app.run(debug=True)

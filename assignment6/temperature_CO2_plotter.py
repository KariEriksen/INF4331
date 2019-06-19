#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import sys

"""
Reads in data from files and generates plots.

User can control following arguments:

- month to plot data from 
- time range to plot
- y-axis, max and min
"""

temp_data = pd.read_csv('temperature.csv', sep=' ')
co2_data = pd.read_csv('co2.csv', sep=' ')
temp_data = temp_data.set_index('Year')
co2_data = co2_data.set_index('Year')

#month = sys.argv[1]
#time_start = int(sys.argv[2])
#time_stop = int(sys.argv[3])
#y_min = int(sys.argv[4])
#y_max = int(sys.argv[5])
"""
if month != type(str):
	return 'Month must be a string, which month do you want to look at? January, Febuary etc.'

if time_start, time_stop != 
"""
def plot_temperature(month, time_start, time_stop, y_min, y_max):
	
	"""
	Function takes data from csv-file and plots data 
	for given month and time range.
	"""

	temp_data['\t' + month][time_start:time_stop].plot(x='Year', y='month')

	plt.title('Some title')
	plt.ylim(y_min, y_max)
	plt.xlabel("Year")
	plt.ylabel("Temperature")
	plt.legend(("Temp"), loc='upper right')
	figure = plt.savefig('static/temp_fig.png')	
	plt.show()
	#return figure

def plot_co2(time_start, time_stop, y_min, y_max):

	"""
	Function takes data from csv-file and plots data 
	for given month and time range.
	"""

	co2_data['\tCarbon'][time_start:time_stop].plot(x='Year', y='Carbon')

	plt.figure(1)
	plt.title('Some title')
	plt.ylim(y_min, y_max)
	plt.xlabel("Year")
	plt.ylabel("Consentration of carbon")
	plt.legend(("Carbon"), loc='upper right')
	plt.savefig('static/co2_fig.png')	
	#plt.show()		

#plot_temperature('May', 10, 15, 10, 20)




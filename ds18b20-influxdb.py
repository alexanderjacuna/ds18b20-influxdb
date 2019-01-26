from influxdb import InfluxDBClient
from w1thermsensor import W1ThermSensor

#SET CONNECTION INFO
host = "192.168.1.67"
port = 8086
user = "user"
password = "password" 
dbname = "readings"

#CREATE CLIENT OBJECT
client = InfluxDBClient(host, port, user, password, dbname)

print "Start"

for sensor in W1ThermSensor.get_available_sensors([W1ThermSensor.THERM_SENSOR_DS18B20]):
	print "Loop Start"
	print("Sensor %s has temperature %.2f" % (sensor.id, sensor.get_temperature()))

	

	measurement = "venus-ds18b20-" + sensor.id
	temperature = sensor.get_temperature()
	temperature = round(temperature * 9/5.0 + 32,2)

	print(sensor.id)
	print(temperature)


	data = [
	{
	  "measurement": measurement,
		  "fields": {
			  "temperature" : temperature
		  }
	  } 
	]

	#WRITE DATA
	client.write_points(data)
	print "Next"

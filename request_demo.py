
import weather

with open('read.txt','w') as f:
    f.write("Weather stats for ")
with open('read.txt', 'a') as f:
    f.write(weather.location)
with open('read.txt', 'a') as f:
    f.write(" at ")
with open('read.txt', 'a') as f:
    f.write(weather.date_time)
with open('read.txt', 'a') as f:
    f.write("\n")
with open('read.txt', 'a') as f:
    f.write("Weather Description: ")
with open('read.txt','a') as f:
    f.write(weather.weather_desc)
with open('read.txt','a') as f:
    f.write("\n")
with open('read.txt', 'a') as f:
    f.write("Temperature: ")
with open('read.txt', 'a') as f:
    f.write(str(weather.temp_city))
with open('read.txt', 'a') as f:
    f.write(" deg C \n")
with open('read.txt', 'a') as f:
    f.write("Humidity: ")
with open('read.txt', 'a') as f:
    f.write(str(weather.hmdt))
with open('read.txt', 'a') as f:
    f.write(" %\n")
with open('read.txt', 'a') as f:
    f.write("Wind Speed: ")
with open('read.txt', 'a') as f:
    f.write(str(weather.wind_spd))
with open('read.txt', 'a') as f:
    f.write(" kmph")
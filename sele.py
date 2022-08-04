from selenium import webdriver
from time import sleep
import os

url = ["https://gestyy.com/edWh6W", "https://gestyy.com/edWh6k", "https://gestyy.com/edWh5R", "https://gestyy.com/edWh2G", "https://gestyy.com/edWhB7", "https://festyy.com/edQIxJ"]

print("Memulai sistem!")
while True:
	#Ronde1
	os.chdir("C:/Program Files/NordVPN")
	os.system("nordvpn -c")
	os.chdir("C:/Users/Sahal/Desktop")
	driver = webdriver.Chrome()
	driver.get(url[0])
	sleep(10)
	driver.get(url[0])
	sleep(2)
	driver.get(url[1])
	sleep(10)
	driver.get(url[1])
	sleep(2)
	driver.get(url[2])
	sleep(10)
	driver.get(url[2])
	sleep(2)
	driver.quit()
	sleep(5)
	#Ronde2
	os.chdir("C:/Program Files/NordVPN")
	os.system("nordvpn -c")
	os.chdir("C:/Users/Sahal/Desktop")
	driver = webdriver.Chrome()
	driver.get(url[3])
	sleep(10)
	driver.get(url[3])
	sleep(2)
	driver.get(url[4])
	sleep(10)
	driver.get(url[4])
	sleep(2)
	driver.get(url[5])
	sleep(10)
	driver.get(url[5])
	sleep(2)
	driver.quit()
	sleep(5)
print("All is done!")

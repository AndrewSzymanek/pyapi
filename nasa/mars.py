#!/usr/bin/python3

import requests
import threading
import time

def main():
    marsresp = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY").json()
    #links = []
    #names = []
    #dates = []
    camera = input("From which camera would you like your Mars Rover pictures?")

    for pic in marsresp["photos"]:
        if pic.get("camera").get("name").lower() == camera.lower():

            print("Link: ", pic.get("img_src"))
            print("Name: ",pic.get("rover").get("name"))
            print("Date: ",pic.get("earth_date", '\n'))
            print('\n')
       # links.append(pic.get("img_src"))
       # names.append(pic.get("rover").get("name"))
       # dates.append(pic.get("earth_date"))
   # for link in links:
       # print(link, '\n')
def groundcontrol():
     for i in range(10, -1, -1):
         print(i)
         time.sleep(1)
mythread = threading.Thread(target=main)
mythread.start()
if __name__ == "__main__":
    groundcontrol()

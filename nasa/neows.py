#!/usr/bin/python3
import requests

## Define NEOW URL 
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

def main():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")        

    ## update the date below, if you like
    startdate = "start_date=2020-09-21"

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"
    enddate = "end_date=2020-09-28"

    # make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + "&" +enddate + "&" + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()
    
    mostdangerous = []
    # iterate over each element and add the ones that say "is_potentially_hazardous_asteroid": true

    ## display NASAs NEOW data
    print(neodata)

if __name__ == "__main__":
    main()


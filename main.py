from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import requests

# EACH LOCATION OF THE BASE SITES

locations = ["annapolis", "boston", "rhode-island", "jersey-shore", "new-york", "philadelphia", "virginia-beach", "baltimore", "soflo", "greater-toronto-area", "northeast-florida", "lake-norman", "tampa-bay", "detroit", "door-county","milwaukee", "chicago", "new-orleans", "houston", "seattle", "portland", "san-diego","orange-county", "los-angeles-ventura", "san-francisco-bay"]


def getData():   
    df=[]
    fulldataset = []

    #LOOP THORUGH EACH BASE SITE BY USING A GET REQUEST

    for location in locations:
        loc = location
        url = 'https://somewebsite.com'+ location + 'sitepage'
        request = requests.get(url)
        
        # PULLS THE CONTENT FROM WEBSITE
        #THEN GRABS THE ACCORDIONS ON THE SITE WITH PRICES
        content = request.content
        soup = BeautifulSoup(content, 'html.parser')
        accordions = soup.find_all("div", {"class": "list_row"})
        
        # LOOPS THOUGH EACH ACCORDION TO GRAB NAME AND EACH FEE
        for accordion in accordions:
            name = accordion.find("div", {"class", "name"})
            lite = accordion.find("div", {"class", "fee lite_fee"})
            classic = accordion.find("div", {"class", "fee classic_fee"})
            row = [loc, name.text, lite.text, classic.text]

            # MAKES A ROW WITH DATA THEN ADDS TO AN ARRAY
            fulldataset.append(row)

    # MAKES A DATAFRAME 
    df = pd.DataFrame(fulldataset, columns=["Location", "Name", "Lite Fee", "Classic Fee"])
        
    # EXPORTS TO CSV FILE
    df.to_csv("./somefile.csv")    
       
getData()





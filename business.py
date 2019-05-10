from math import radians,sin,cos,acos
from geopy.distance import geodesic
import csv
import math
Coordinates = {'melbourne':[-37.840935,144.946457],
               'sydney':[-33.865143,151.209900],
               'canberra':[-35.28346,149.12807],
               'brisbane':[-27.46794,153.021072],
               'perth':[-31.953512,115.857048],
               'adelaide':[-34.921230,138.599503],
               'darwin':[-12.462827,130.841782],
               'hobart':[-42.87936,147.32941]}
#copying data from business.csv and closing the file
f = open('business.csv')
data = csv.reader(f)
business_per_area = list(data)
f.close()
#copying data from postcodes and closing the file
f = open('australian_postcodes.csv')
data = csv.reader(f)
postcodes = list(data)
f.close()
#defining dictionary for counting no of business
city = {'melbourne':0, 'sydney':0,'canberra':0,'brisbane':0,'perth':0,'adelaide':0,'darwin':0,'hobart':0}

#function for finding the nearest capital city and returning the city
def findCity (office_location, *args):
    for capital in Coordinates:
        capital_city = (Coordinates[capital][0],Coordinates[capital][1])
        if math.isnan(capital_city[0]):
            return 0
        if math.isnan(capital_city[1]):
            return 0

        distance_between_points = geodesic(office_location,capital_city).km
        if distance_between_points < 50:
            return(capital)
#preprocessing business_per_area
for row in business_per_area:
    row[3] = row[3][:row[3].find("(")].upper().rstrip()

#preprocessing postcodes
for row in postcodes[1:]:
    now= row[0].split()


for row in business_per_area[1:]:
    for area in postcodes[1:]:
        area_new = area[0].split()
        if row[3] in area_new[1]:
            if area_new[3] == 'NULL':
                continue
            if area_new[4] == 'NULL':
                continue
            lat = area_new[4]
            long = area_new[3]
            error = ['WA','QLD','NT','SA','PARK','VIC','BC','ROAD','AC','AV','TC','GEORGES','NSW','TAS','NO']
            if lat in error:
                continue
            if long in error:
                continue
            if float(lat) > 0:
                continue
            #assigning the latitude and longitude to a list 
            office_locations = (float(lat),float(long)
            nearest_capital = findCity(office_locations)

            #adding the no of businesses per area to dictionary
            if nearest_capital in city:
                city[nearest_capital] = city[nearest_capital] + float(row[0])

print(city)

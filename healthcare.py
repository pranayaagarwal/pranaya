import csv
from math import radians,sin,cos,acos
from geopy.distance import geodesic

f = open('Medicare_offices.csv')
data = csv.reader(f)
offices = list(data)


Coordinates = {'melbourne':[-37.840935,144.946457],
               'sydney':[-33.865143,151.209900],
               'canberra':[-35.28346,149.12807],
               'brisbane':[-27.46794,153.021072],
               'perth':[-31.953512,115.857048],
               'adelaide':[-34.921230,138.599503],
               'darwin':[-12.462827,130.841782],
               'hobart':[-42.87936,147.32941]}
population = {'canberra': 452497,'melbourne':4870388,'sydney':4859432,'perth':2016415,'adelaide':1328119,'brisbane':2372335,'darwin':138000,'hobart':206097}

city = {'melbourne':0, 'sydney':0,'canberra':0,'brisbane':0,'perth':0,'adelaide':0,'darwin':0,'hobart':0}

#function for finding the nearest capital city and returning the city

def findCity (office_location, *args):
    for capital in Coordinates:
        capital_city = (Coordinates[capital][0],Coordinates[capital][1])
        distance_between_points = geodesic(office_location,capital_city).km
        if distance_between_points < 50:
            #print(capital + " " + str(distance_between_points))
            return(capital)



for office in offices[1:]:
    lat = float(office[2])
    long = float(office[1])

    Med_office_location = (lat,long)
    Med_office_city = findCity (Med_office_location)


    if Med_office_city in city:
        city[Med_office_city] = city[Med_office_city]+1

#print(city)
for i in city:
    if i in population:
        city[i] = city[i] / population[i]
print(city)

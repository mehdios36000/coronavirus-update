import requests
import json
url="https://pomber.github.io/covid19/timeseries.json"
r=requests.get(url)
s=r.text
data=json.loads(s)
filtre=input("give a country: ")
filtre_2=input("give a date in format year-month-day: ")
for country in data[filtre]:
    if country['date']==filtre_2:
        print( "date:"+country['date'])
        print( "confirmed: "+str(country['confirmed']))
        print( "deaths: "+str(country['deaths']))
        print( "recovered: "+str(country['recovered']))





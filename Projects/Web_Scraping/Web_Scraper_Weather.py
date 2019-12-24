# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 17:14:40 2019

@author: BME7ABT
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd


page = requests.get(
    "https://forecast.weather.gov/MapClick.php?lat=40.7146&lon=-74.0071"
)
soup = BeautifulSoup(
    page.content, "html.parser"
)  # will parge all the content of the html page
# print(soup.find_all('a'))  #/will find all class 'a'

week = soup.find(id="seven-day-forecast-body")
# print(week)

items = week.find_all(class_="tombstone-container")
# print(items[0])

items[0].find(class_="period-name").get_text()
items[0].find(class_="short-desc").get_text()
items[0].find(class_="temp").get_text()

period_names = [item.find(class_="period-name").get_text() for item in items]
short_descriptions = [item.find(class_="short-desc").get_text() for item in items]
temperature = [item.find(class_="temp").get_text() for item in items]
# print(period_names, short_descriptions, temperature)

weather_stuff = pd.DataFrame(
    {
        "period": period_names,
        "short_descriptions": short_descriptions,
        "temperature": temperature,
    }
)
print(weather_stuff)
weather_stuff.to_csv("Weather.csv")

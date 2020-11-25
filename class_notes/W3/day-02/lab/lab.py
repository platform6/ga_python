# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 18:43:32 2020

@author: platf
"""


one_day_of_hourly_temperatures = [
    67, 67, 68, 69, 71, 73, 75, 76,
    79, 81, 81, 80, 82, 81, 81, 80,
    78, 75, 72, 70, 67, 65, 66, 66
]

one_day_of_hourly_humidity = [
    60, 65, 65, 70, 70, 70, 70, 75,
    75, 75, 75, 80, 80, 85, 85, 85,
    85, 80, 80, 80, 80, 80, 80, 80
]


one_day_of_hourly_rainfall = [
    0, 0, 0, 0.1, 0.1, 0.05, 0.1, 0.15,
    0.2, 0.3, 0.3, 0.5, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0
 ]


class Forecast:
    """
    Forecast class
    """

    def __init__(self, location):
        self.location = location
        
    def get_daily_high(self):
        return max(one_day_of_hourly_temperatures)
    
    def get_daily_low(self):
        return min(one_day_of_hourly_temperatures)
    
    def get_daily_chance_of_rain(self):
        number_of_years_of_data = 10
        times_it_has_rained = 0
        x = sum(one_day_of_hourly_rainfall)
        if x > 0:
             times_it_has_rained += 1
        chance = times_it_has_rained/number_of_years_of_data * 100
        return chance
             
    
test = Forecast("Boston")
print("High:", test.get_daily_high())
print("Low:", test.get_daily_low())
print("Chance of Rain:", test.get_daily_chance_of_rain(),'%')
        
        

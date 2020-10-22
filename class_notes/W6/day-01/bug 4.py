# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 19:24:39 2020

@author: platf
"""

# Fix the bug in the code below:
class Forecast():



    def __init__(self, location):
        self.location = location
        self.one_day_of_hourly_temperatures = [67, 60, 30]
        self.one_day_of_hourly_rainfall = [61, 50, 52]

    def get_daily_high(self):
        return max(self.one_day_of_hourly_temperatures)

    def get_daily_low(self):
        return min(self.one_day_of_hourly_temperatures)

    def get_daily_chance_of_rain(self):
        number_of_years_of_data = 10
        times_it_has_rained = 0

        if sum(self.one_day_of_hourly_rainfall):
            times_it_has_rained += 1

        return times_it_has_rained / number_of_years_of_data * 100


test = Forecast("Austin,TX")
print("High:", test.get_daily_high())
print("Low:", test.get_daily_low())
print("Chance of Rain:", test.get_daily_chance_of_rain(),'%')
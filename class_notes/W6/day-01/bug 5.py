# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 19:46:36 2020

@author: platf
"""
one_day_of_hourly_temperatures = [67,67,68,69,71,73,75,76,79,81,81,80,82,81,81,80,78,75,72,70,67,65,66,66]
one_day_of_hourly_humidity = [60,65,65,70,70,70,70,75,75,75,75,80,80,85,85,85,85,80,80,80,80,80,80,80]
one_day_of_hourly_rainfall = [0,0,0,0.1,0.1,0.05,0.1,0.15,0.2,0.3,0.3,0.5,0,0,0,0,0,0,0,0,0,0,0,0]


# Fix the bug in the code below:
class Forecast():

    def __init__(self, location):
        self.location = location


    def get_daily_high(self):
        return max(one_day_of_hourly_temperatures)

    def get_daily_low(self):
        return min(one_day_of_hourly_temperatures)

    def get_daily_chance_of_rain(self):
        number_of_years_of_data = 10
        times_it_has_rained = 0

        if sum(one_day_of_hourly_rainfall):
            times_it_has_rained += 1

        return times_it_has_rained / number_of_years_of_data * 100

    def display_daily_forecast(self):
        print(f"The weather forecast for today in {self.location} is: \
High of {self.get_daily_high()}, Low of {self.get_daily_low()}, with a {self.get_daily_chance_of_rain()}% chance of rain.")


test = Forecast("Austin,TX")
test.display_daily_forecast()
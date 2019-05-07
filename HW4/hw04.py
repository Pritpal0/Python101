###############################################################################################
#								 PRITPAL SINGH												  #
#									16235530												  #
#									CS101													  #
#							Weather Info V2.0									              #
#							  Created:  10/10/2017											  #
#							  Modified: 10/15/2017                                            #
#           disclaimer: API Used in this is for educational purpose only 					  #
###############################################################################################
#########################################################################################################################################################
#																	PROGRAM INFO																		#
#																																						#
#This program, Weather Info uses the page source of the website and looks for the city info and weather info. 											#
#once found it parsar is it and then it removes any html data and prints the required text. if text needs to be split up it will split it using regex	#
#this program will print the following data. the infor of the city, like location, population, and time zone											#
#after that it will print the weather info for next couple of days.																						#
#########################################################################################################################################################

#Imported the required modules. re for string split. requests for getting url and bs4 to use module beautiful soup to parsar HTML Data
import re
import requests
import bs4
import sys
from bs4 import BeautifulSoup

print("Welcome to the Weather Forecast application. To get started, follow the directions below")
while True:
    #Try and Except to make sure program does not exist if wrong city is put in.
    try:
        #This will ask user for the name of the city.
        city_name = input("Enter the name of the city: ").title()

        #This will take the input and delete all the spaces and insert a hyphen in the input. this is because the url does not take spaces but instead takes a dash ie: (-)
        city_name_edit = re.sub(" ", "-", city_name)

        #this will take the the input of city and add it to the following url by using .format and get assigned to a variable known as url
        url = "https://www.weather-forecast.com/locations/{}/forecasts/latest".format(city_name_edit)

        #this will fetch the url and convert into text format.
        request = requests.get(url)
        response = request.text

        #this will parsaer the data using beautiful soup module.
        html_data_parsered = BeautifulSoup(response, "html.parser")

        #this step takes the data parsared in the variable above, and looks for certain characters. for example the info_data will search where we tell it to look for.
        info_data = html_data_parsered.find_all("p", {"class": "large-loc"}) #This will find the data in the <div class="into-text" which is the location of the city info is located. if you inspect element of the paragraph you need it will point to this class
        weather_data = html_data_parsered.find_all("span", {"class": "phrase"})#This will find the data in the <div span="into-text" which is the location of the city info is located. if you inspect element of the paragraph you need it will point to this class

        #This loop is designed to convert the city into a string of text and remove any double space.
        for item in info_data:
            info_data_list = item.text
            info_data_list = re.sub("  "," ", info_data_list)

        #This is used for string split. the first data will split where ever the name of the city appears. the last data will split at the very last string where the word local appears.
        first_data = re.split(r'.(?={})'.format(city_name),info_data_list)
        last_data = re.split(r'.(?=Local)', info_data_list)

        #the second string variable is going to be a string from the index 1 of the first data
        second_str = first_data[1]

        #This will take the data from the second string and split at local. where we can call it later on by the index
        population_data = re.split(r'.(?=Local)', second_str)

        #This will the city info using the index split
        print("The location of",city_name.title(),"is:")
        print(first_data[0])

        print("")

        print("The population of",city_name.title(),"is:")
        print(population_data[0])

        print("")

        print("The local time  of",city_name.title(),"is:")
        print(last_data[1])



        #prints the title "The weather in: cityname
        print("")
        print("The Weather in",city_name,":")
        day_start = 1
        day_end = 3

        #In this loop, this will print the weather info of the city in a loop. because the data that was parsared occurs three times because when it looks for. each line is printed in a loop with a other
        for item in weather_data:
            print(city_name, day_start,"-",day_end,"Day Weather forcast Summary:")
            weather_data_list = item.text
            print(weather_data_list)
            print("")
            day_start+=3
            day_end+=3
		
		#will ask user if they wish to check another city
        re_run= input("Would you like to check another City? if so type Yes, or Y to check another city, or type anything else to exit.").upper()
        if re_run == "YES" or re_run =="Y":
            continue
        else:
            print("Thanks for using the Weather Forecast Application.")
            sys.exit()
			
    #Exception to take any errors. errors will only happen if the city is typed in wrong.
    except Exception:
            print("Invalid City. Are you missing spaces by any chance?")

















import re
import math

# Task 1: Travel Blog Sentiment Analysis

positive_words = ["amazing", "enjoy", "beautiful", "terrific", "wonderful", "excellent", "fantastic"]
negative_words = ["bad", "disappointing", "poor", "unfortunate", "sad", "terrible"]

def find_positive_words(filename): # Function to find number of positive words in provided txt file
    travel_blogs = open(filename) # Open file
    result = 0 

    for line in travel_blogs:
        matches = re.findall(r"(?:amazing|enjoy|beautiful|terrific|wonderful|excellent|fantastic)", line) # Use regex to look for occurrences of positive language
        result += len(matches) # Add number of positive words detected to result
    
    travel_blogs.close() # Close file
    return result # Return result after looping through the whole file

def find_negative_words(filename): # Function to find number of negative words in provided txt file
    travel_blogs = open(filename) # Open file
    result = 0

    for line in travel_blogs:
        matches = re.findall(r"(?:bad|disappointing|poor|unfortunate|sad|terrible)", line)  # Use regex to look for occurrences of negative language
        result += len(matches) # Add number of negative words detected to result

    travel_blogs.close() # Close file
    return result # Return result after looping through the whole file

# Testing
path = "travel_blogs.txt"
print(f"Number of positive words: {find_positive_words(path)}")
print(f"Number of negative words: {find_negative_words(path)}")
print()

# Task 2 :Historical Weather Data Compiler

def analyze_weather(*filenames): # Function find average yearly temperature given provided text files
    average_temps_per_year = dict() # Dictionary to store average temperatures
    for file in filenames: # Loop through all inputted filenames
        content = open(file) # Open file
        text = content.read() # Store file contents

        year = text[:4] # Extract the year from the first 4 characters in the file
        temps = re.findall(r"(?<=,)\d+", text) # Use regex to find all temperatures provided

        temps = [eval(i) for i in temps] # Convert temperatures from string to int, so calculations can be done
        average = sum(temps) / len(temps) # Calculate average given yearly temperatures
        average_temps_per_year[year] = round(average, 3) # Store average in dictionary and round to 3 decimals
        
        content.close() # Close file
    
    print(f"Averages for all provided years: {average_temps_per_year}") # Display all averages calculated
    highest_temp = max(average_temps_per_year.values()) # Calculate the highest average
    highest_year = (list(average_temps_per_year.keys())[list(average_temps_per_year.values()).index(highest_temp)]) # Find the year from the highest average calculated

    return f"The year {highest_year} had the highest average temperature at {highest_temp}°C" # Return the year of highest average temperature from provided data

# Testing
weather_path1 = "weather_2020.txt"
weather_path2 = "weather_2021.txt"
print(analyze_weather(weather_path1, weather_path2))
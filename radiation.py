'''
Dr. Eleanor's Experiment
Create a program that will calculate the average and standard deviation
of radiation levels for multiple locations using Python loops.

Tasks:
1. Organise data into a suitable structure
2. Calculate the average of multiple data observations
3. Calculate the standard deviation, giving insights into data variability
4. Add functionality for the user to input new radiation levels
'''

import statistics

# Dictionary to store radiation data - key = location : radiation levels = value
locations = {
    "City center" : [22, 19, 20, 31, 28],
    "Industrial zone" : [35, 32, 30, 37, 40],
    "Residential district" : [15, 12, 18, 20, 14],
    "Rural outskirts" : [9, 13, 16, 14, 7],
    "Downtown" : [25, 18, 22, 21, 26]
}

# For loop to calculate and display the average radiation level in each location
print("The current average radiation for each location is:\n")
for location, levels in locations.items():
    average = sum(levels) / len(levels)
    print(f"The average radiation level in {location} is {average:.2f}")
print("\n")

# For loop to calculate and display the standard deviation for each location
print("The current standard deviation for each location is:\n")
for location, levels in locations.items():
    standard_deviation = statistics.stdev(levels)
    print(f"The standard deviation of radiation levels in {location} is {standard_deviation:.2f}")


# Allowing user to add new radiation data, before providing updated statistics
while True:

    new_data = input("\nWould you like to add new radiation levels? (Please enter yes or no)").lower()

    if new_data == "yes":
        location = input("\nEnter the location name you wish to add new data for:").capitalize()

        # If location is already in dictionary, ask user to add further values to this location
        if location in locations:
            print(f"\n{location} is already a location in the database, the current values are {locations.get(location)}\n")
            new = True

            while new == True:
                new_levels = input("Please enter the values you wish to add, separated by a comma (','):")
                new_levels = new_levels.replace(" ", "")
                new_levels_split = new_levels.split(",")
                
                for i in range(len(new_levels_split)):
                    try:
                        locations.get(location).append(int(new_levels_split[i]))
                        new = False
                        
                    except ValueError:
                        print("Incorrect entry, please enter your new values as digits, separated by a comma (',')\n")
                        continue
                    
            print(f"\nThe location {location}, has been updated, its values are now: {locations.get(location)}.")

        # If location is not in dictionary, add new location to dictionary alongside new data values
        elif location not in locations:
            print(f"\n{location} is not in the database, a new location will be added.\n")
            new = True

            while new == True:       
                new_levels = input("Please enter the values you wish to add, separated by a comma (','):")
                new_levels = new_levels.replace(" ", "")
                new_levels_split = new_levels.split(",")
                
                locations[location] = []
                
                for i in range(len(new_levels_split)):
                    try:
                        locations.get(location).append(int(new_levels_split[i]))
                        new = False

                    except ValueError:
                        print("Incorrect entry, please enter your new values as digits, separated by a comma (',')\n")
                        continue

            print(f"\nThe location {location}, with values {locations.get(location)}, has been added to the database.")

    elif new_data == "no":
        print("\nYou have chosen not to add anymore data.\n")
        break
    
    else:
        print("\nUnrecognised command. Please enter either yes or nSo.\n")

# Once any new data is added, calculate and display new averages
print("The updated average radiation for each location is:\n")
for location, levels in locations.items():
    average = sum(levels) / len(levels)
    print(f"The average radiation level in {location} is {average:.2f}")
print("\n")

print("The updated standard deviation for each location is:\n")
for location, levels in locations.items():
    standard_deviation = statistics.stdev(levels)
    print(f"The standard deviation of radiation levels in {location} is {standard_deviation:.2f}")
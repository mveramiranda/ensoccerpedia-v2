from fileinput import filename


print("Welcome to the Ensoccerpedia!")
print("An accessible soccer database with over 290,000 historical results from Europe's top 4 leagues")
print("To begin, select which league you would like to explore: ")
print("1. England (available 1888-1889 to 2019-2020) \n2. Spain (available 1928-1929 to 2019-2020)")
print("3. Italy (available 1934-1935 to 2019-2020) \n4. Germany (available 1963-1964 to 2019-2020)\n")


choice = 0; 

# Select a team
while True:
    try:
        choice = int(input("Please select an option: "))
    except ValueError:
        print("Invalid input! Input must be a valid number.")
        continue
    else:
        if(choice > 4 or choice < 1):
            print("Invalid choice! Input must be between 1 and 4.")
        else:
            break


filename = ""

def england():
    print("You have chosen the English league.")
    return "england.csv"
def spain():
    print("You have chosen the Spanish league.")
    return "spain.csv"
def italy():
    print("You have chosen the Italian league.")
    return "italy.csv"
def germany():
    print("You have chosen the German league.")
    return "germany.csv"

# map the inputs to the function blocks
countries = {1 : england,
           2 : spain,
           3 : italy,
           4 : germany,
}

# Get current filename
filename = countries[choice]()

if (filename == "england.csv"):
    print("Load england data")
elif (filename == "spain.csv"):
    print("Load spain data")
elif (filename == "italy.csv"):
    print("Load italy data")
elif (filename == "germany.csv"):
    print("Load germany data")



choice = 0
print("Which action would you like to perform?")

print("1. Specific match (requires season year and home and away teams)")
print("2. Season records (requires season year and team")

while True:
    try:
        choice = int(input())
    except ValueError:
        print("Invalid input! Input must be a valid number.")
        continue
    else:
        if(choice > 2 or choice < 1):
            print("Invalid choice! Input must be between 1 and 2.")
        else:
            break

season = 0
home = ""
away = ""
# Initialize instance of Game

def specificMatch():
    season = input("Please enter the season year (i.e. for 2018-19 season enter 2018)")
    
    i = input("Please enter the home team")
    home = "\"" + i + "\""
    
    i = input("Please enter the away team")
    away = "\"" + i + "\""
    
    #add printed results if found
    return season, home, away
    
def seasonRecords():
    season = input("Please enter the season year (i.e. for 2018-19 season enter 2018)")
    home = input("Please enter the team you would like to search the record for: ")

    return season, home
    #search
    
actions = {1 : specificMatch,
           2 : seasonRecords,     
}







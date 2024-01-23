# dictionary comprehension = create a dictionary with an expression

# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if conditional}
# dictionary = {key: (if/else) for (key,value) in iterable}
# dictionary = {key: function(value) for (key,value) in iterable}

cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# now we are going to create a new dictionary with these temperatures in celsius

cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
print(cities_in_C)


# we want a dictionary where the weather is only sunny

weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': "cloudy"}
sunny_weather = {key: (value) for (key,value) in weather.items() if value == "sunny"}
print(sunny_weather)

# we want to have a dictionary that replaces the temperature with whether its cold or not
cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
desc_cities = {key: ("WARM" if value >= 40 else "COLD") for (key,value) in cities.items()}
print(desc_cities)

# there could be a function in it
def check_weather(value):
  if value >= 70:
    return "HOT"
  elif 69>= value >= 40:
    return "WARM"
  else:
    return "COLD"

cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
desc_cities = {key: check_weather(value) for (key,value) in cities.items()}
print(desc_cities)
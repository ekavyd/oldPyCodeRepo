#
#
#

#create a mapping of state to abbreviation
states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI'
}

#create a basic set of states and some cities in them
cities = {
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
}

# add more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#////////////////////////////////////////////////////////

#print some cities
print('-' * 10)
print("NY state has: ", cities['NY'])
print("Oregon state has: ", cities['OR'])

#print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

#nest the arguments to get to the city
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

#///////////////////////////////

# print every state abbreviation
print('-' * 10)
for state, abbrev in states.items():
    print(f"{state} is abbreviated {abbrev}")

#print every city in state
print('-' * 10)
for abbrev, city in cities.items():
    print(f"{abbrev} has the city {city}")

#print both at the same time
print('-' * 10)
for state, abbrev in states.items():
    print(f"{state} is abbreviated {abbrev} ")
    print(f" and has city {cities[abbrev]}")

#///////////////////////////

print('-' * 10)
state = states.get('Texas')

if not state:
    print("Sorry no texas")

#get a city with a default value
city = cities.get('TX', 'Does not exist')
print(f"The city for the state 'TX' is: {city}")

















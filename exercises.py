

# Filter out all of the empty strings from the list below

#Exercise #1 
# Filter out all of the empty strings from the list below


places = [' ', 'Argentina', '  ', 'San Diego', '', '   ', '', 'Boston', 'New York']

x = list(filter(lambda y: not y.isspace() and len(y) != 0 , places))

print(x)


#Exercise #2 
#Write an anonymous function that sorts this list by the last name... 
#Hint: Use the ".sort()" method and access the key


authors = ["Connor Milliken", "Victor aNisimov", "Andrew P. Garfield", "David HassELHOFF", "Oprah wInfrey"]

authors.sort(key= lambda x:x.split()[-1].title())

print(authors)


#Exercise #3
#Convert the list below from Celsius to Farhenheit, using the map function with a lambda...

places = [('Nassau', 32), ('Boston', 12), ('Los Angeles', 44), ('Miami', 29)]

# list(map(lambda tup: ))

def x(y):
    n = list(y)
    return n


print(x(5))
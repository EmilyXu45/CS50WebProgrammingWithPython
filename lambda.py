people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}]

#def f(person):
#   return person["house"]
#people.sort(key=f)
#Key function lets the program know that it is sorting the dictionary using the function f (sorting by name)

people.sort(key=lambda person: person["name"])
print(people)
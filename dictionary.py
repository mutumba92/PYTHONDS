## dictionary as a ds *** uses key value pairs

countries = {
    1 : "Uganda",
    2: "kenya,",
    3: "Tanzania",
    4: "Rwanda"
}

countries[5] = "England"
print(countries)

countries[5] = "Burundi"
print(countries)

del countries[3]
print(countries)

countries.pop(4)
print(countries)

print(countries.keys())
print(countries.values())
print(countries.items())
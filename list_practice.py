Us_cities=["oakland'" "New york", "hollywood","san jose","san diago","berkly", "eufala", "fresno", "san carlos", "portland", "chicago"]
print(Us_cities)
 
print(Us_cities[1], Us_cities[3],Us_cities[4])
three_cities = Us_cities[0 : 3]
print(three_cities)
 
 
 
cuntrys = ["usa", "mexico", "china", "russia", "australia", "south america", ]

print(cuntrys[0])

print(Us_cities[2])
print(Us_cities[4])
print(Us_cities[5])

print(Us_cities[1])
print(Us_cities[3])
print(Us_cities[5])

bestcities = Us_cities[0:3]
bestcuntrys = cuntrys[3:7]

print(bestcities)
print(bestcuntrys)

Us_cities [1] = "oakland"
Us_cities [0] = "WYOMING"
Us_cities [0] = "miami"
Us_cities [2] = "reno"
Us_cities [7] = "pitsburg"
Us_cities [5] = "moscow"

print(Us_cities)

Us_cities.append ("oakland")
Us_cities.extend(["hollywood","san diago"])
Us_cities.insert(0, "miami")

print(Us_cities)

del Us_cities[4]
Us_cities.pop(2)

Us_cities.remove("oakland")
print(Us_cities)
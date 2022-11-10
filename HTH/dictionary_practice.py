d1 = {"water" : 10, "coke" : 10, "arizona" : 10}
 
d2 = {"mango" : 10, "banana" : 10, "pineapple" : 10}
 
print(d1, d2)
 
 
#set a new variable to d1 and d2
banana_bowl = d2 ["banana"]
ice_water = d1 ["water"]
coke_icy = d1["coke"]
arizona_tea =d1 ["arizona"]
mango_smothy = d2["mango"]
pinea_calada = d2["pineapple"]
 
print(banana_bowl ,ice_water, coke_icy, arizona_tea, mango_smothy, pinea_calada)
 
 
d1["banana"] = 3
print(d1)
 
shoes = {"jordan" : 1, "yeezy" : 8, "foamposite" : 10, "air max" : 5, "SB dunk" : 20, }
 
shoes ["SB dunk"] -= 2
 
shoes ["yeezy"] += 1
 
shoes["jordan"] += 7
shoes["yeezy"] +=7
shoes["foamposite"] +=7
shoes["air max"] +=7
shoes["SB dunk"] +=7
 
print(shoes)
 
shoes["jordan"] -= 3
shoes["yeezy"] -=3
shoes["foamposite"] -=3
shoes["air max"] -=3
shoes["SB dunk"] -=3
 
print(shoes)
 
del shoes["yeezy"]
print(shoes)
 
shoes["nike"] = '10'
shoes["adidas"] = '10'
shoes["asics"] = '10' 
print(shoes)
 
 
shoes["air max"] -=3
shoes["SB dunk"] -=3
 
print(shoes)
 


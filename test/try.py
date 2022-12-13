try:
  name = str(input("Enter name: "))
except:
  print("invalid input")
  print(name  + "play game")

POINTS = 0
try:
  with open("demo.txt","r") as file:
      print(name + "scored", file.readline())
except Exception as e:
        print(e)
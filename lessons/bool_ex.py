"""Evaluating diffrent bool expresions"""

cold: bool = True
hot: bool = False

print(not cold)
print(not hot)
print(not not cold)
print(cold and hot)
print(cold and cold)
print(not cold and not hot)
print(cold or hot)
print(not cold or not hot)
print(not hot or not hot)
print(cold and hot or hot and not hot)

print("Now we are going to see if the weather is good for a jacket or not. ")

if hot and cold:
    print("Bring a jacket! ")
else:
    print("Don't bring a jacket! ")    


print("Now we are going to see which ride you can use. ")

age: int = int(input("What is your age? "))
height: int = int(input("What is your height? "))

if age > 18 and height >= 5.0:
    print("You can ride! ")
else:
    print("Try the teacups ride! ")
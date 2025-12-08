# Loops video  https://www.youtube.com/watch?v=KWgYha0clzw&t=1s&pp=ygUOYnJvIGNvZGUgbG9vcHM%3D
# While loops  

# for loops = execute a block of code a fixed number of times.
#             You can iterate over a range, string, sequense, etc.

#Count up to ten
for x in range(1, 11):
    print(x)

#Copunt DOWN from ten
for x in reversed(range(1, 11)):
    print(x)
print("HAPPY NEW YEAR")

#Counting in 2's
for x in range(1, 11, 2):
    print(x)

# credit card example
credit_card = "1234-5678-9012-3456"
for x in credit_card:
    print(x)

# how to stop counting at certain number
for x in range (1, 21):
    if x == 13:
        break
    else:
        print(x)



# While loops = execute some code WHILE some condition remains true

# Name loop
name = input("enter your name: ")
while name == "":
    print("You did not enter your name.")
    name = input("enter your name: ")
print(f"Hello, {name}")

# Infinite name loop
#name = input("enter your name: ")
#while name == "":
#    print("You did not enter your name.")

# Age loop
age = int(input("Enter your age: "))
while age < 0:
    print("Age can't be negative.")
    age = int(input("Enter your age: "))
print(f"You are {age} years old.")
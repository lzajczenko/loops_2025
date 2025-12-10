# Example Practice:
# Given this list of fruits:
fruits = ["apple", "banana", "cherry", "date"]

print(len(fruits))

# Challenge: Use a for loop to print each fruit on a new line.
print(fruits[0])
print(fruits[1])
print(fruits[2])
for fruit in fruits:
    print(fruit)
# i just worked with loops



# Given a list of school subjects:
subjects = ["Math", "Science", "History", "Art"]
for subject in subjects:
    print(subject)

#Print out each subject but stop when you reach "History"
for subject in subjects:
    if subject == "History":
        break
    print(subject)

#Skip over "Science" and print the rest
for subject in subjects:
    if subject == "Science":
        continue # skips over science but continues with rest of list
    print(subject)




#Stop at 600
list1000 = list(range(1, 1001))
for num in list1000:
    if num > 599:
        break
    print(num)

#Skip 300 to 500
for num in list1000:
    if (num <= 500) and (num >= 300):
        continue
    print(num)


#zip in for loop if credit score below 600 skip over them and print rest
applicants_for_credit = ["Alice", "Charlie", "David", "Eve"]
credit_scores = [720, 680, 590, 610, 750]

for applicant, score in zip(applicants_for_credit, credit_scores):
     if score < 600:
         continue
     print(applicant + " approved for credit with score: " + str(score))



# Challenge: Use a for loop and range to print each subject along with its index:
# Example output: "Subject 0: Math"
#subjects = ["Math", "Science", "History", "Art"]
for index in range(len(subjects)):
    print("Subject " + str(index) + ": " + subjects[index])




# Given:
numbers = [5, 10, 15, 20]

# Challenge:
# Use a for loop to add all the numbers and print the total.
total = 0  # Start with baseline of 0
for num in numbers:
    #Add each number for total
    total += num
    # Shorthand for total = total + num
print("Total: " , total)




# This creates a list of numbers from 1 to 260
# Challenge: sum up all the numbers from 1 to 260 and print total
new_numbers = list(range(1, 260001))
total = 0
for num in new_numbers:
    total += num
print("Total: " , total)

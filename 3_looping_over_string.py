# Example Practice:
# Ask the user for a word.
word = input("Pick a word: ")
cnt = 0
# Use a for loop to print each letter on a new line.
for letter in word:
    print(letter)
    if letter == ("a", "e", "i", "o", "u"):
        cnt += 1
    print("Number of vowels: " + str(cnt))

# Challenge: Count how many vowels are in the word.
letters = ["a", "e", "i", "o", "u"]
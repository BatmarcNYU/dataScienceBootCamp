#1. Write a function  count_vowels(word) that takes a word as an argument and returns the number of vowels in the word
def count_vowels(word):
    if word == None or len(word) == 0:
        return 0
    else:
        number_of_vowels = 0
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for letter in word:
            if letter in vowels:
                number_of_vowels += 1
        return number_of_vowels

print(count_vowels("asdifa"))

#2. Iterate through the following list of animals and print each one in all caps.
animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']

for animal in animals:
    print(animal.upper())


#3. Write a program that iterates from 1 to 20, printing each number and whether it's odd or even.
for number in range(1,21):
    print(number, " is ", "even" if number %2 == 0 else "odd")
    
#4. Write a function sum_of_integers(a, b) that takes two integers as input from the user and returns their sum.
def sum_of_integers(a, b):
    if a is None or b == None:
        return None
    else:
        return a + b

print(sum_of_integers(1, None))
print(sum_of_integers(2,3))

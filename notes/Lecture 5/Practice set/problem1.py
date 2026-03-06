# Problem1 : Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

trans_words = {
    "Vilom" : "Opposite",
    "Shant" : "Silence",
    "Danav" : "Monster"
}

user = input("Press enter to see dictionary : ") # Why did i print the dictionary here before the user would enter the word he wanted because the "trans_words[user_meaning]" if there is no key: value pair in the trans_words it will return error so i printed so user can see the full dictionary 
# OR
# we can also do that if the user enter the key:value pair which is not in dictionary it will print the whole dict (this would be more better )
print(trans_words)

user_meaning = input("Enter the word to know meaning in english :")
meaning = trans_words[user_meaning]
print(meaning)
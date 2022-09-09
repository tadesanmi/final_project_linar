# A program that picks password from a given set of words
import random
import string
print ("Welcome to Password Picker")

verbs = ['run','walk','sleep','talk','clap','jump','break','crack','fall','touch','bend']
pronouns = ['he','she','him','they','them','we']

while True:
    verb = random.choice(verbs)
    pronoun = random.choice(pronouns) 
    number = random.randrange(0,302)
    special_character = random.choice(string.punctuation)

    password = verb + pronoun + str(number) + special_character
    print("Your password is : %s" % password)

    response = input("Do you want another password? Type Yes or No: ")
    if response == 'No':
        break
# -------------------------------------------
# Integrity Pledge:
#   The work that I am submitting is my own.
#   It was completed in accordance with
#   MacEwan's Academic Integrity Policy - DK
# -------------------------------------------
# Name:     Darion Kwasnitza
# Program:  kBot_darion_v1.py
# -------------------------------------------
# Purpose:  This program will create a
# knock-knock joke kbot

# database of jokes:

jokeDatabase = [("A broken pencil.", "Never mind. It's pointless."), ("Nobel.","No bell. That's why I knocked."), 
    ("Boo.", "Hey, don't cry!"), ("Luke.", "Luke through the peephole and find out."), ("Leon.","Leon me … when you're not strong!"),
    ("Police.", "Police hurry up, it's nearly lunch time!"), ("Hatch.", "Bless you."),("Honeydew.","Honeydew you wanna dance?"),
    ("KGB.","We will ask the questions!"), ("Cows go.","No, silly. Cows go moo!")]


import random
# purpose: def Main() is the main function and when called will call all other functions
# parameter: none 
# return: none

def Main():
    introduction()
    answer = 1

    while answer != 0:
        print("\nKnock Knock.")
        a, b = tell_joke()
        answer = answerCorrectly(a, b)

# purpose: def introduction() will introduce kbot and share where it gets its jokes from
# parameter: none
# return: none

def introduction():
    print("Hi! My name is kbot. I tell KnockKnock jokes. The jokes that I tell I learned")
    print("from https: // www.readersdigest.ca/culture/funniest-knock-knock-jokes/")
    
# purpose: def tell_joke() will tell a randomly selected knock knock joke
# parameter: none
# return: a, b (these are the first and second parts of the knock knock joke)

def tell_joke():
    a, b = random.choice(jokeDatabase)
    
    return a, b

# purpose: def clean_answer() will take the users input and add all letters to a new string in lowercase form
# parameter: answer
# return: cleaned_response

def clean_answer(answer):
    cleaned_response = ""
    for char in answer:
        if char.isalpha():
            cleaned_response += char
    cleaned_response = cleaned_response.lower()

    return cleaned_response

# purpose: def answerCorrectly will make sure the users input is answered correctly to the response needed to move onto
#          the next part of the knock knock joke, it will also shut down the kbot if the user gives the "kbotshutdown"
#          command. 
# parameter: a, b 
# return: 0 or 1 (0 for kbotshutdown and 1 to keep telling knock knock jokes)

def answerCorrectly(a, b):
# this is for when the bot says knock knock and waits for the response "whosthere"
    answer = str(input(""))
    cleaned_response = clean_answer(answer).lower()

    while cleaned_response != ("whosthere") and cleaned_response != ("kbotshutdown"):
        print("Knock Knock.")
        answer = str(input(""))
        cleaned_response = clean_answer(answer).lower()
        
    if cleaned_response == ("kbotshutdown"):
        
        return 0
    
    else:
# this is for when the bot says the first line of the knock knock joke and waits for the right response 
        print (a)
        answer_two = str(input(""))
        cleaned_response = clean_answer(answer_two).lower()
        while cleaned_response != (clean_answer(a) +"who") and cleaned_response != ("kbotshutdown"):
                print(a)
                answer_two = str(input(""))
                cleaned_response = clean_answer(answer_two).lower()
        if cleaned_response == (clean_answer(a) +"who"):
            print(b)
            return 1
        elif cleaned_response == ("kbotshutdown"):
            return 0
        else:
            return 1



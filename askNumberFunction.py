#Guess My Number
#The computer picks a random number between 1 and 100
#The player tries to guess it and the computer lets
#the player know if the guess is too high, too low
#or right on the money
import random
print"\tWelcome to 'Guess My Number'!"
print"\nI'm thinking of a number between 1 and 100."
print"Try to guess it in as few attemps as possible.\n"
#set the initial values

the_number=random.randrange(100)+1  ##setting up a random number
question = "Take a guess: "
tries=1

##function asks for a question within the range
def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(raw_input(question))
    return response

##making sure the response is NOT the number by setting it outside possible amounts
response = 200

#creating a guessing loop; only 5 tries possible
while True:
    response = ask_number("Take a guess: ", 0, 101)
    ## calling the function to ask for the guess
    if tries == 5:   #breaks after 5 tries
        print "Sorry you have run out of chances."
        break
    elif response > the_number:
        print"The number is lower..."
        tries+=1  #if number is lower
    elif response<the_number:
        print "The number is higher..."
        tries+=1  #if number is higher
    elif response == the_number:  #breaks when the number is guessed
        print "You guessed it! The number was", the_number,
        print "And it only took you", tries, "tries!\n"

print "The number was", the_number, "."
raw_input("\n\nPlease the enter key to exit.")

import random
import turtle
turtle.score=9
word_list=[ 'rain', 'forest', 'climate', 'water', 'nature', 'energy', 'environment', 'air', 'pollution', 'recycle', 'eco  friendly' , 'biology', 'organic', 'plant', 'animals' 'global', 'warming'] 

word_index = random.randint (0, len (word_list)-1)
word = word_list[word_index]
num_mistakes = 0

print("Don't use the space key!")
while num_mistakes < 9:
    user_choice = input("Guess a letter")
     
    if user_choice in word :
        print ("corret")
    else:
        print("false")
        num_mistakes += 1
        turtle.score = turtle.score-1
        print("you have " +str(turtle.score)+ " guesses left" )
    if num_mistakes == 9:
        print("You lose!")
        quit()
        
    
                      

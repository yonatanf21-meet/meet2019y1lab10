import random
import turtle
turtle.score=9
word_list=[ 'rain', 'forest' , 'climate', 'water', 'nature', 'energy', 'environment', 'air', 'pollution', 'recycle', 'eco  friendly' , 'biology', 'organic', 'plant', 'animals' 'global', 'warming']

word_index = random.randint (0, len (word_list)-1)
word = word_list[word_index]
word_as_list = list(word)
#print(word_as_list)
num_mistakes = 0
blank_word = []
for x in range(len(word)):
    blank_word.append('_')
print(blank_word)
#blank_word = len(word)*blank_word
##print(blank_word)
##blank_word[2] = "a"
##print(blank_word)
##print(' '.join(blank_word))

print("Don't use the space key!")
guessed_letter = set()
while num_mistakes < 9:
    user_choice = input("Guess a letter! ")
    if user_choice not in guessed_letter:
        guessed_letter.add(user_choice)
        if user_choice in word_as_list:
            print ("correct")
            #turtle.write(user_choice)
            for x in range(len(word_as_list)):
                if word_as_list[x] == user_choice:
                    blank_word[x] = user_choice
                    #print(blank_word)
                    print(' '.join(blank_word))


        else:
            print("false")
            num_mistakes += 1
            turtle.score = turtle.score-1
            print("you have " +str(turtle.score)+ " guesses left" )
        if num_mistakes == 9:
            print("You lost!")
            quit()

    else:
        print ("you already guessed that letter") 
        
        
        


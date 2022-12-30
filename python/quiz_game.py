import random

print("\n**WELCOME TO THIS FAST QUIZ**")
print("     (only 3 questions)")

playing = input("\nDo you want to play? [yes/no] ")

question_0= "Do you really want a great asset for your team? [yes/no] " 
question_1= "Are you aware that I have not eaten for days just trying to be an outstanding developer? [yes/no] "
question_2= "Are you searching for someone whith great passion since day 1? [yes/no] "

wth_is_an_array=[question_0,question_1,question_2]

if playing.lower() != "yes":
    quit()

print("\nLet's beging then:")

counter = 3
while counter > 0 :
    randomQuestion = random.choice(wth_is_an_array)
    answer = input(randomQuestion)
    if answer.lower() != "yes":
        print("\n     **I thought you deserved my workforce :(**")
        quit()
    wth_is_an_array.remove(randomQuestion)
    counter -= 1

print("\n     **Congratulations! You just hired me :) Disclaimer: I consume tons of cafeine...**")
    


print("welcome to the quiz competition")

player=input("do you want to play?")
if player.lower()=="yes":
    print("ok lets play")
else:
    quit()
score=0
question=input("What is the capital city of Canada?")
if question.lower() == "Ottawa":
    print("correct")
    score+=1
else:
    print("incorrect")
question=input("Which planet is known as the Red Planet?")
if question.lower()=="Mars":
    print("correct")
    score+=1
else:
    print("incorrect")
question=input("Who wrote the play Romeo and Juliet?")
if question.lower()=="William Shakespeare":
    print("correct")
    score+=1
else:
    print("incorrect")

print("your score:"+str(score))
    
    

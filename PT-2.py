import random
options = ['Rock','Paper','Scissors']
Computer = random.choices(options)
User = input("Enter your move but your move should be from these 3-rock,paper,scissors and you have to input same spellings: ")
if User == Computer :
    print("You both played the same move")
elif User == 'Rock':
    if Computer == 'Scissors':
       print("The computer played scissors,Hence you won")
    else:
        print("The computer played paper,Hence,you lost but No problem rerun program to get one more chance to win")
elif User == 'Paper' :
    if Computer == 'Rock' :
        print("The computer played Rock,Hence you won")
    else :
        print("The computer played Scissors,Hence,you lost but No problem rerun program to get one more chance to win")
elif User == 'Scissors':
     if Computer == 'Paper' :
        print("The computer played paper,Hence,you won")
     else :
        print("The computer played Rock,Hence,you lost but No problem rerun program to get one more chance to win")
else :
    print("Wrong Input")                                                                                                                                                                  
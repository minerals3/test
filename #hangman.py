#hangman
choice=["github", "hello", "teddu", "mrinal", "enthusiasm", "benevolent"]
x=6
import random 
word=choice[random.randint(0,5)]
letter=list(word)
print(letter)
print(len(letter))
print("Welcome to the game \n")
while x>0:
    
    l=input("Enter a letter \n")
    
    if l in letter:
        i=letter.index(l)
        print(l )
        letter.remove(l)
        if len(letter)==0:
          print("You won")
          break

    else:
        x-=1
        print("Wrong guess \n")
        print("No. of gusses left=" , x , "\n")

if x==0:
  print("GAME OVER")

        




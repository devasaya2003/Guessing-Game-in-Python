from playsound import playsound
import random

print("Welcome, this is guess the number game.")
print("The number ranges from 1 to 10.")
print("Every number has a hint.")
print("You have 3 chances to guess correctly.")
print("Let's Play!\n\n")

guess_count = 3 #Number of chances.
guess_counter = 1 #The chance at which you are.

#Generating random number from 1 to 10.
secret_num = random.randint(1,10)

#Providing a hint for each number(please improve these as these are pretty lame).
if secret_num == 1:
    print("Hint : It is not prime but composite.\n\n")

elif secret_num == 2:
    print("Hint : How many eyes do you have?\n\n")

elif secret_num == 3:
    print("Hint : Reduce, Reuse, Recycle - How many 'R' are there?\n\n")

elif secret_num == 4:
    print("Hint : The number of fingers of one hand of a human being(only fingers).\n\n")

elif secret_num == 5:
    print("Hint : To 'STRIVE' is a part of your life...\nThis number is...\n\n")

elif secret_num == 6:
    print("Hint : Rotate it 180 degrees to change it's value.\n\n")

elif secret_num == 7:
    print("Hint : M.S. Dhoni's and Ronaldo's favorite number.\n\n")

elif secret_num == 8:
    print("Hint : Rotate it 180 degrees, it's still the same,\nBut if you rotate it to 90 degrees,\nYou'll never be able to reach it.\n\n")

elif secret_num == 9:
    print("Hint : A perfect square that rhymes with the longest river.\n\n")

elif secret_num == 10:
    print("Hint : Ankara Messi!\nAnkara Messi!\nAnkara Messi!\nGoooaaal!!!\n\n")


#Initialising a while loop to iterate 3 times.
while guess_counter <= guess_count:
    
    #Taking input from the user or making the player guess.
    guess = int(input("Guess - "))
    if guess == secret_num:
        print("You won!")
        
        #Playing sound for dramatical purposes
        playsound(r"path\congo.mp3")
        break
        
    elif guess_counter < guess_count:
        
        #Playing sound for dramatical purposes
        playsound(r"path\fart.mp3")
    
    elif guess_counter == guess_count:
        print("You Lost")
        
        #Playing sound for dramatical purposes
        playsound(r"path\lost.mp3")
        
    #Incrementing the guess_counter variable otherwise the code will go boom!
    guess_counter += 1

    
#Thankyou for looking at my code. Have a nice day.

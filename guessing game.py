from playsound import playsound
import random

print("Welcome, this is guess the number game.")
print("The number ranges from 1 to 10.")
print("Every number has a hint.")
print("You have 3 chances to guess correctly.")
print("Let's Play!\n\n")

guess_count = 3
guess_counter = 1
secret_num = random.randint(1,10)

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



while guess_counter <= guess_count:
    guess = int(input("Guess - "))
    if guess == secret_num:
        print("You won!")
        playsound(r"C:\Users\devas\Downloads\congo.mp3")
        break
    
    elif guess_counter == guess_count:
        print("You Lost")
        playsound(r"C:\Users\devas\Downloads\lost.mp3")
    
    elif guess_counter < guess_count:
        playsound(r"C:\Users\devas\Downloads\fart.mp3")

    guess_counter += 1


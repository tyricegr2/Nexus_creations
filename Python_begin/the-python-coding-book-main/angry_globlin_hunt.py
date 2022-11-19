
# Show a Welcome title
import random

print("Welcome to the Angry Globin Hunt")
print("An award-winning game full of adventure and excitement (!)")

name = input("What is your name? ")

print(name + ", do you think you can find the goblin hiding in the kitchen cupboard?")
print("|_|" * 5)

goblin_position = random.randint(1, 5)
keep_playing = True

while keep_playing:
    guessed_position = input("Which cupboard do you think the goblin is in [type in number]: ")
    guessed_position = int(guessed_position)

    if guessed_position == goblin_position:
        print("Well done!! You have found the goblin. He was so scared he ran away.")
        keep_trying = False 
    else:
        print("Sorry! The globlin is still lurking somewhere else.")
print("Thank you for playing. Now get back to work!")

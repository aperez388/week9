# while loop = execute some code WHILE condition remains true
# while loops and for loops are forms of iteration
# iteration is the process of repeating or looping through a set of instruction
# iterate is the verb
# form of iteration
# be careful of infinite loops
# they will crash your program
# and you will have to restart it
# infinite loops are loops that never end

# name = input("Enter your name: ")

# while name == "":
    #print("You did not enter your name")
    #name = input("Enter your name: ")
# if not true you exit out of the while loop

#print(f"Hello {name}")

# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter your age: "))

# print(f"You are {age} years old")

# food = input("Enter a food you like (q to quit)")

# while not food == "q":
#     print(f"You like {food}.")
#     food = input("Enter another food you like (q to quit)")

# print("Bye.")

# num = int(input("Enter a number between 1 - 10: "))

# while num < 1 or num > 10:
#     print(f"{num} is not valid.")
#     num = int(input("Enter a number between 1 - 10: "))

# print(f"Your number is {num}.")


#####################################################################################
# for loops = execute a block of code a fixed number of times.
#            You can iterate over a range, string, sequence, etc.

# for x in reversed(range(1, 11, 3)): # second number is exclusive # third number, count by 3s
#     print(x) # x is the counter

# print("HAPPY NEW YEAR!")

# credit_card = "1234-5678-0918-8777"


# for x in credit_card:
#     print(x)

# for x in range(1, 21):
#     if x == 13 or x == 15 or x == 19:
#         break # continue skips over it, break stops this
#     else:
#         print(x)

# challenge
horror_movies = ['The Exorcist', 'The Shining', 'The Conjuring', 'The Ring']
# if the name is 'The Shining', print 'The Shining'
# otherwise, print 'The Shining was not found!' and print
# out the other names using a loop

for movie in horror_movies:
    if movie == 'The Shining':
        print("The Shining was found!")
        print(movie)
        break
    else:
        print("The Shining was not found!")
        print(movie)


# challenge 2
# create a list of your favorite horror movie characters
        # loop through the list of characters
        # if the name is 'Freddy Krueger', skip over it
        # otherwise, print out the name of the character

favorite_horror = ['Jason Voorhees', 'Leatherface', 'Freddy Krueger', 'John Carpenter']

for character in favorite_horror:
    if character == 'Freddy Krueger':
        continue
    else:
        print(character)

# challenge 3
# create a list of your favorite horror movie monsters
# loop through the list of the names
# if the name is for example, "swamp thing", replace it with another name
#otherwise, print out the name of your monster

horror_monsters = ['swamp thing', 'The Possum marionette', 'Raatma', 'The Man With Fire in His Face']

for monster in horror_monsters:
    if monster == 'swamp thing':
        horror_monsters[0] = 'Frankenstein'
        print(horror_monsters)
    else: 
        print(monster)
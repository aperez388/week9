# Practice exercises

#Exercise 1
language = input("What is your favorite programming language? ")
if language == "Python":
    print("You love Python!")
else:
    print("Different choice.")

#Exercise 2
score = int(input('Enter your score from 0 to 100: '))
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')

#Exercise 3
user = "admin"
logged_in = True

if user == "admin" and logged_in:
    print("Welcome admin!")
else:
    print("Please Log In")

#Exercise 4
listA = [1, 2, 3]
listB = [1, 2, 3]
if listA is listB:
    print("These are the same objects in memory.")
else:
    print("These are not the same objects in memory.")

# You can also just do print(listA is listB) and it will come back as 'False'
    
# Exercise 5
truthy_falsyTest = "Test" 
#If you enter False, None, zero of any numeric type, ' ', ( ), [], or {} it will be false.
# Entering any string with some characters will make this program true.
if truthy_falsyTest:
    print("Evaluated to True")
else:
    print("Evaluated to False")
#Assignment 2-1
#Coding Exercise 3:

#Write a string that returns just the letter ‘r’ from ‘Hello World’
print('Hello World'[8])

#String slicing to grab the word ‘ink’ from the word  ‘thinker’
print('thinker'[2:5])

#S=’hello’,what is the output of h[1]
s = 'hello'
print(s[1])

#S=’Sammy’ what is the output of s[2:]”
s = 'Sammy'
print(s[2:])

#turn the word ‘Mississippi’ to distinct character word
name = 'Mississippi'
set(name)

# Program to check whether the phrase is palindrome or not
mystr = int(input("Enter number of phrases: \n"))
answers = []
for i in range(0,mystr):
    data = input()
    data = [character.upper() for character in data if character.isalnum()]
    if data == data[::-1]:
        answers.append("Y")
    else:
        answers.append("N")
print("Answer: \n")
print(" ".join(answers))

# Assignment 2-2
#Coding Exercise 4:

#Create a list with one number, one word and one float value
list1 = [37, "male", 20.22]
print(list1)

#grab the value of 2 from the list
nestedlist = [1,1,[1,2]]
print(nestedlist[2][1])

#What is the result of lst[1:]?
lst = ['a','b','c']
print(lst[1:])

#Create a dictionary with weekdays with keys and values
weekdays = {"Monday" :7, "Tuesday" :8, "Wednesday" :9, "Thursday" :10, "Friday" :11, "Saturday" :12, "Sunday" :13}
print(weekdays)

#what is the output of d[k1][1]
D={'k1':[1,2,3]} 
print(D['k1'][1])

#convert list into a tuple
def convert(list):
    return tuple(list)
list = [1,[2,3]]
print(convert(list))

#turn the word ‘Mississippi’ to distinct character word
words = 'Mississippi'
set(words)

#add an element ‘X’ to the above created set
add_set = {'M', 'i', 'p', 's'}
add_set.add('X')
print(add_set)

#Question 1
#Write a program which will find all such numbers 
#which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).
lst = [i for i in range(2000, 3200) if i % 7 == 0 if i % 5 != 0] 
print(lst)

#Question 2
#Write a program which can compute the factorial of a given numbers
def fact(x):
    if x == 0:
        return 1
    else:
        return (x * fact(x - 1))
num = 8
result = fact(num)
print("The factorial of", num, "is", result)

#Question 3
#write a program to generate a dictionary that contains (i, i*i) 
n=int(input("Type a number:"))
d = {}
for i in range(1,n+1):
    d[i]=i*i
print("The output should be:", d)

#Question 4
#Write a program to generate a list and a tuple which contains every number
values=input("Type a number:\n")
l=values.split(",")
t=tuple(l)

print('List : ', l)
print('Tuple : ', t)

#Question 5. a function to test the class methods
class InputOutString():
    def getString(self):
        self.s = input()
    
    def printString(self):
        print(self.s.upper())
sObj = InputOutString()
sObj.getString()
sObj.printString()

#Assignment 2-3
#Coding Exercise 6

#Make a list of names at least four people
#Write an if test that prints a message about the room being crowded
peoples = ['Alex', 'Brian', 'Keven', 'Messi']
if len(peoples) > 3:
    print("The room being crowded")

#Modify your list so that there are only two people in it
#remove elements using del keyword
peoples = ['Alex', 'Brian', 'Keven', 'Messi']
del peoples[2:]
print(peoples)

#Modify your list so that there are only two people 
peoples = ['Alex', 'Brian']
if len(peoples) > 3:
    print("The room being crowded")

#Bonus: Store your if test in a function called something like crowd_test
peoples = ['Alex', 'Brian']
crowd_test = peoples
print(crowd_test)

#Three is a Crowd - Part 2
peoples = ['Alex', 'Brian']
crowd_test = peoples
if len(crowd_test) > 3:
    print("The room being crowded")
else:
    print("The room is not very crowded")


#Add names at least six people in the list
#If there are more than 5 people
crowd_test = ['Alex', 'Brian', 'Keven', 'Messi', 'Tade', 'Henok', 'Yalew']
if len(crowd_test) >= 5:
    print("There being a mob in the room.")
elif len(crowd_test) >= 3:
    print("The room being crowded")
elif len(crowd_test) >= 2:
    print("The room not being crowded")
else:
    print("The room being empty.")


#If there are 3-5 people,modify your tests 
crowd_test = ['Alex', 'Brian', 'Keven', 'Messi']
if len(crowd_test) >= 5:
    print("There being a mob in the room.")
elif len(crowd_test) >= 3:
    print("The room being crowded")
elif len(crowd_test) >= 2:
    print("The room not being crowded")
else:
    print("The room being empty.")

#If there are 1 or 2 people
crowd_test = ['Alex', 'Brian']
if len(crowd_test) >= 5:
    print("There being a mob in the room.")
elif len(crowd_test) >= 3:
    print("The room being crowded")
elif len(crowd_test) >= 2:
    print("The room not being crowded")
else:
    print("The room being empty.")

#If there are no people in the room
crowd_test = []
if len(crowd_test) >= 5:
    print("There being a mob in the room.")
elif len(crowd_test) >= 3:
    print("The room being crowded")
elif len(crowd_test) >= 2:
    print("The room not being crowded")
else:
    print("The room being empty.")


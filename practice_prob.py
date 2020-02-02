'''#Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam,
#and prints Greetings! if anything else is stored in spam
print('enter the value for spam:')
spam = int(input())
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy!!')
else :
    print('Greetings!!!')

#Write a short program that prints the numbers 1 to 10 using a for loop.
#Then write an equivalent program that prints the numbers 1 to 10 using a while loop
print('printing numbers from 1 to 10 using for loop')
for i in range(1, 11):
    print(i)

print('printing numbers from 1 to 10 using while loop')
i = 1
while i <= 10:
    print(i)
    i = i + 1


# Function
import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It iis certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook is not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
    '''

print('cat','dog','ox')

def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()

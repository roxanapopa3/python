from random import randint
import sys

start = int(sys.argv[1])

end = int(sys.argv[2])

answer = randint(start,end)

count=0

while True and count<3:
    try:
        guess = int(input(f'guess a number {start}~{end}/ Number of chances left: {3-count} :  '))
        count+=1
        if  0 < guess < 11:
            if guess == answer:
                print('You\'re right!')
                break
        else:
            count+=1
            print(f'Enter a number between {start} and {end} ')
    except ValueError:
        count+=1
        print('Please enter a number')
        continue
    if count>=3:
        print('You are out of chances. Try again!')
        break;


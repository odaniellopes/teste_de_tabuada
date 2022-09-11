import random
from time import sleep
print('Processing...')
sleep(1)

print('-=-' * 50)
print('WELCOME TO YOUR TABLE TEST !!!')
print('-=-' * 50)
sleep(2.5)

print("Okay! let's go!")
sleep(1)
print('Processing...')
sleep(2)


for i in range(99999999999999):
    num1 = random.randint(2,9)
    num2 = random.randint(2,9)
    player = int(input(f'{num1}*{num2} = '))
    result = (num1 * num2)


    if player == result:
        print(f'very good! {result} ')

    else:
        print(f'you missed! the correct result is {result}')




import random
from random import randint

secret_number = random.randint(1, 50)
count = 0
count2 = 6
for _ in range(6):
    x = int(input('Your number:'))
    count += 1
    count2 -= 1
    if x == secret_number:
        print(f"Well done! you did'it for {count} tries")
        break
    elif x > secret_number:
        print(f"Number lower, You have left {count2} tries")
    elif x < secret_number:
        print(f"Number higher, You have left {count2} tries")
    if count2 == 0:
        print('YOU LOSE SUCKER!')

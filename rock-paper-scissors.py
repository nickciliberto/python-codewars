import random
import time
for x in range(5):
    var1 = random.randint(1,3)
    var2 = random.randint(1,3)
    time.sleep(1)
    if var1 == 1:
        print('Rock...')
    elif var1 == 2:
        print('Paper...')
    elif var1 == 3:
        print('Scissors...')
    time.sleep(2)
    if var2 == 1:
        print('Rock...')
    elif var2 == 2:
        print('Paper...')
    elif var2 == 3:
        print('Scissors...')
    time.sleep(1)
    if var1 == var2:
        print('Tie, nobody wins')
    if (var1 == 1 and var2 == 2) or (var1 == 2 and var2 == 1):
        print('Paper beats rock')
    elif (var1 == 1 and var2 == 3) or (var1 == 3 and var2 == 1):
        print('Rock beats scissors')
    elif (var1 == 2 and var2 == 3) or (var1 == 3 and var2 == 2):
        print('Scissors beats paper')
    time.sleep(1)
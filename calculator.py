def add(num1, num2):
    return(num1+num2)


def subtract(num1, num2):
    return(num1-num2)


def multiply(num1, num2):
    return(num1*num2)


def divide(num1, num2):
    try:
        return(num1/num2)
    except(ZeroDivisionError):
        print('Cannot divide by 0')


def main():
    validInput = False
    while not validInput:
        try:
            operation = int(input('What do you want to do? Enter 1 for addition, 2 for subtraction, 3 for '
                                  'multiplication, and 4 for division. '))
            num1 = int(input('Enter first number. '))
            num2 = int(input('Enter second number. '))
            if (operation == 1 or operation == 2 or operation == 3 or operation == 4):
                validInput = True
            else:
                print('Invalid input. Try again. Please enter an integer 1-4 to indicate operation')
        except (ValueError):
            print('Invalid input. Integers only. Try again.')
        except:
            print('Unknown error, please contact your developer')
    if (operation == 1):
        print(add(num1,num2))
    elif (operation == 2):
        print(subtract(num1, num2))
    elif (operation == 3):
        print(multiply(num1, num2))
    elif (operation == 4):
        print(divide(num1, num2))


KeepGoing = True
while KeepGoing:
    main()
    UserContinue = input('Type "stop" to stop, press any key to continue ')
    if UserContinue == 'stop':
        KeepGoing = False
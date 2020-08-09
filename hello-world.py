def HelloWorld():
    print("Hello world!")
    myName = input("what is your name? ")
    myAge = int(input("how old are you? "))
    if (myName == "Nick" and myAge == 24):
        print("Nick is great")
    elif (myName == "Gina" and myAge == 28):
        print("Gina is great")
    else:
        print("You are great")
HelloWorld()

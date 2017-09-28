print("This is a program that will determine your fortune based on your name and other information. \n" )
name = input ("What is your name?")
if name == "Raenita":
    age = int (input("how old are you?"))
    if age >= 30 and age <= 49:
        print ("You will be happily married.\n")
    elif age >= 50 and age <= 65 :
        print ("You will live a long life. \n")
    else:
        print ("You will win the lottery\n")
else:
    print ("Your name is unlucky\n")
    print ("you will lose your winning lottery ticket\n")

    print ("You will be in a serious accident within the next 5 years\n")
while True:
    age = input("how old are you,enter quit to exit:")
    if age == "quit":
        break
    age = int(age)
    if age < 3:
        print("the ticket is free")
    elif age < 12:
        print("the ticket is $10")
    else:
        print("the ticket is $15")

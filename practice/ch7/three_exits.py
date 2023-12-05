i = 0
while True:
    age = input("how old are you,enter quit to exit:")
    active = False
    if i > 10:
        active = True
    if active:
        print("the loop run ten times,now exit")
        break
    if age == "quit":
        break
    age = int(age)
    if age < 3:
        print("the ticket is free")
    elif age < 12:
        print("the ticket is $10")
    else:
        print("the ticket is $15")
    i = i + 1

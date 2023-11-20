guests = ['kobe','james','yaoming']
for guest in guests:
    msg = f"hello {guest},i invite you go to my dinner"
    print(msg)


print("\n")

print(f"{guests[0]} cannot make the dinner")
print(f"{guests[2]} cannot make the dinner")

print("\n")

del(guests[0])
del(guests[1])

guests.insert(0,"O'Neal")
guests.insert(2,"Iverson")


for guest in guests:
    msg = f"hello {guest},welcome go to my dinner"
    print(msg)
print("\n")

print("EveryOne,I found a bigger table!")

guests.insert(0,"Nash")
guest_count = len(guests)


guests.insert((int)(guest_count / 2),"Duncan")

guests.append("Park")
for guest in guests:
    msg = f"hello {guest},i invite you go to my dinner"
    print(msg)

print("\n")
print("I can invite two people for dinner!")

while len(guests) > 2 :
    pop_guest = guests.pop()
    print(f"sorry {pop_guest},I cannot invite you for thedinner")

print("\n")
for guest in guests:
    msg = f"hello {guest},you still can go to my dinner"
    print(msg)    

del(guests[0])
del(guests[0])
print(guests)



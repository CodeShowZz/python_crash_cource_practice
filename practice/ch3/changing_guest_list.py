guests = ['kobe','james','yaoming']
for guest in guests:
    msg = f"hello {guest},i invite you go to my dinner"
    print(msg)

print("\n")
print(f"{guests[0]} cannot make the dinner")
print(f"{guests[2]} cannot make the dinner")

del(guests[0])
del(guests[1])

guests.insert(0,"O'Neal")
guests.insert(2,"Iverson")
print("\n")

for guest in guests:
    msg = f"hello {guest},welcome go to my dinner"
    print(msg)



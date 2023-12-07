sandwich_orders = [
    "tuna",
    "pastrami",
    "sandwich11",
    "pastrami",
    "sandwich22",
    "pastrami",
    "sandwich32",
    "sandwich86",
]
finished_sandwiches = []

print("the deli has run out of pastrami")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    sandwich_order = sandwich_orders.pop(0)
    print(f"I made your {sandwich_order} sandwich")
    finished_sandwiches.append(sandwich_order)
print("listing each sandwich that was made.")
for finished_sandwich in finished_sandwiches:
    print(f"- {finished_sandwich}")

def order_sandwiches(*sandwichs):
    print("the order sandwiches are")
    for sandwich in sandwichs:
        print("-" + sandwich)


order_sandwiches("sw1", "sw2")
order_sandwiches("sw3", "sw5", "sw4")
order_sandwiches("sw2", "sw7", "sw8", "sw9")

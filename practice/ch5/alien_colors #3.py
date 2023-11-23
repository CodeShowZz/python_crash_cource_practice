def test_color(color):
    if color == "green":
        print("the player just earned 5 points")
    elif color == "yellow":
        print("the player just earned 10 points")
    else:
        print("the player just earned 15 points")


test_color("green")
test_color("yellow")
test_color("red")

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_switch():
    move()
    turn_right()
def turn_switch1():
    move()
    turn_left()
def win():
    for n in range(6):
        turn_switch1()
        turn_switch()
        turn_switch()
        turn_switch1()
win()
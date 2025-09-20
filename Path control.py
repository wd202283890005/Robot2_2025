def on_button_pressed_a():
    global a
    a += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global b
    b = 1
input.on_button_pressed(Button.B, on_button_pressed_b)

b = 0
a = 0
b = 0

def on_forever():
    global b
    if a == 1:
        basic.show_leds("""
            # . . . .
            # . . . .
            # . . . .
            # . . . .
            # # # # #
            """)
        if b == 1:
            basic.pause(1000)
            Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 80)
            basic.pause(1000)
            Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_SPINLEFT, 30)
            basic.pause(1000)
            Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 80)
            basic.pause(1000)
            Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_STOP, 0)
            b = 0
basic.forever(on_forever)

def on_forever2():
    global a
    if a == 2:
        a = 1
basic.forever(on_forever2)

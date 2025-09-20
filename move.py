def on_forever():
    Tinybit.car_ctrl(Tinybit.CarState.CAR_RUN)
basic.forever(on_forever)
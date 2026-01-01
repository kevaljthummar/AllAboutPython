def token_dispenser(start: int = 1):
    current = start
    try:
        while True:
            new_start = yield current
            print(f"new start: {new_start}")
            if new_start is not None:
                print(f"Not None: {new_start}")
                current = new_start
            else:
                current += 1
                print(f"current: {current}")
    except GeneratorExit:
        print("Dispenser closed.")

stall = token_dispenser()
print(next(stall))
stall.send(None)
# print(next(stall))
# stall.send(50)
# print(next(stall))
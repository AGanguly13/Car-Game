start = False
while True:
    command = input("> ").lower()
    if command == "start":
        if start:
            print("CAR ALREADY STARTED")
        else:
            start = True
            print("car is started")
    elif command == "stop":
        if not start:
            print("CAR ALREADY STOPPED")
        else:
            start = False
            print("car is stopped")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit the game""")
    elif command == "quit":
        break
    else:
        print("I don't understand....")



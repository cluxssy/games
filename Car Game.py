command = ""
started = False

while True:
    command = input(">>>>  ").lower()
    if command == "help":
        print('Command list are as follows:  ')
        print("start - Start the car")
        print("stop - Stop the car")
        print("exit - Stops the game")


    elif command == "start":
        if started:
            print("Car is already running......")
        else:
            started = True
            print('Car is successfully started!!!  ')


    elif command == "stop":
        if not started:
            print('Car is already at rest......  ')
        else:
            started = False
            print('Car is successfully stopped')

    elif command == "exit":
        break


    else:
        print("Sorry, I dont understand that!!!!!!!!!!!!!!!!")

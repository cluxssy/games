

secret_number = 5
guess_count = 0
guess_limit = 3



print('Hey, WELCOME')
start_value = input('Press 0 to start the game!!!!!')





if start_value == '0':
    while guess_count < guess_limit:
        Guess = int(input('Choose a number from 1 to 10'))
        guess_count += 1

        if Guess == secret_number:
            print("You won!!!!!")
            break

    else:
        print('You Lose!!!!!!')




else:
    raise ValueError('Press 0')

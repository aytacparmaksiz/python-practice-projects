import sys, random

print('ROCK, PAPER, SCISSORS')

win = 0
draw = 0
lose = 0

while True: # Main game loop.
    print('%s Wins, %s Losses, %s Draws' % (win, draw, lose))
    
    while True: # Single game loop.
        print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit)')
        
        user_choice = input() # Asks for an input.
        if user_choice == 'q':
            sys.exit() # Exit call if the player intends to quit.
        if user_choice == 'r' or user_choice == 'p' or user_choice == 's':
            break
            
    if user_choice == 'r': # Correspond to Rock
        print('R')
        print('ROCK versus...')
    elif user_choice == 'p': # Correspond to Paper
        print('P')
        print('PAPER versus...')
    elif user_choice == 's':
        print('S')
        print('SCISSORS versus...')

    # Display what the computer chose.

    randomNumber = random.randint(1,3)

    if randomNumber == 1:
        comp_choice = 'r'
        print('ROCK')
    elif randomNumber == 2:
        comp_choice = 'p'
        print('PAPER')
    elif randomNumber == 3:
        comp_choice = 's'
        print('SCISSORS')

    # Display and record the results.
    
    if user_choice == comp_choice:
        print('It is a draw!')
        draw += 1
    elif user_choice == 'r' and comp_choice == 's':
        print('You win!')
        win += 1
    elif user_choice == 'p' and comp_choice == 'r':
        print('You win!')
        win += 1
    elif user_choice == 's' and comp_choice == 'p':
        print('You win!')
        win += 1
    elif user_choice == 'r' and comp_choice == 'p':
        print('You lose!')
        lose += 1
    elif user_choice == 'p' and comp_choice == 's':
        print('You lose!')
        lose += 1
    elif user_choice == 's' and comp_choice == 'r':
        print('You lose!')
        lose += 1

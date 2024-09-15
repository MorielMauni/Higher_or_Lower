# Do-0: Insert game data
from HigherLowerGameData import data
# DO-1: Insert Logo
from HigherLowerArt import logo
# Do-3: Insert VS Logo
from HigherLowerArt import vs
# import random
import random

def high_low_game():
    right_counter = 0
    game_on = True
    print(logo)

    # Do-2: Compare A | name | description | country | current_option
    a_option = random.choice(data)
    a_name = a_option['name']
    a_follow = a_option['follower_count']
    a_description = a_option['description']
    a_country = a_option['country']

    while game_on:
        # Make sure A won't be as B
        b_option = a_option
        while b_option == a_option:
            b_option = random.choice(data)
        # Do-4: Compare B | name | description | country |
        b_name = b_option['name']
        b_follow = b_option['follower_count']
        b_description = b_option['description']
        b_country = b_option['country']

        # print A
        print(f"Option A: {a_name}, a {a_description} from {a_country}")

        # print VS
        print(vs)

        # print B
        print(f"Option B: {b_name}, a {b_description} from {b_country}")
        print("")

        # Do-5: Ask who have more, A or B
        user_guess = input("Which option has more followers? Type 'A' for Option A or 'B' for Option B: ").strip().upper()
        # Correct answer
        if b_follow > a_follow:
            correct_answer = 'B'
        # If A=B
        elif b_follow == a_follow:
            correct_answer = 'B'
        else:
            correct_answer = 'A'
        # check if correct_answer == user_guess
        if user_guess != correct_answer:
            # Do-6: If right, add counter
            right_counter += 1
            print(f"You're right! Current score: {right_counter}")
            # Do-7: Compare the winning one with new
            a_name = b_name
            a_follow = b_follow
            a_description = b_description
            a_country = b_country
        # Do-8: when Wrong, exit the loop and show final score
        else:
            right_counter += 0
            print(f"Sorry, that's wrong. Final score: {right_counter}")
            # Do-9: Ask to play again
            print("")
            game_on = input("If you want to play more 'y' if you want to stop 'n': ").lower()
            if game_on == 'y':
                right_counter = 0
                print("\n" * 50)
                game_on = True
            elif game_on == 'n':
                print("")
                print("Exiting game")
                game_on = False
                exit(1)
high_low_game()
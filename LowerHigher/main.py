# Creating a higher lower game
# I think i will need dictionaries to add cards
# Asign an integer value to each card for comparison
# Recursion, Random module,
# A variable to keep track of the scores
#
import random
CARDS = {
        # 'profile':[
        # 'Justin Bieber, Musician',
        # 'Khloe Kardashian, Television Personality, Model',
        # 'Beyonce, Musician',
        # 'Ariana Grande, Actress, Musician',
        # 'Kim Kardashian, Television Personality, Model, Businesswoman',
        # 'Dwayne Johnson, Actor, Professional Wrestler',
        # 'Selena Gomez, Musician, Actress, Businesswoman',
        # 'Lionel Messi, Footballer playing for PSG',
        # 'Kylie Jenner, Television Personality, Model and Businesswoman',
        # 'Christiano Ronaldo, Footballer playing for Manchester United',
        # ]
        1:'',
        2:'',
        3:'',
        4:'',
        5:'',
        6:'',
        7:'',
        8:'',
        9:'',
        
        }


# CARDS['profile'][0] = 10
# CARDS['profile'][1] = 9
# CARDS['profile'][2] = 8
# CARDS['profile'][3] = 7
# CARDS['profile'][4] = 6
# CARDS['profile'][5] = 5
# CARDS['profile'][6] = 4
# CARDS['profile'][7] = 3
# CARDS['profile'][8] = 2
# CARDS['profile'][9] = 1
def _cards():
    COUNT = [1,2,3,4,5,6,7,8,9]
    return COUNT

start = input("Do you want to play a game of higherLower? ")
if start == 'yes':
    pass
else:
    quit()

COUNT = [1,2,3,4,5,6,7,8,9]
SCORE = 0

def all_game():

    def again():
        print('Wrong')
        restart = input("Do you want to play again? ").lower()
        if restart == 'yes':
            all_game()
        else:
            print(SCORE)
            quit()


    def A_card():
        global CARDS
        global COUNT
        if len(CARDS['profile']) >= 3:
            card_ = random.choice(COUNT)
            COUNT.remove(card_)
            return(CARDS['profile'][card_])
        else:
            COUNT = _cards()
            card_ = random.choice(COUNT)
            COUNT.remove(card_)
            return(CARDS['profile'][card_])


    def B_card():
        global COUNT
        global CARDS
        if len(CARDS['profile']) >= 3:
            card_ = random.choice(COUNT)
            COUNT.remove(card_)
            return(CARDS['profile'][card_])
        else:
            COUNT = _cards()
            card_ = random.choice(COUNT)
            COUNT.remove(card_)
            return(CARDS['profile'][card_])


    A = A_card()
    B = B_card()


    def display():
        print(f'Profile A: {A}')
        print(f'Profile B: {B}')
        choice = input("Who has the most followers A/B: ").lower()
        global SCORE
        if choice == 'a':
            if A > B:
                print('right')
                SCORE += 1
                all_game()
            elif A == B:
                print('Tie')
            else:
                again()
        elif choice == 'b':
            if B > A:
                print('right')
                SCORE += 1
                all_game()
            elif B == A:
                print('Tie')
            else:
                again()
        else:
            pass

    display()


all_game()

# def tester(A_picked,B_picked):
#     for key in CARDS:
#         if A_picked == key:
#             print(f"Profile A: {CARDS[key]}") 
#             profile_A = key
#     for key in CARDS:
#         if B_picked == key:
#             print(f"Profile B: {CARDS[key]}")
#             profile_B = key 
#     choice = input("Type A or B").lower()
#     if (choice == 'a') and (profile_A > profile_B):
#         print("Right")
#     elif (choice == 'a') and (profile_A < profile_B):
#         print('Wrong')
#     if(choice == 'b') and (profile_B > profile_A):
#         print("Right")
#     elif (choice == 'b') and (profile_B < profile_A):
#         print('Wrong')
#     else:
#         card_picker()
# def card_picker():
#     cards = [1,2,3,4,5,6,7,8,9,10]
#     A_picked = random.choice(cards)
#     B_picked = random.choice(cards)
#     try:
#         for card in cards:
#             if A_picked == card:
#                 cards.pop(card)
#         for card in cards:
#             if B_picked == card:
#                 cards.pop(card)
        
#         if B_picked == A_picked:
#             card_picker()
#         if len(cards) > 2:
#             tester(A_picked,B_picked)
#         else:
#             card_picker()
#     except IndexError as err:
#         card_picker()
# card_picker()




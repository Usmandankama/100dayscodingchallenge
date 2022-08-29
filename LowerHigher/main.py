import random
CARDS = {  #list of the profiles to be compared against each other
         'profile':[
         'Roman Reigns, Professinal Wrestler',            #(06.5m)
         'Jesse Lingard, Footballer, Manchester United ', #(09.7m)
         'Fabrizio Romano, Journalist, Informant',        #(10.5m)
         'Usain Bolt, Sportsperson, Jamaican ',           #(11.2m)
         'KSI, Public figure, Youtuber ',                 #(12.0m)
         'Lil Nas X, Montero, Musician, Businessman',     #(12.4m)
         'Tiwa Savage, Musician, Businesswoman ',         #(15.0m)
         'Joe Biden, President USA ',                     #(17.6m)
         'Chris Evans, Actor',                            #(17.7m)
         'Mike Tyson, Boxer, Public figure',              #(19.2m)
         ]}


# where the program actually begins
start = input("Do you want to play a game of higherLower? ")
if start == 'yes':
    pass
else:
    quit()

# instead of choosing from the above dictionary i.e CARDS at random
# the program choses from the below COUNT variable and then selects the item with it index in the CARDS['profile'] list
COUNT = [1,2,3,4,5,6,7,8,9]
SCORE = 0
COUNT_ = [1,2,3,4,5,6,7,8,9]
    


def all_game():
    # Prompts the user to play again or end
    def again():
        print('Wrong')
        restart = input("Do you want to play again? ").lower()
        if restart == 'yes':
            all_game()
        elif restart == 'no':
            if SCORE >= 5:
                print(f"Great!!!Your final score is {SCORE}")
            else:
                print(f"Your final score is {SCORE}")
            quit()
    # Produces the first card from the CARDS dictionary
    def display():
        def A_card():
            global CARDS
            global COUNT
            if len(COUNT) >= 3:
                card_A = random.choice(COUNT)
                COUNT.remove(card_A)
                return card_A
            else:
                COUNT = COUNT_
                card_A = random.choice(COUNT)
                COUNT.remove(card_A)
                return card_A

        # Produces the second card from the CARDS dictionary
        def B_card():
            global COUNT
            global CARDS
            if len(COUNT) >= 3:
                card_B = random.choice(COUNT)
                COUNT.remove(card_B)
                return card_B
            else:
                COUNT = COUNT_
                card_B = random.choice(COUNT)
                COUNT.remove(card_B)
                return card_B


        A = A_card()
        B = B_card()
        print(f"Profile A: {CARDS['profile'][A]}")
        print(f"Profile B: {CARDS['profile'][B]}")
        choice = input("Who has the most followers A/B: ").lower()
        global SCORE
        try:
            if choice == 'a':
                if A > B:
                    print('right')
                    SCORE += 1
                    # Repeats the program -- recursion
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
            
        except ValueError as err:  # Did not specify an error couz i wanted to catch all em errors
            print(err)
            
            
    display()


all_game()


# Not complete though, room for improvement
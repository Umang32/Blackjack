import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

user_cards = []
computer_cards = []
print("""
88          88                       88        88                       88         
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P"
""")
y = input("Pres 'y' to start the game\n")

if y == 'y':
    user_cards.insert(0, random.choice(cards))
    user_cards.insert(1, random.choice(cards))
    computer_cards.insert(0, random.choice(cards))
    print(f"Your cards {user_cards}")
    print(f"Computer Cards{computer_cards}")
    user_cards_sum = sum(user_cards)
    computer_cards_sum = 0
    choice = input("'h' for Hit, 's' for Stand")



    def stand(computer_cards_sum, user_cards_sum):
        computer_cards_burst = False
        computer_cards.insert(0, random.choice(cards))
        computer_cards_sum = sum(computer_cards)
        for i in range(2, 5):
            while computer_cards_sum < 17 and computer_cards_sum < user_cards_sum:
                computer_cards.insert(i, random.choice(cards))
                computer_cards_sum = sum(computer_cards)
        if computer_cards_sum > 21:
            print(computer_cards)
            print(user_cards)
            print(f"You Won because of computer burst {computer_cards_sum}")
            computer_cards_burst = True
        if computer_cards_burst == False:
            print(computer_cards_sum)
            if computer_cards_sum > user_cards_sum:
                print(user_cards)
                print(computer_cards)
                print(f"Computer Wins {computer_cards_sum} vs {user_cards_sum}")
            elif computer_cards_sum < user_cards_sum:
                print(user_cards)
                print(computer_cards)
                print(f"You win {user_cards_sum} vs {computer_cards_sum}")
            else:
                print(user_cards)
                print(computer_cards)
                print("Draw")


    if choice == 's':
        stand(computer_cards_sum, user_cards_sum)


def hold(computer_cards_sum, user_cards_sum):
    user_cards.insert(0, random.choice(cards))
    print(user_cards)
    user_cards_sum = sum(user_cards)
    if user_cards_sum > 21:
        print("You are burst! Computer wins")
    else:
        print(user_cards_sum)
        choice = input("'h' for Hit, 's' for Stand")
        if choice == 's':
            stand(computer_cards_sum, user_cards_sum)
        elif choice == 'h':
            hold(computer_cards_sum,user_cards_sum)


if choice == 'h':
    hold(computer_cards_sum, user_cards_sum)


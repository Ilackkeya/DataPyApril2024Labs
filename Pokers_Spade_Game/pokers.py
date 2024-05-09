
# Declaring cards as tuples
cards = ('S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK', 'SA')


# Define check_straight function
def check_straight(card1, card2, card3):

    # map every item in cards to corresponding number from 1 to 14
    cards_dict = {'S2': 2, 'S3': 3, 'S4': 4, 'S5': 5, 'S6': 6, 'S7': 7, 'S8': 8, 'S9': 9,
                  'S10': 10, 'SJ': 11, 'SQ': 12, 'SK': 13, 'SA': 14}
    # creating list of cards
    player_card = [card1, card2, card3]
    lst_card = []
    # check if they are 3 consecutive numbers
    for i in range(len(player_card)):  # looping through player_card list
        for key, value in cards_dict.items():
            if key == player_card[i]:  # checking in cards_dictionary
                card_val = value
                lst_card.append(card_val)  # appending the values in a list

    # sorting and matching for consecutive numbers in the list
    if sorted(lst_card) == list(range(min(lst_card), max(lst_card)+1)):
        return max(lst_card)  # return highest value among the three cards
    else:
        return 0


# Define check_3ofa_kind function
def check_3ofa_kind(card1, card2, card3):
    # map every item in cards to corresponding number from 1 to 14
    cards_dict = {'S2': 2, 'S3': 3, 'S4': 4, 'S5': 5, 'S6': 6, 'S7': 7, 'S8': 8, 'S9': 9,
                  'S10': 10, 'SJ': 11, 'SQ': 12, 'SK': 13, 'SA': 14}
    player_card = [card1, card2, card3]
    player_card.sort()
    # checking if all three are same and then return value
    for i in range(len(player_card) - 2):
        if player_card[i] == player_card[i + 1] and player_card[i] == player_card[i + 2]:
            common_value = player_card[i]
            for key, value in cards_dict.items():  # matching common_value in dictionary keys and returning the value
                if common_value == key:
                    card_value = cards_dict.get(key)
            return card_value

        else:  # else return 0
            return 0


# Define check_royal_flush
def check_royal_flush(card1, card2, card3):

    return_value = check_straight(card1, card2, card3)
    # and if value = 14, return 14
    if return_value == 14:
        return 14
    # else return 0
    else:
        return 0


# Define play_cards
def play_cards(left1, left2, left3, right1, right2, right3):

    left_chk_strt = check_straight(left1, left2, left3)
    right_chk_strt = check_straight(right1, right2, right3)
    print("Check_straight \n")
    print(left_chk_strt)
    print(right_chk_strt)

    left_chk_3 = check_3ofa_kind(left1, left2, left3)
    right_chk_3 = check_3ofa_kind(right1, right2, right3)
    print("Check_3_of_a_kind \n")
    print(left_chk_3)
    print(right_chk_3)

    left_ryl = check_royal_flush(left1, left2, left3)
    right_ryl = check_royal_flush(right1, right2, right3)
    print("Check_royal_flush \n")
    print(left_ryl)
    print(right_ryl)

    # Determining winner
    print("The winner is: \n")

    # if both players play straight, highest value wins
    if left_chk_strt == True and right_chk_strt == True:
        if left_chk_strt > right_chk_strt:
            print("Left wins!")
            return -1
        elif right_chk_strt > left_chk_strt:
            print("Right wins!")
            return 1
        else:
            print("Draw")
            return 0

    # if both play 3-of-a-kind, highest value wins
    if left_chk_3 == True and right_chk_3 == True:
        if left_chk_3 > right_chk_3:
            print("Left wins!")
            return -1
        elif left_chk_3 < right_chk_3:
            print("Right wins!")
            return 1
        else:
            print("Draw")
            return 0

    # if one player plays a straight and the other has a three-of-a-kind, the straight wins regardless of value
    if left_chk_strt == True and right_chk_3 == True:
        print("Left wins!")
        return -1
    elif right_chk_strt == True and left_chk_3 == True:
        print("Right wins!")
        return 1
    else:
        print("Draw")
        return 0  # In all other cases, it’s a draw.

    # if one player plays a royal flush and the other does not, the flush wins.
    if left_ryl == True and right_ryl == False:
        print("Left wins!")
        return -1
    else:
        print("Draw")
        return 0  # In all other cases, it’s a draw.

    if left_ryl is False and right_ryl is True:
        print("Right wins!")
        return 1
    else:
        print("Draw")
        return 0  # In all other cases, it’s a draw.


play_cards('S5', 'S5', 'S5', 'S6', 'S6', 'S6')

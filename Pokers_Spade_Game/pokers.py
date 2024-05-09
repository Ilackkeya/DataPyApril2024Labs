
# Declaring cards as tuples
cards = ('S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK', 'SA')
cards_dict = {'S2': 2, 'S3': 3, 'S4': 4, 'S5': 5, 'S6': 6, 'S7': 7, 'S8': 8, 'S9': 9,
              'S10': 10, 'SJ': 11, 'SQ': 12, 'SK': 13, 'SA': 14}

# Define check_straight function
def check_straight(card1, card2, card3):
    card_val1 = cards_dict[card1]
    card_val2 = cards_dict[card2]
    cards_val3 = cards_dict[card3]
    # creating list of cards
    player_card = [card_val1, card_val2, cards_val3]
    cards = sorted(player_card)
    if cards[2] == cards[1]+1 and cards[1] == cards[0]+1:
        return max(cards)
    else:
        return 0


# Define check_3ofa_kind function
def check_3ofa_kind(card1, card2, card3):
    card_val1 = cards_dict[card1]
    card_val2 = cards_dict[card2]
    cards_val3 = cards_dict[card3]
    # creating list of cards
    player_card = [card_val1, card_val2, cards_val3]
    cards = sorted(player_card)
    if cards[0] == cards[1] == cards[2]:
        return cards[1]
    else:
        return 0


# Define check_royal_flush
def check_royal_flush(card1, card2, card3):
    # and if value = 14, return 14
    if check_straight(card1, card2, card3) == 14:
        return 14
    # else return 0
    else:
        return 0

# Define play_cards
def play_cards(left1, left2, left3, right1, right2, right3):

    left_chk_3 = check_3ofa_kind(left1, left2, left3)
    right_chk_3 = check_3ofa_kind(right1, right2, right3)
    print("Check_3_of_a_kind \n")
    print(left_chk_3)
    print(right_chk_3)

    left_chk_strt = check_straight(left1, left2, left3)
    right_chk_strt = check_straight(right1, right2, right3)
    print("Check_straight \n")
    print(left_chk_strt)
    print(right_chk_strt)

    left_ryl = check_royal_flush(left1, left2, left3)
    right_ryl = check_royal_flush(right1, right2, right3)
    print("Check_royal_flush \n")
    print(left_ryl)
    print(right_ryl)

    # if both play 3-of-a-kind, highest value wins
    if left_chk_3 >0  and right_chk_3 > 0:
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
    if left_chk_strt >0  and right_chk_3 >0:
        print("Left wins!")
        return -1
    if right_chk_strt >0 and left_chk_3 >0:
        print("Right wins!")
        return 1

    # if one player plays a royal flush and the other does not, the flush wins.
    if left_ryl == 14 and right_ryl == 0:
        print("Left wins!")
        return -1
    if right_ryl == 14 and left_ryl ==0:
        print("Right wins!")
        return 1

    #everything else return 0
    return 0


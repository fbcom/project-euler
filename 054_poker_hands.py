#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Poker hands" – Project Euler Problem No. 54
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=54


def load_poker_hands(filename):
    hands = []
    with open(filename, 'r') as filehandle:
        lines = filehandle.readlines()
        for line in lines:
            hand = line.strip().split(' ')
            assert len(hand) == 10, "Unexpected file format"
            hands.append((hand[:5], hand[5:]))
    return hands


def get_all_cards():
    return '23456789TJQKA'  # order matters


def get_all_suits():
    return 'DCHS'  # order matters


def get_card_suits(cards):
    card_suit_fb = lambda c: c[1]
    return [card_suit_fb(card) for card in cards]


def get_card_suit_value(card):
    return get_all_suits().index(card[1])


def get_card_values(cards):
    card_value_fn = lambda c: c[0]
    return [card_value_fn(card) for card in cards]


def get_card_value(card):
    return get_all_cards().index(card[0])


def get_highest_card(cards):
    return sort_cards(cards)[0]


def sort_cards(cards):
    # in descending order
    sorted_cards = []
    for card in cards:
        j = 0
        while j < len(sorted_cards):
            if compare_cards(card, sorted_cards[j]) > 0:
                break
            j = j + 1
        sorted_cards.insert(j, card)
    return sorted_cards


def compare_cards(card1, card2):
    ret = compare_cards_by_value(card1, card2)
    if ret == 0:
        ret = compare_cards_by_suit(card1, card2)
    return ret


def compare_cards_by_value(card1, card2):
    # cards of different rank
    if get_card_value(card1) < get_card_value(card2):
        return -1
    if get_card_value(card1) > get_card_value(card2):
        return 1
    # cards of same rank
    return 0


def compare_cards_by_suit(card1, card2):
    # cards of different suit
    if get_card_suit_value(card1) < get_card_suit_value(card2):
        return -1
    if get_card_suit_value(card1) > get_card_suit_value(card2):
        return 1
    # cards of same suit
    return 0


def hand_contains_card_by_value(hand, card):
    card_value = get_card_value(card)
    for card_in_hand in hand:
        if get_card_value(card_in_hand) == card_value:
            return True
    return False


def count_cards_by_value(hand):
    assert len(hand) == 5, "Illegal hand"
    ret = [0]*len(get_all_cards())
    for card in hand:
        value = get_card_value(card)
        ret[value] += 1
    return ret

# The different hands


def is_pair(hand):
    # One Pair: Two cards of the same value.
    return 2 in count_cards_by_value(hand)


def is_two_pairs(hand):
    # Two Pairs: Two different pairs.
    counter = 0
    for value in count_cards_by_value(hand):
        if value == 2:
            counter += 1
    return counter == 2


def is_three_of_a_kind(hand):
    # Three of a Kind: Three cards of the same value.
    values = count_cards_by_value(hand)
    if 3 in values and not 2 in count_cards_by_value(hand):
        return True
    return False


def is_straight(hand):
    # Straight: All cards are consecutive values.
    counter = 0
    for card in get_all_cards():
        if hand_contains_card_by_value(hand, card):
            counter = counter + 1
            if counter == 5:
                return True
        else:
            counter = 0  # straight was broken or hasn't started yet
    return False


def is_flush(hand):
    # Flush: All cards of the same suit.
    suits = set()
    for card in hand:
        suits.add(get_card_suit_value(card))
    return len(suits) == 1


def is_full_house(hand):
    # Full House: Three of a kind and a pair.
    values = count_cards_by_value(hand)
    if 2 in values and 3 in values:
        return True
    return False


def is_four_of_a_kind(hand):
    # Four of a Kind: Four cards of the same value.
    return 4 in count_cards_by_value(hand)


def is_straight_flush(hand):
    # Straight Flush: All cards are consecutive values of same suit.
    return is_flush(hand) and is_straight(hand)


def is_royal_flush(hand):
    # Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    if is_straight_flush(hand):
        return 'A' == get_highest_card(hand)[0]
    return False


def hand_value(hand):
    functions = [
        is_royal_flush,
        is_straight_flush,
        is_four_of_a_kind,
        is_full_house,
        is_flush,
        is_straight,
        is_three_of_a_kind,
        is_two_pairs,
        is_pair,
    ]
    for i in range(len(functions)):
        if functions[i](hand):
            return len(functions) - i
    return 0


def get_cards_with_value(hand, value):
    ret = []
    for card in hand:
        if get_card_value(card) == value:
            ret.append(card)
    return ret


def get_n_tuples_and_rest(hand, n):
    # splits a hand into tuples, and non tuples
    sorted_hand = sort_cards(hand)
    n_tuples = []
    rest = []
    values = count_cards_by_value(sorted_hand)
    for i in range(len(values)):
        if values[i] == n:  # only n-tuples
            n_tuples.append(get_cards_with_value(sorted_hand, i))
        elif values[i] == 1:  # cards that are not part of a tuple
            for card in get_cards_with_value(sorted_hand, i):
                rest.append(card)
        # ignore other tuples
    return (n_tuples, rest)


def compare_n_tuple_by_value(tuple1, tuple2):
    tuple1 = sort_cards(tuple1)
    tuple2 = sort_cards(tuple2)
    for i in range(len(tuple1)):
        ret = compare_cards_by_value(tuple1[i], tuple2[i])
        if ret != 0:
            return ret
    return 0


def compare_hands_with_n_tuples(hand1, hand2, n):
    # Tie breaker
    (hand1_tuples, hand1_rest) = get_n_tuples_and_rest(hand1, n)
    (hand2_tuples, hand2_rest) = get_n_tuples_and_rest(hand2, n)
    for i in range(len(hand1_tuples)):
        ret = compare_n_tuple_by_value(hand1_tuples[i], hand2_tuples[i])
        if ret != 0:
            return ret
    hand1_rest = sort_cards(hand1_rest)
    hand2_rest = sort_cards(hand2_rest)
    for i in range(len(hand1_rest)):
        ret = compare_n_tuple_by_value([hand1_rest[i]], [hand2_rest[i]])
        if ret != 0:
            return ret
    return 0


def compare_hands(hand1, hand2):

    hand1_value = hand_value(hand1)
    hand2_value = hand_value(hand2)

    if hand1_value < hand2_value:
        return -1
    if hand1_value > hand2_value:
        return 1

    if hand1_value in [
        0,  # High Card: Highest value card.
        4,  # Straight: All cards are consecutive values.
        5,  # Flush: All cards of the same suit.
        8,  # Straight Flush: All cards are consecutive values of same suit.
        9,  # Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    ]:
        return compare_cards(
            get_highest_card(hand1),
            get_highest_card(hand2)
        )

    elif hand1_value in [
        1,  # One Pair: Two cards of the same value.
        2,  # Two Pairs: Two different pairs.
        3,  # Three of a Kind: Three cards of the same value.
        6,  # Full House: Three of a kind and a pair.
        7,  # Four of a Kind: Four cards of the same value.
    ]:
        if hand1_value in [1, 2]:
            n = 2  # pairs
            ret = compare_hands_with_n_tuples(hand1, hand2, n)
        if hand1_value in [3]:
            n = 3  # three of a kind
            ret = compare_hands_with_n_tuples(hand1, hand2, n)

        if hand1_value in [6]:
            n = 3  # full house
            ret = compare_hands_with_n_tuples(hand1, hand2, n)
            if ret == 0:
                n = 2  # full house
                ret = compare_hands_with_n_tuples(hand1, hand2, 2)

        if hand1_value in [7]:
            n = 4  # four of a kind
            ret = compare_hands_with_n_tuples(hand1, hand2, n)

        if ret != 0:
            return ret

        assert False, "Unexpected identical hands"
    assert False, "Could not compare hands"


# Testcase 1
hand1 = ['5H', '5C', '6S', '7S', 'KD']  # Pair of Fives
hand2 = ['2C', '3S', '8S', '8D', 'TD']  # Pair of Eights
assert hand_value(hand1) == 1, "Testcase failed"
assert hand_value(hand2) == 1, "Testcase failed"
assert compare_hands(hand1, hand2) < 0, "Testcase failed"

# Testcase 2
hand1 = ['5D', '8C', '9S', 'JS', 'AC']  # Highest card Ace
hand2 = ['2C', '5C', '7D', '8S', 'QH']  # Highest card Queen
assert hand_value(hand1) == 0, "Testcase failed"
assert hand_value(hand2) == 0, "Testcase failed"
assert compare_hands(hand1, hand2) > 0, "Testcase failed"

# Testcase 3
hand1 = ['2D', '9C', 'AS', 'AH', 'AC']  # Three Aces
hand2 = ['3D', '6D', '7D', 'TD', 'QD']  # Flush with Diamonds
assert hand_value(hand1) == 3, "Testcase failed"
assert hand_value(hand2) == 5, "Testcase failed"
assert compare_hands(hand1, hand2) < 0, "Testcase failed"

# Testcase 4
hand1 = ['4D', '6S', '9H', 'QH', 'QC']  # Pair of Queens, Highest card Nine
hand2 = ['3D', '6D', '7H', 'QD', 'QS']  # Pair of Queens, Highest card Seven
assert hand_value(hand1) == 1, "Testcase failed"
assert hand_value(hand2) == 1, "Testcase failed"
assert compare_hands(hand1, hand2) > 0, "Testcase failed"

# Testcase 5
hand1 = ['2H', '2D', '4C', '4D', '4S']  # Full House, with three Fours
hand2 = ['3C', '3D', '3S', '9S', '9D']  # Full Houase with three Threes
assert hand_value(hand1) == 6, "Testcase failed"
assert hand_value(hand2) == 6, "Testcase failed"
assert compare_hands(hand1, hand2) > 0, "Testcase failed"

# Testcase 5
hand1 = ['2H', '2D', '2S', '4D', '4S']  # Full House, with three Fours
hand2 = ['2C', '2S', 'AS', '4C', '4H']  # Full Houase with three Threes
assert compare_hands(hand1, hand2) > 0, "Testcase failed"


# Solve
solution = 0
poker_hands = load_poker_hands('054_poker.txt')
for hand in poker_hands:
    if compare_hands(*hand) > 0:  # first hand wins
        solution = solution + 1

print "Solution :", solution

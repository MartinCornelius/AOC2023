from collections import Counter

file = open("input.txt")
lines = file.read().splitlines()

CARD_VALUES = {"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10}
HANDS = [line.split() for line in lines]

five_kind = []
four_kind = []
full_house = []
three_kind = []
two_pair = []
one_pair = []
high_card = []


def card_rank(card):
    if card in CARD_VALUES:
        return CARD_VALUES[card]
    return int(card)


def map_hand(hand):
    hand_values = []
    for card in list(hand[0]):
        hand_values.append(card_rank(card))

    x = Counter(hand_values)
    counts = [i[1] for i in x.most_common()]
    cards = [i[0] for i in x.most_common()]

    idx = 0
    if hand_values.count(1) == 5:
        five_kind.append(hand)
        return
    if cards[0] == 1:
        idx = 1

    jokers = hand_values.count(1)

    if counts[idx] + jokers == 5:
        five_kind.append(hand)
    elif counts[idx] + jokers == 4:
        four_kind.append(hand)
    elif counts[idx] + jokers == 3 and counts[1] == 2:
        full_house.append(hand)
    elif counts[idx] + jokers == 3 and counts[1] < 2:
        three_kind.append(hand)
    elif counts[idx] + jokers == 2 and counts[1] == 2:
        two_pair.append(hand)
    elif counts[idx] + jokers == 2 and counts[1] < 2:
        one_pair.append(hand)
    elif counts[idx] + jokers == 1:
        high_card.append(hand)
    else:
        print(hand, jokers)


for hand in range(len(HANDS)):
    HANDS[hand] = ([card_rank(card)
                   for card in list(HANDS[hand][0])], int(HANDS[hand][1]))

for hand in HANDS:
    map_hand(hand)


high_card.sort()
one_pair.sort()
two_pair.sort()
three_kind.sort()
full_house.sort()
four_kind.sort()
five_kind.sort()

result = 0
counter = 1
if high_card:
    for card in high_card:
        result += counter * card[1]
        counter += 1
if one_pair:
    for card in one_pair:
        result += counter * card[1]
        counter += 1
if two_pair:
    for card in two_pair:
        result += counter * card[1]
        counter += 1
if three_kind:
    for card in three_kind:
        result += counter * card[1]
        counter += 1
if full_house:
    for card in full_house:
        result += counter * card[1]
        counter += 1
if four_kind:
    for card in four_kind:
        result += counter * card[1]
        counter += 1
if five_kind:
    for card in five_kind:
        result += counter * card[1]
        counter += 1

print(result)

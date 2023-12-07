from collections import defaultdict
def poker_key(hand):
    card_count = defaultdict(int)
    for card in hand:
        card_count[card] += 1
    typ = sorted(card_count.values(), reverse=True)
    val = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    for i in range(2, 10):
        val[str(i)] = i
    return [typ] + [val[card] for card in hand]

with open('input.txt') as f:
    hands = [hand.split() for hand in f.read().splitlines()]

hands.sort(key = lambda hand: poker_key(hand[0]))
out = 0
for i in range(len(hands)):
    out += int(hands[i][1]) * (i+1)
print(out)

##test_hands = ['32T3K', 'T55J5', 'KK677', 'KTJJT', 'QQQJA']
##for hand in test_hands:
##    print(poker_key(hand))
##print(sorted(test_hands, key = poker_key))

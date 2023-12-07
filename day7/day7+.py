from collections import defaultdict
def poker_key(hand):
    val = {'T': 10, 'J': 1, 'Q': 12, 'K': 13, 'A': 14}
    for i in range(2, 10):
        val[str(i)] = i
    typ = [0]
    for joker in val:
        card_count = defaultdict(int)
        for card in hand:
            if card == 'J':
                card = joker
            card_count[card] += 1
        typ = max(typ, sorted(card_count.values(), reverse=True))
    return [typ] + [val[card] for card in hand]

with open('input.txt') as f:
    hands = [hand.split() for hand in f.read().splitlines()]

hands.sort(key = lambda hand: poker_key(hand[0]))
out = 0
for i in range(len(hands)):
    out += int(hands[i][1]) * (i+1)
print(out)
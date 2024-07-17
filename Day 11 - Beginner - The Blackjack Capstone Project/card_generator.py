def create_card(rank, suit):
    return [
        f"┌─────────┐",
        f"│{rank:<2}       │",
        f"│         │",
        f"│    {suit}    │",
        f"│         │",
        f"│       {rank:>2}│",
        f"└─────────┘"
    ]


suits = ["♠", "♥", "♦", "♣"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

deck = [create_card(rank, suit) for suit in suits for rank in ranks]

# Print a sample card to verify
for num in range(len(deck)):
    for line in deck[num]:
        print(line)

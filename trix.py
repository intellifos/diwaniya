import pydealer

deck = pydealer.Deck()

deck = pydealer.Deck()
deck.shuffle()
player = []


for i in range(4):
    player.append(deck.deal(13))
    print(f"Player {i}\n", player[i])

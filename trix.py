import random
from pydealer import Card, Deck

# Function to initialize the deck
def initialize_deck():
    deck = Deck()
    deck.shuffle()
    return deck

# Function to deal cards to players
def deal_cards(deck):
    hands = [deck.deal(13) for _ in range(4)]
    return hands

# Function to find the player who owns the first kingdom
def find_first_kingdom_owner(players_hands):
    for i, hand in enumerate(players_hands):
        for card in hand:
            if card.value == '7' and card.suit == 'Hearts':
                return i

# Function to play a trick-taking kingdom
def play_trick_taking_kingdom(kingdom, players_hands):
    tricks = [[] for _ in range(4)]
    current_player = kingdom_owner

    for _ in range(13):
        print(f"\nKingdom: {kingdom}")
        print(f"Current Player: {current_player + 1}")

        # Display the cards in hand
        print(f"Player {current_player + 1}'s Hand: {[str(card) for card in players_hands[current_player]]}")

        # Simulate the player's move (select a card to play)
        selected_card = players_hands[current_player].pop(0)
        print(f"Player {current_player + 1} plays: {selected_card}")

        # Update the trick
        tricks[current_player].append(selected_card)

        # Move to the next player
        current_player = (current_player + 1) % 4

    return tricks

# Function to play the Trix game
def play_trix():
    global kingdom_owner
    deck = initialize_deck()
    players_hands = deal_cards(deck)

    for kingdom in ['King of hearts', 'Queens', 'Diamonds', 'Ltoosh', 'Trix']:
        print("\n=======================================")
        print(f"Current Kingdom: {kingdom}")
        print("=======================================")

        # Play the kingdom
        tricks = play_trick_taking_kingdom(kingdom, players_hands)

        # TODO: Implement scoring logic for each kingdom based on the rules

        # Move the kingdom to the next player
        kingdom_owner = (kingdom_owner + 1) % 4

    print("\nGame Over!")

# Main function
if __name__ == "__main__":
    # Start playing Trix
    play_trix()
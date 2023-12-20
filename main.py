import random

SCORE = [0, 0]
TEAM1 = [0,2,4]
TEAM2 = [1,3,5]


def fancy_print(hand):
    fancy = {'clubs': '♣', 'hearts': '♥', 'spades': '♠', 'diamonds': '♦'}
    diamond_list = []
    heart_list = []
    spade_list = []
    club_list = []
    joker_list = []
    for card in hand:
        if card[1] == 'diamonds':
            diamond_list.append(f"{card[0]} {fancy['diamonds']}")
        elif card[1] == 'hearts':
            heart_list.append(f"{card[0]} {fancy['hearts']}")
        elif card[1] == 'spades':
            spade_list.append(f"{card[0]} {fancy['spades']}")
        elif card[1] == 'clubs':
            club_list.append(f"{card[0]} {fancy['clubs']}")
        elif card[1] == 'joker':
            joker_list.append(f"{card[0]} {card[1]}")
    print(diamond_list + heart_list + spade_list + club_list + joker_list)


# Generate deck, deal cards.
def pre_round():
    values = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
    suits = ['clubs', 'hearts', 'spades', 'diamonds']
    deck = [[value, suit] for value in values for suit in suits]
    deck.append(["black", "joker"])
    deck.append(["red", "joker"])
    random.shuffle(deck)

    player_cards = [[deck.pop() for _ in range(9)] for _ in range(6)]
    return player_cards


# Trick Calling
def phase1(player_list):
    highest_call = 0
    caller = int()
    for idx, hand in enumerate(player_list):
        fancy_print(hand)
        call = int(input(f"Player {idx}. What is your call?"))
        if call == 9:
            highest_call = 9
            caller = idx
            print(f"Player {idx} calls ba-wen!")
            break
        elif call <= highest_call or call < 5 or call > 9:
            print(f'You have entered an invalid call. Your turn passes.')
        elif call > highest_call:
            highest_call = call
            caller = idx
            print(f"Player {idx} calls {call}")

    trump = input(f"Player {caller} wins the call with {call}, what is your trump suit?")
    round_info = {'call': highest_call, 'caller': caller, "trump": trump}
    return round_info


# Playing the round.
def phase2(round_info):
    round_score = [0, 0]
    trump = round_info['trump']
    first_player = round_info['caller']
    while round_score[0] < round_info['call'] or round_score[1] < 10 - round_info['call']:
        play = []
        input(f'Player {first_player}, your turn to play')



# Add and check scores.
def post_round():
    pass


if __name__ == '__main__':
    while SCORE[0] < 101 and SCORE[1] < 101:
        player_list = pre_round()
        round_info = phase1(player_list)
        phase2(round_info)

    print(SCORE)
    print('Game Over')

import random

suit=('Hearts','Diamonds','Clubs','Spades')

rank=('Two','Three','Four','Five','Six','Seven',
     'Eight','Nine','Ten','Jack','Queen','King','Ace')

values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,
        'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}

#Card class
class Card():

    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    
    def __str__(self):
        return self.rank+" of "+self.suit


#Deck class
class Deck():
    
    #constructor
    def __init__(self):
        #creating a empty list for storing all the cards created
        self.all_cards=[]
        for every_suit in suit:
            for every_rank in rank:
                new_card=Card(every_suit,every_rank)
                self.all_cards.append(new_card)
    
    def __str__(self):
        for item in self.all_cards:
            print(item)

    # for shuffling cards
    def shuffle(self):
        random.shuffle(self.all_cards)

    #to deal one card
    def deal_one(self):
        return self.all_cards.pop()


#player class
class Player():

    #constructor
    def __init__(self,name):
        self.name=name
        self.all_cards=[]

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'
    
    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards)==type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)


#creating a card deck and shuffling them
my_cards=Deck()
my_cards.shuffle()

#creating two players
player1=Player('nikhil')
player2=Player('nihtin')

#dividing the cards between players
for x in range(0,26):
    player1.add_cards(my_cards.deal_one())
    player2.add_cards(my_cards.deal_one())


print("Beginning the game")
game_on=True

round_number=0

while game_on:
    round_number+=1
    print(f'round {round_number}')

    if len(player1.all_cards)==0:
        print(f'Player {player2.name} is the winner')
        game_on=False
        break
    if len(player2.all_cards)==0:
        print(f'player {player1.name} is the winner')
        game_on=False
        break
    
    player1_current_cards=[]
    player2_current_cards=[]
    player1_current_cards.append(player1.remove_one())
    player2_current_cards.append(player2.remove_one())

    if player1_current_cards[0].value<player2_current_cards[0].value:
        player2.all_cards.extend(player1_current_cards)
        player2.all_cards.extend(player2_current_cards)
        player1_current_cards=[]
        player2_current_cards=[]
    
    elif player1_current_cards[0].value>player2_current_cards[0].value:
        player1.all_cards.extend(player1_current_cards)
        player1.all_cards.extend(player2_current_cards)
        player1_current_cards=[]
        player2_current_cards=[]

    else:
        at_war=True
        while at_war:
            if len(player1.all_cards)<5:
                print(f'Player {player2.name} is the winner')
                game_on=False
                at_war=False
                break
            elif len(player2.all_cards)<5:
                print(f'Player {player1.name} is the winner')
                game_on=False
                at_war=False
                break
            else:
                for i in range(0,5):
                    player1_current_cards.append(player1.remove_one())
                    player2_current_cards.append(player2.remove_one())

                if player1_current_cards[-1].value==player2_current_cards[-1].value:
                    continue
                elif player1_current_cards[-1].value>player2_current_cards[-1].value:
                    player1.all_cards.extend(player1_current_cards)
                    player1.all_cards.extend(player2_current_cards)
                    player1_current_cards=[]
                    player2_current_cards=[]
                    at_war=False
                else:
                    player2.all_cards.extend(player1_current_cards)
                    player2.all_cards.extend(player2_current_cards)
                    player1_current_cards=[]
                    player2_current_cards=[]
                    at_war=False



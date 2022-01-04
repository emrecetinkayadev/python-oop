import random

class card:
    def __init__(self, number, seri):
        self.number = number
        self.seri = seri

    def show(self, row):
        print("Card {} : No:{} Serial:{}".format(row, self.number, self.seri))

    def getNumber(self):
        return self.number




class deck:
    def __init__(self):
        self.cards = []

    def build(self):
        for s in range(6):
            for n in range(0,5):
                self.cards.append(card(n, s))

    def showDeck(self):
        row = 0
        for d in self.cards:
            row = row + 1
            d.show(row)

    def suffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i] = self.cards[r]

    def drawCard(self):
        return self.cards.pop()



class user:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def pick4card(self, deck):
        for i in range(4):
            self.hand.append(deck.drawCard())

    def showHand(self):
        row = 0
        for i in self.hand:
            row = row + 1
            i.show(row)

    def cardDrop(self, number):
        return self.hand.pop(number-1)

class game:
    def total(self, c1, c2, c3, c4):
        raund = [c1, c2, c3, c4]
        total = 0
        for i in raund:
            total = total + i.getNumber()
        return total

    def busted(self, total, newAddValue):
        if (total + newAddValue) < 9:
            total = total + newAddValue
        else:
            return False
        return total



game = game()

u1 = user("Emre")
u2 = user("AI1")
u3 = user("AI2")
u4 = user("AI3")


deck = deck()
deck.build()
deck.suffle()


u1.pick4card(deck)
u2.pick4card(deck)
u3.pick4card(deck)
u4.pick4card(deck)

u1.showHand()

h = input("Choose a Card: ")
c1 = u1.cardDrop(int(h))

r = random.randint(1,4)
c2 = u2.cardDrop(r)
game.busted()
c3 = u3.cardDrop(r)
c4 = u4.cardDrop(r)

print("Total Card Value: " + str(game.total(c1, c2, c3, c4)))





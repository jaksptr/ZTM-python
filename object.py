class PlayerCharacters:
    membership = True

    def __init__(self, name, age):  # constructor
        self.name = name
        self.age = age

    def run(self):
        return 'run'


player1 = PlayerCharacters('john', 21)
player2 = PlayerCharacters('cindy', 19)
player2.attack = 50

print(player1.name, " ", player1.age)
print(player2.name, " ", player2.age)
print(player2.attack)
print(player1.membership)

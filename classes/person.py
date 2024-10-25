class Player():
    def __init__(self, name):
        self.name = name
        self.gold = 0
        self.spins = 0

    def __str__(self):
        return self.name
    

class Player:

    def __init__(self, gold_coins = 0, health_points = 10, lives = 5):
        self.gold_coins = gold_coins
        self.health_points = health_points
        self.lives = lives
    
    def __str__(self):
        return (f'Your gold is {self.gold_coins}, your health is {self.health_points} and your lives are {self.lives}')

    def level_up(self, increase_lives):
        self.lives = self.lives + 1

    def collect_treasure(self):
        self.gold_coins += 1
        if self.gold_coins % 10 == 0:
            self.level_up(1)

    
    def do_battle(self, damage):
        self.health_points -= 1
        if self.health_points < 1:
            self.lives -= 1
            self.health_points = 10
        if self.lives < 1:
            self.reset()

    def reset(self):
       self.gold_coins = 0
       self.health_points = 10
       self.lives = 5

  
            
player1 = Player()
# player1.collect_treasure()
player1.do_battle(5)
print(player1)
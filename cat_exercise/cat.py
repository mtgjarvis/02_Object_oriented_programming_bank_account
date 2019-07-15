class Cat:
    '''
    A class representing 2 Cats
    '''

    def __init__(self, name, preferred_food, meal_time):
        self.name = name
        self.preferred_food = preferred_food
        self.meal_time = meal_time

    def __str__(self):
        print("")

    def eats_at(self, time):
        self.meal_time = time
        return (f'{self.meal_time}')

    def meow(self, discription):
        self.discription = discription
        return (f'My name is {self.name} and I eat {self.preferred_food} at {self.meal_time}')

print(Cat.__doc__)

ruby = Cat('Ruby', 'Chicken in gravey', '5 PM')
print(ruby.meow(''))
nina = Cat('Nina', 'Tuna', '6 PM')
print(nina.meow(''))
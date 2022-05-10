class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
        
# Methods
    def walk(self, pet):
        pet.play()
        return self

    def feed(self, pet):
        if self.pet_food >= 1:
            self.pet_food += -1
            pet.eat()        
        if self.treats >= 1:
            self.treats += -1
            pet.eat()
        if self.pet_food <= 0 and self.treats <= 0:
            return self
        return self
        
    def bathe(self, pet):
        pet.noise()
        return self

class Pet:
    def __init__(self, name, type, tricks, health, energy, sound):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        self.sound = sound

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.health += 10
        self.energy += 5
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        print(self.sound)
        return self

george = Pet("George", "Fire", "Fireball", 40, 30, "shriek")
logan = Ninja("Logan", "Goonie", 2, 2, george)

teken = Pet("Teken", "Earth", "Groundslam", 60, 30, "squawk")
doofus = Ninja("Doofus", "Goonus", 1, 4, teken)

logan.feed(george).bathe(george).walk(george)
george.sleep().eat().play().noise()
print(george.health)
print(logan.treats)
doofus.feed(teken).feed(teken).feed(teken).feed(teken)
print(teken.health)
class Hero:
    def __init__(self, name= None, title= None, health= 100, mana= 100, regeneration_rate= 2):
        self.name = name
        self.title = title
        self.health = health
        self.mana = mana
        self.regeneration_rate = regeneration_rate

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def is_alive(self):
        return self.health > 0

    def can_cast(self):
        return self.mana > 0

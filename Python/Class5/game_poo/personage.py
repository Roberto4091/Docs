from random import randint


class Personage:
    __name = None
    __health = None
    __attack = None

    def __init__(self, name, health, attack):
        self.__name = name
        self.__health = health
        self.__attack = attack

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_attack(self):
        return self.__attack

    def receive_attack(self, attack):
        self.__health -= randint(0, attack)

    def serialize_person(self):
        template = "{name} (health: {health} / attack: {attack})"

        return template.format(
            name=self.__name,
            health=self.__health,
            attack=self.__attack
        )

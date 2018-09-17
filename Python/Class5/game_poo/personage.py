from random import randint


class Personage:
    _name = None
    _health = None
    _attack = None

    def __init__(self, name, health, attack):
        self._name = name
        self._health = health
        self._attack = attack

    def get_name(self):
        return self._name

    def get_health(self):
        return self._health

    def get_attack(self):
        return self._attack

    def receive_attack(self, attack):
        self._health -= randint(0, attack)

    def serialize_person(self):
        template = "{name} (health: {health} / attack: {attack})"

        return template.format(
            name=self._name,
            health=self._health,
            attack=self._attack
        )

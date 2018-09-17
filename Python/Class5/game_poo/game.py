from personage import Personage
from functions import run_game

if __name__ == '__main__':

    print('Personaje 1')
    name1 = input('Ingrese nombre:')
    health1 = int(input('Ingrese vida: '))
    attack1 = int(input('Ingrese ataque: '))

    print('Personaje 2')
    name2 = input('Ingrese nombre:')
    health2 = int(input('Ingrese vida: '))
    attack2 = int(input('Ingrese ataque: '))

    data_p1 = {
        'name': name1,
        'health': health1,
        'attack': attack1
    }

    data_p2 = {
        'name': name2,
        'health': health2,
        'attack': attack2
    }

    p1 = Personage(**data_p1)
    p2 = Personage(**data_p2)

    winner = run_game(p1, p2)

    print('El ganador es {}'.format(winner.get_name()))

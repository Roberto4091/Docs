def run_attack(attacker, enemy):
    cant = attacker.get_attack()
    enemy.receive_attack(cant)


def get_game_title(p1, p2):
    return "{personage1} vs. {personage2})".format(
        personage1=p1.serialize_person(),
        personage2=p2.serialize_person()
    )


def print_game_log(obj_p1, obj_p2):
    print("{p1}: {health1} | {p2}: {health2}".format(
        p1=obj_p1.get_name(), health1=obj_p1.get_health(),
        p2=obj_p2.get_name(), health2=obj_p2.get_health()
    ))


def run_game(obj_p1, obj_p2):
    personages = (obj_p1, obj_p2)

    turno = True
    while obj_p1.get_health() > 0 and obj_p2.get_health() > 0:
        atacante = personages[int(turno)]
        atacado = personages[int(not turno)]

        run_attack(atacante, atacado)
        print_game_log(obj_p1, obj_p2)

        turno = not turno

    return atacante

def get_firts_two_characters(string):
    # 6.1.A
    return string[:2]


def get_last_three_characters(string):
    # 6.1.B
    return string[-3:]


def print_every_two(string):
    # 6.1.C
    return string[::2]


def reverse(string):
    # 6.1.D
    return string[::-1]


def reverse_and_concact(string):
    # 6.1.D
    return string + reverse(string)


def str_insert_character(string, char):
    # 6.2.A
    new_string = ""

    for i in string:
        new_string += i + char

    return new_string[:-1]


def str_delete_spacing(string, replace):
    # 6.2.B
    string = string.replace(" ", replace)
    return string


def str_delete_numbers(string, char):
    # 6.2.C
    for i in "0123456789":
        string = string.replace(i, char)

    return string


def str_insert_character_every_three(string, char):
    # 6.2.D
    count = 0
    str_format = ""
    for i in string:
        if (count == 3):
            str_format += (char + i)
            count = 0
        else:
            str_format += i

        count += 1
    return str_format


def str_delete_spacing_refactor(string, replace, max_replace):
    # 6.3
    string = string.replace(" ", replace, max_replace)
    return string

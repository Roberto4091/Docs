# Ejercicio 3.1


def converterToSeconds(hh, mm, ss):
    seconds = ss
    seconds += mm * 60
    seconds += hh * 3600

    return seconds


def converToHHSS(seconds):
    m = seconds / 60
    s = seconds % 60
    h = m / 60
    m = m % 60
    return h, m, s

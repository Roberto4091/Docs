# Ejercicio 3.2.
from exercise_7 import converterToSeconds, converToHHSS

print("Primer Tiempo")
hh_primary = int(input("Hora: "))
mm_primary = int(input("Minutos: "))
ss_primary = int(input("Segundos: "))

print("Segundo Tiempo")
hh_second = int(input("Hora: "))
mm_second = int(input("Minutos: "))
ss_second = int(input("Segundos: "))

segundos_t1 = converterToSeconds(hh_primary, mm_primary, ss_primary)
segundos_t2 = converterToSeconds(hh_second, mm_second, ss_second)
h, m, s = converToHHSS(segundos_t1 + segundos_t2)

print("Suma: " + str(int(h)) + "hh " + str(int(m)) + "mm " + str(s) + "ss")

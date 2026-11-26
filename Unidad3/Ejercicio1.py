'''
------- Fundamentos de programación ------
  ----- modulo 3                    -----
   ----Ximena González Curcho       ----
'''

''' a) Si la calificación es 9 o más, diga <<Excelente>>
b) Si es menor que 0 o mayor a 10 que diga <<Calificación inválida>>
c) Si la calificación es mayor a 8 pero menor a 9 que diga <<Buen trabajo>>
'''

calificacion = float(input("Calificación:"))

if calificacion >= 11:
    print("Calificación inválida")

elif calificacion < 0:
    print("Calificación inválida")

elif calificacion >=9:
    print("Excelente")

elif calificacion > 8:
    print("Buen trabajo")
else:
    print("Reprobado")
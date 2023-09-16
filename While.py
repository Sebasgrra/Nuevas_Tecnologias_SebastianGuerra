import random

vida = 5
puntos = 0

while vida != 0:
    num = random.randint (0,9)

    if num != 0:
        puntos+=1
        print("You have: ", puntos, "Puntos")
    else: 
        vida -=1
        print("You have: ", vida, "Vidas")
    
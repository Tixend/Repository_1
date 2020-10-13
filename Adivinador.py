import random

print ("Bienvenido al programa, intenta adivinar un numero del 0 al 200, tienes 20 intentos")
numero = random.randrange(0, 200)

for i in range(20):
    adiv = int(input("Ingrese un numero: "))
    if adiv == numero:
        print ("¡Felicitaciones, el numero ingresado es el correcto!, le tomó",i,"intentos")

    elif adiv < numero:
        print ("El numero ingresado es muy bajo")
    else:
        print ("El numero ingresado es muy alto")
import random
numero_secreto = random.randint(1, 100)
intentos = 0 
print("Adivina el numero")
print("Ingresa un número entre 1 y 100")

while True:
    try:
        guess = int(input("Introduce tu número: "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue
    intentos += 1

    if guess < numero_secreto:
        print("El número es más alto. Intenta de nuevo.")
    elif guess > numero_secreto:
        print("El número es más bajo. Intenta de nuevo.")
    else:
        print(f"¡Felicidades! Adivinaste el número {numero_secreto}.")
        print(f"Lo lograste en {intentos} intento(s).")
        break 
    

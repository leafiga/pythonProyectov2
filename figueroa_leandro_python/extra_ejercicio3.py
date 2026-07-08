def imprimir_numeros(texto1, texto2):
    contador = 0

    for numero in range(1, 101):

        if numero % 3 == 0 and numero % 5 == 0:
            print(texto1 + texto2)

        elif numero % 3 == 0:
            print(texto1)

        elif numero % 5 == 0:
            print(texto2)

        else:
            print(numero)
            contador += 1

    return contador


resultado = imprimir_numeros("Python", "Git")
print(f"\nSe imprimieron {resultado} numeros.")
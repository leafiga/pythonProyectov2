# ==========================
# ESTRUCTURA SECUENCIAL
# ==========================

print("\n===== ESTRUCTURA SECUENCIAL =====")

nombre = "Leandro"

print(nombre)
print("Bienvenido a Python!")


# ==========================
# ESTRUCTURA CONDICIONAL (if)
# ==========================

print("\n===== ESTRUCTURA CONDICIONAL (if) =====")

edad = 18

if edad >= 18:
    print("Es mayor de edad")


# ==========================
# ESTRUCTURA CONDICIONAL (if-else)
# ==========================

print("\n===== ESTRUCTURA CONDICIONAL (if-else) =====")

edad = 16

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")


# ==========================
# ESTRUCTURA CONDICIONAL (if-elif-else)
# ==========================

print("\n===== ESTRUCTURA CONDICIONAL (if-elif-else) =====")

nota = 8

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Aprobado")
else:
    print("Insuficiente")


# ==========================
# BUCLE FOR
# ==========================

print("\n===== BUCLE FOR =====")

suma = 0

for numero in range(1, 6):
    suma += numero
    print(f"Se suma {numero}. Total acumulado: {suma}")

print(f"La suma total es: {suma}")


# ==========================
# BUCLE WHILE
# ==========================

print("\n===== BUCLE WHILE =====")

contador = 1

while contador <= 5:
    print(f"Iteración número {contador}")
    contador += 1

print("El contador llegó a su fin.")

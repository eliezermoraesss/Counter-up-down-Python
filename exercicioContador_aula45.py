"""
Exercícios de contadores aula 45
"""

contadorDescrescente = 11
for n in range(0, 9, 1):
    contadorDescrescente -= 1
    print(n, contadorDescrescente)

"""
Resolução do professor
"""
for i, j in enumerate(range(10, 1, -1)):
    print(i, j)

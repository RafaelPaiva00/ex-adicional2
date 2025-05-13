"""
============================================================
          Cálculo das Raízes de uma Equação do 2º Grau
============================================================

Este programa resolve equações do segundo grau na forma:

        ax² + bx + c = 0

O usuário deve fornecer os valores de **a, b e c**, e o programa verificará:

1️⃣ Se **a = 0**, a equação não é do segundo grau e o programa será encerrado.  (.)
2️⃣ Se **Δ < 0**, a equação **não possui raízes reais**.  (.)
3️⃣ Se **Δ = 0**, a equação possui **apenas uma raiz real**. (.) 
4️⃣ Se **Δ > 0**, a equação possui **duas raízes reais**.  (.)

============================================================
"""

valorA = float(input("me de o valor de A aqui:"))
while valorA == 0:
    print ("\n-----a equação não é do segundo grau!-----")
    valorA = float(input("\n tente novamente:"))    

valorB = float(input("me de o valor de B aqui: "))
valorC = float(input("me de o valor de C aqui: "))


delta = (valorB * valorB) - ((4 * valorA) * (valorC))

if delta < 0:
    print ("a equação não possui raízes reais.")

if delta == 0:
    print ("a equação possui apenas uma raiz real.")

if delta == 0:
    print ("a equação possui apenas uma raiz real.")

if delta > 0:
    print ("a equação possui duas raízes reais.")
"""
            ============================================================
          Verificação de Ano Bissexto, Data Válida e Decomposição de Número
            ============================================================

Este programa realiza três funções diferentes:

1️⃣ **Verificar se um ano é bissexto:**
   - O usuário deve fornecer um ano e o programa informará se ele é bissexto.

2️⃣ **Verificar se uma data é válida:**
   - O usuário deve fornecer uma data no formato **dd/mm/aaaa** e o programa verificará se a data é válida.

3️⃣ **Decompor um número inteiro menor que 1000:**
   - O usuário deve fornecer um número e o programa informará quantas centenas, dezenas e unidades ele possui.

============================================================
"""

"""
1️⃣
"""
ano = int(input("Digite um ano e eu lhe falarei se ele é bissexto: "))

if ano % 400 == 0:
    print ("o ano é bissexto!")
elif ano % 100 == 0:
    print ("o ano não é bissexto!")
elif ano % 4 == 0:
    print ("o ano é bissexto!")

else:
    print ("o ano não é bissexto!")



"""
2️⃣
"""


while True:
    data = input("Digite uma data no formato dd/mm/aaaa: ")

    if data.replace("/", "").isdigit() and data.count("/") == 2:
        break  
    else:
        print("Erro! Você não colocou uma data válida. Tente novamente.")

dia, mes, ano = map(int, data.split("/"))

while dia > 31:
    print ("erro, dia invalido")
    dia = int(input("digite outro: "))
while mes > 12:
    print ("erro, mês invalido")
    mes = int(input("digite outro: "))

print (data)

"""
3️⃣
"""

n_1000 = int(input("digite um numero inteiro menor que 1000:"))

while n_1000 > 1000:
    n_1000 = int(input("\nnumero invalido, tente novamente:"))





centena = n_1000 // 100
dezenas = (n_1000 % 100) // 10
unidades = n_1000 % 10

print (f"você tem {centena} centenas, {dezenas} dezenas e {unidades} unidades") 












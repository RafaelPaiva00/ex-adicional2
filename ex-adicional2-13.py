"""
11. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                  Até 5 Kg               Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""

# quantos quilos foi pego
morango_kg = float(input("Digite quantos kg de morango você está levando: "))
maca_kg = float(input("Digite quantos kg de maçã você está levando: "))

#preço por quilo com a quantidade
if morango_kg <= 5:
    preco_morango = 2.50
else:
    preco_morango = 2.20

if maca_kg <= 5:
    preco_maca = 1.80
else:
    preco_maca = 1.50

# Calcular total
total_morango = morango_kg * preco_morango
total_maca = maca_kg * preco_maca
total = total_morango + total_maca

# Aplicar desconto, se necessário
if (morango_kg + maca_kg > 8) or (total > 25):
    total *= 0.90  # desconto de 10%

#valor a pagar
print("------------------------------------------------------")
print(f"Valor a pagar: R$ {total:.2f}")
print("------------------------------------------------------")
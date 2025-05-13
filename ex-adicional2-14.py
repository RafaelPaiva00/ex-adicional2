"""
12. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                  Até 5 Kg               Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente.
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
"""

# Programa da Promoção do Hipermercado Tabajara

print("""
==============================================
      Promoção de Carnes - Hipermercado Tabajara
==============================================
File Duplo   - R$ 4,90/kg até 5kg | R$ 5,80/kg acima de 5kg
Alcatra      - R$ 5,90/kg até 5kg | R$ 6,80/kg acima de 5kg
Picanha      - R$ 6,90/kg até 5kg | R$ 7,80/kg acima de 5kg
""")

# Entrada do tipo de carne e quantidade
tipo = input("Digite o tipo da carne (File Duplo, Alcatra, Picanha): ").strip().lower()
quantidade = float(input("Digite a quantidade de carne (em kg): "))
usou_cartao = input("Pagamento com Cartão Tabajara? (s/n): ").strip().lower() == 's'

# Define o preco por quilo com base no tipo e quantidade
if tipo == "file duplo":
    preco_kg = 4.90 if quantidade <= 5 else 5.80
    nome_carne = "File Duplo"
elif tipo == "alcatra":
    preco_kg = 5.90 if quantidade <= 5 else 6.80
    nome_carne = "Alcatra"
elif tipo == "picanha":
    preco_kg = 6.90 if quantidade <= 5 else 7.80
    nome_carne = "Picanha"
else:
    print("Tipo de carne inválido.")
    exit()

# Calcula valores
preco_total = preco_kg * quantidade
desconto = preco_total * 0.05 if usou_cartao else 0
valor_final = preco_total - desconto

# Exibe o cupom fiscal
print("\
========== CUPOM FISCAL ==========")
print(f"Tipo de carne: {nome_carne}")
print(f"Quantidade: {quantidade:.2f} kg")
print(f"Preço total: R$ {preco_total:.2f}")
print(f"Tipo de pagamento: {'Cartão Tabajara' if usou_cartao else 'Outro'}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor a pagar: R$ {valor_final:.2f}")
print("================================")

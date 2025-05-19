"""
10. Um posto está vendendo combustíveis com a seguinte tabela de descontos:

Álcool:
- até 20 litros, desconto de 3% por litro
- acima de 20 litros, desconto de 5% por litro

Gasolina:
- até 20 litros, desconto de 4% por litro
- acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A- álcool, G- gasolina)

 calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""
print("-----------------------------------------------------")
litros = int(input("digite aqui o quanto de litros foi colocado: "))
print("-----------------------------------------------------")
conbustivel = input("coloque o tipo de conbustivel"
"\n\nA- álcool"
"\nG- gasolina"
"\ndigite aqui: ")

match(conbustivel):
    case "a":
        if litros <= 20:
            pagar_a = litros * (1.90 * 0.03)
            pagar_a_desconto = (litros * 1.90) - pagar_a
            print (f"o valor a pagar é: {pagar_a_desconto}")
        elif litros > 20:
            pagar_a = litros * (1.90 * 0.05)
            pagar_a_desconto = (litros * 1.90) - pagar_a
            print (f"o valor a pagar é: {pagar_a_desconto}")

    case "g":
        if litros <= 20:
            pagar_g = litros * (2.50 * 0.04)
            pagar_g_desconto = (litros * 2.50) - pagar_g
            print (f"o valor a pagar é: {pagar_g}")
        elif litros > 20:
            pagar_g = litros * (2.50 * 0.06)
            pagar_g_desconto = (litros * 2.50) - pagar_g
            print (f"o valor a pagar é: {pagar_g}")


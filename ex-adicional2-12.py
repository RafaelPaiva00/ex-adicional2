print("-----------------------------------------------------")
litros = int(input("digite aqui o quanto de litros foi colocado: "))
print("-----------------------------------------------------")
conbustivel = input("coloque o tipo de conbustivel"
"\n\nA- álcool"
"\nG- gasolina"
"\ndigite aqui: ")

match(conbustivel):
    case "a":
        if litros == 20:
            pagar_a = litros * (1.90 * 0.03)
            pagar_a_desconto = litros * 1.90 - pagar_a
            print (f"o desconto é {pagar_a_desconto}")
        elif litros > 20:
            pagar_a = litros * (1.90 * 0.05)

            print (f"o desconto é {pagar_a}")

    case "g":
        if litros == 20:
            pagar_g = litros * (2.50 * 0.04)

            print (f"o desconto é {pagar_g}")
        elif litros > 20:
            pagar_g = litros * (2.50 * 0.06)

            print (f"o desconto é {pagar_g}")


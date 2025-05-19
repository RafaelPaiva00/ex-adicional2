num = int(input("me de um numero de classe inteiro e eu lhe falerei se e par ou inpar: "))

calculo = num % 2

if calculo > 0:
    print("par")
elif calculo == 0:
    print("inpar")
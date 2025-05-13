while True:

    num1 = float(input("digite um numero aqui: "))
    num2 = float(input("digite um outro numero aqui: "))

    print("escolha uma operação"
    "\n°-----------------------------°" \
    "\n[+]" \
    "\n[-]" \
    "\n[/]" \
    "\n[*]" \
    "\n°-----------------------------°")
    operacao = input("digite aqui: ")

    if operacao not in ["+", "-", "/", "*"]:
        print("Operação inválida. Tente novamente.\n")
        continue

    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "/":
        resultado = num1 / num2
    elif operacao == "*":
        resultado = num1 * num2

    print(f"\nResultado da operação: {resultado}")

    
    if resultado % 2 == 0:
        print("É um número par.")
    else:
        print("É um número ímpar.")


    if resultado > 0:
        print("É um número positivo.")
    elif resultado < 0:
        print("É um número negativo.")
    else:
        print("O resultado é zero.")


    if resultado == int(resultado):
        print("É um número inteiro.")
    else:
        print("É um número decimal.")

    print("\n-----------------------------------\n")

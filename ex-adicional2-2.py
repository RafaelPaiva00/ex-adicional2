"""
===========================================
       CALCULADORA DE MÉDIA ESCOLAR
===========================================

Este programa lê as duas notas parciais obtidas por um aluno 
ao longo do semestre e calcula sua média.

A atribuição de conceitos segue a tabela abaixo:

  Média de Aproveitamento  |  Conceito
  -------------------------|-----------
  Entre 9.0 e 10.0        |     A
  Entre 7.5 e 9.0         |     B
  Entre 6.0 e 7.5         |     C
  Entre 4.0 e 6.0         |     D
  Entre 0.0 e 4.0         |     E

O algoritmo deve mostrar na tela:
. As notas inseridas +
. A média calculada +
. O conceito correspondente 
. A mensagem "APROVADO" se o conceito for A, B ou C
. A mensagem "REPROVADO" se o conceito for D ou E

===========================================

"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if 9.0 <= media <= 10.0:
    conceito = "A"
elif 7.5 <= media < 9.0:
    conceito = "B"
elif 6.0 <= media < 7.5:
    conceito = "C"
elif 4.0 <= media < 6.0:
    conceito = "D"
else:
    conceito = "E"

if conceito in ["A", "B", "C"]:
    status = "APROVADO!"
else:
    status = "REPROVADO!"

print("\n=========== RESULTADO ===========")
print(f"Nota 1: {nota1:.1f}")
print(f"Nota 2: {nota2:.1f}")
print(f"Média: {media:.1f}")
print(f"Conceito: {conceito}")
print(f"Situação: {status}")
print("=================================")
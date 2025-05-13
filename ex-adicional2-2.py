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


nota1 = float(input("digite a sua primeira nota aqui: "))
nota2 = float(input("digite a sua segunda nota aqui: "))

media = (nota1 + nota2) / 2


print((f"\n nota 1: {nota1:}\n nota 2: {nota2:}"))

print((f"\n media: {media}"))

conceitos = [
    (9.0, 10.0, "A"),
    (7.5, 9.0, "B"),
    (6.0, 7.5, "C"),
    (4.0, 6.0, "D"),
    (0.0, 4.0, "E")
]

conceito = conceitos[media]

print(conceito)


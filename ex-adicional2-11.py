"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

- "Telefonou para a vítima?" 1 "Inocente"
- "Esteve no local do crime?" 2 "Suspeita"
- "Mora perto da vítima?" 3 "Cúmplice"
- "Devia para a vítima?" 4 "Cúmplice"
- "Já trabalhou com a vítima?" 5 "Assassino"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""
#perguntas sobre o crime

print("------------------------------------------------"
"\n  oque ouve na 22situação?"
"\n\n- Telefonou para a vítima [1]"
"\n- Esteve no local do crime [2]"
"\n- Mora perto da vítima [3]"
"\n- Devia para a vítima  [4]"
"\n- Já trabalhou com a vítima [5]"
"\n------------------------------------------------")
pergunta = int(input("digite aqui: "))

#classificação da pessoa
match pergunta:
    case 1:
        print("------------------------------------------------"
              "\nInocente")
    case 2:
        print("------------------------------------------------"
            "\nSuspeita")
    case 3:
        print("------------------------------------------------"
            "\nCúmplice")
    case 4:
        print("------------------------------------------------"
            "\nCúmplice")
    case 5:
        print("------------------------------------------------"
              "\nAssassino")

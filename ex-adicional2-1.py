#pegando informações do usuario
n_dia_semana = int(input("Digite um número entre um e sete, e eu lhe mostrarei qual é o dia da semana correspondente.\n"))

#mostrando se der errado
while n_dia_semana > 7 or n_dia_semana == 0:
    print ("número invalido!")
    n_dia_semana = int(input("Tente novamente: "))

#criando a estrutura da conta de dias com N
lista_semana = ["false", "domingo", "segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado"]

if n_dia_semana > 0:
    print (f"{n_dia_semana}.{lista_semana[n_dia_semana]}")
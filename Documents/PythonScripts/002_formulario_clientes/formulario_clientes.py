#Essas primeiras linhas são apenas um título, com cores invertidas
print('=====================================')
print('\033[1:7m FORMULÁRIO DE SATISFAÇÃO DO CLIENTE\033[m')
print('===================================== \n')

#=============== Variáveis que ficam obrigando o usuário inserir algum valor ===============
nome = input('Digite seu Nome: ').upper()
while nome == '':
    nome = input('\033[1:31m*** \033[mPor favor, digite seu Nome: ').upper()

resposta = input(nome+' em uma escala de 0 a 10, qual seu nível de satisfação? ')
while resposta == '':
    resposta = input('\033[1:31m*** \033[m'+nome+' em uma escala de 0 a 10, qual seu nível de satisfação?')
#==========================================================================================================



if float(resposta) >10 or float(resposta) <0:
    print('\033[1:97:41m *** RESPOSTA INVÁLIDA!!! ***\033[m') #FUNDO VERMELHO, LETRA BRANCA

elif float(resposta) >=0 and float(resposta) <= 3:
    print('\033[1:31m *** VOCÊ ESCOLHEU: PÉSSIMO ATENDIMENTO *** \033[m')
    print('Digite 1) SIM \nDigite 2) NÃO')
    avaliacao = input('Deseja acrescentar alguma observação nesse atendimento? \n  ')

    if avaliacao == '2':
        print('Obrigado pela resposta do nível de atendimento, tenha um ótimo dia')
    elif avaliacao == '1':
        observacao = input('Digite aqui sua observação: ')
        print('\033[1mMensagem enviada com sucesso. \n Obrigado pela sua avaliação!!! \033[m')
    else:
        print('\033[1:97:41mOpção Inválida!!!\033[m Obrigado pela sua avaliação, caso queira nos avaliar, acesse nosso site')


elif float(resposta) >=4 and float(resposta) <=6:
    print('\033[1:33m *** VOCÊ ESCOLHEU: ATENDIMENTO REGULAR ***\033[m')
    print('Digite 1) SIM \nDigite 2) NÃO')
    avaliacao = input('Deseja acrescentar alguma observação nesse atendimento? \n  ')

    if avaliacao == '2':
        print('Obrigado pela resposta do nível de atendimento, tenha um ótimo dia')
    elif avaliacao == '1':
        observacao = input('Digite aqui sua observação: ')
        print('\033[1mMensagem enviada com sucesso. \n Obrigado pela sua avaliação!!! \033[m')
    else:
        print(
            '\033[1:97:41mOpção Inválida!!!\033[m Obrigado pela sua avaliação, caso queira nos avaliar, acesse nosso site')


elif float(resposta) >=7 and float(resposta) <=9 :

    print('\033[1:34m *** VOCÊ ESCOLHEU: BOM ATENDIMENTO ***\033[m')
    print('Digite (1) - SIM \nDigite (2) - NÃO')
    avaliacao = input('Deseja acrescentar alguma observação nesse atendimento? \n  ')

    if avaliacao == '2':
        print('Obrigado pela resposta do nível de atendimento, tenha um ótimo dia')
    elif avaliacao == '1':
        observacao = input('Digite aqui sua observação: ')
        print('\033[1mMensagem enviada com sucesso. \n Obrigado pela sua avaliação!!! \033[m')
    else:
        print(
            '\033[1:97:41mOpção Inválida!!!\033[m Obrigado pela sua avaliação, caso queira nos avaliar, acesse nosso site')

else:
    print('\033[1:32m*** VOCÊ ESCOLHEU: ÓTIMO ATENDIMENTO!!!!! ***\033[m')
    print('Digite (1) - SIM \nDigite (2) - NÃO')
    avaliacao = input('Deseja acrescentar alguma observação nesse atendimento? \n  ')

    if avaliacao == '2':
        print('\033[1:97:43mObrigado pela resposta do nível de atendimento, tenha um ótimo dia\033[m')
    elif avaliacao == '1':
        observacao = input('Digite aqui sua observação: ')
        print('\033[1mMensagem enviada com sucesso. \n Obrigado pela sua avaliação!!! \033[m')
    else:
        print('\033[1:97:41mOpção Inválida!!!\033[m Obrigado pela sua avaliação, caso queira nos avaliar, acesse nosso site')

##################################################################
#  SENAC/RESILIA - Formação em Análise de Dados (FAD)            #
#  Projeto em Grupo - Módulo 1 - Fale Comigo!                    #
#  !/usr/bin/env python3                                         #
#  -*- coding: utf-8 -*-                                         #
#  Criado por: Diego de Arruda Nieto, Douglas Klem Portugal      #
#  do Amaral, Emanoel Cascaes Gomes, Matheus Barbosa Furtado     #
#  e Yasmin Belo da Silva                                        #
#  Data de criação: 12/01/2023                                   #
#  versão = '3.11'                                               #
##################################################################
#
# Atividade:
#
# Sua equipe foi chamada para criar um projeto que vai ajudar com atendimentos automatizados
# de dúvidas sobre a empresa e no futuro vai coletar informações para auxiliar na tomada de decisão.
# Desenvolvemos um código que lista opções de atendimento e o usuário é guiado por mensagens
# avançando dentro desse atendimento simulado até que chegue ao final obtendo a resposta desejada.
#
# Escolhemos uma empresa no ramo de atuação com coleta labotatorial e clínica diagnóstica, como
# mostrado a seguir:
#
print('#'*100)
print('Bem-vindo ao chatbot da Clínica FAD! Aqui você encontra informações rápidas sobre nossos serviços.')
print('#'*100)


def questionarioinicio():
    print('''Digite uma das opções abaixo:
1 EXAMES E RESULTADOS
2 AGENDAMENTOS E CONSULTAS
3 ORÇAMENTOS
4 FALAR COM UM DE NOSSOS ATENDENTES
5 SAIR''')


def questionario2():
    print('''
1 BAIXAR EXAME
2 IMPRIMIR EXAME
3 ENCAMINHAR EXAME PARA SEU MÉDICO
4 EXCLUIR EXAME''')


def questionario3():
    print('''
1 VOLTAR AO INÍCIO
2 SAIR''')


def quesconsultas1():
    print('''
1 VER CONSULTAS AGENDADAS
2 CANCELAR UMA CONSULTA
3 REMARCAR UMA CONSULTA''')


def quesconsultas2():
    print('''
1 CONSULTAR PREÇOS DISPONÍVEIS
2 ADICIONAR UM ORÇAMENTO SIMULADO
3 REMOVER UM ORÇAMENTO SIMULADO''')


def quesconsultas3():
    print('''
1 TELEFONES  
2 REDES SOCIAIS
3 ENCAMINHAMENTO INTERNO''')


def questionarioconsultas2():
    print('''
    1 - ''')


def separador():
    print('*'*30)


inicio = ''

while inicio != '5':
    questionarioinicio()
    separador()
    inicio = input('Qual é a opção desejada? ')
    separador()
    if inicio == '1':
        questionario2()
        separador()
        questio2 = input('Qual é a opção desejada para exames? ')
        separador()
        if questio2 == '1':
            print('Clique AQUI para baixar seu exame.')
            questionario3()
            quest3 = input('Qual é a opção desejada? ')
            if quest3 == '1':
                pass
            elif quest3 == '2':
                print('Saindo...')
                print('Obrigado por escolher a Clínica FAD! Volte sempre!')
                print('#'*100)
                break
        if questio2 == '2':
            print('Clique AQUI para imprimir seu exame.')

            questionario3()
            quest3 = input('Qual é a opção desejada?')
            if quest3 == '1':
                pass
            elif quest3 == '2':
                print('Saindo.')
                print('Obrigado por escolher a Clínica FAD! Volte sempre!')
                print('#'*100)
                break
            separador()
        if questio2 == '3':
            print('Clique AQUI para encaminhar seu exame.')

            questionario3()
            quest3 = input('Qual é a opção desejada?')
            if quest3 == '1':
                pass
            elif quest3 == '2':
                print('Saindo.')
                print('Obrigado por escolher a Clínica FAD! Volte sempre!')
                print('#'*100)
                break
            separador()
        if questio2 == '4':
            print('Clique AQUI para excluir seu exame.')

            questionario3()
            quest3 = input('Qual é a opção desejada?')
            if quest3 == '1':
                pass
            elif quest3 == '2':
                print('Saindo.')
                print('Obrigado por escolher a Clínica FAD! Volte sempre!')
                print('#'*100)
                break
            separador()
    elif inicio == '2':
        quesconsultas1()
        separador()
        questio1 = input('Qual é a opção desejada?')
        separador()
        if questio1 == '1':
            print('Clique AQUI para ver suas consultas agendadas.')
            questionario3()
            quest3 = input('Qual é a opção desejada?')
            if quest3 == '1':
                pass
            elif quest3 == '2':
                print("Saindo.")
                print('Obrigado por escolher a Clínica FAD! Volte sempre!')
                print('#'*100)
                break

        elif questio1 == '2':
            print('Clique AQUI para cancelar sua consulta.')
            questionario3()
            quest3 = input('Qual é a opção desejada?')
            if quest3 == '1':
                pass
            elif quest3 == '2':
                print('Saindo.')
                print('Obrigado por escolher a Clínica FAD! Volte sempre!')
                print('#'*100)
                break
        elif questio1 == '3':
            print('Clique AQUI para remarcar uma consulta previamente agendada.')
            questionario3()
            quest3 = input('Qual é a opção desejada?')
            if quest3 == '1':
                pass
            elif quest3 == '2':
                print('Saindo.')
                print('Obrigado por escolher a Clínica FAD! Volte sempre!')
                print('#'*100)
                break
    elif inicio == '3':
        quesconsultas2()
        separador()
        questio1 = input('Qual é a opção desejada?')
        separador()
        if questio1 == '1':
            print(
                'Clique AQUI para ver os preços de acordo com a tabela de exames atual.')
            questionario3()
            quest3 = input('Qual é a opção desejada?')
            if quest3 == '1':
                pass
            elif quest3 == '2':
                print("Saindo.")
                print('Obrigado por escolher a Clínica FAD! Volte sempre!')
                print('#'*100)
                break

        elif questio1 == '2':
            print('Clique AQUI para adicionar uma simulação de orçamento.')
            questionario3()
            quest3 = input('Qual é a opção desejada?')
            if quest3 == '1':
                pass
            elif quest3 == '2':
                print('Saindo.')
                print('Obrigado por escolher a Clínica FAD! Volte sempre!')
                print('#'*100)
                break
        elif questio1 == '3':
            print('Clique AQUI para remover uma simulação de orçamento.')
            questionario3()
            quest3 = input('Qual é a opção desejada?')
            if quest3 == '1':
                pass
            elif quest3 == '2':
                print('Saindo.')
                print('Obrigado por escolher a Clínica FAD! Volte sempre!')
                print('#'*100)
                break
    elif inicio == '4':
        quesconsultas3()
        separador()
        questio1 = input('Qual é a opção desejada?')
        separador()
        if questio1 == '1':
            print(
                'Clique AQUI para acessar os telefones disponíveis.')
            questionario3()
            quest3 = input('Qual é a opção desejada?')
            if quest3 == '1':
                pass
            elif quest3 == '2':
                print("Saindo.")
                print('Obrigado por escolher a Clínica FAD! Volte sempre!')
                print('#'*100)
                break

        elif questio1 == '2':
            print('Clique AQUI para acessar nossas redes sociais.')
            questionario3()
            quest3 = input('Qual é a opção desejada?')
            if quest3 == '1':
                pass
            elif quest3 == '2':
                print('Saindo.')
                print('Obrigado por escolher a Clínica FAD! Volte sempre!')
                print('#'*100)
                break
        elif questio1 == '3':
            print('Não encontrou meios de nos contactar? Deixe uma mensagem com suas informações que retornaremos o mais breve possível:')
            questionario3()
            quest3 = input('Qual é a opção desejada?')
            if quest3 == '1':
                pass
            elif quest3 == '2':
                print('Saindo.')
                print('Obrigado por escolher a Clínica FAD! Volte sempre!')
                print('#'*100)
                break
else:
    print('Obrigado por escolher a Clínica FAD! Volte sempre!')
    print('#'*100)
#
# Referências (último acesso em 15/01/2023):
# https://sergiofranco.com.br/
# https://www.dremerson.com.br/
#

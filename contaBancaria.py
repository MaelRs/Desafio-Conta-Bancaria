from time import sleep

def linha():
    print('='*50)

def cabeçalho():
    linha()
    print('Bem vindo ao Banco Ismael!'.center(50))
    linha()

numero_de_saques=0
limite_de_saques=3
valor_total_saques=0
valor_total_depositos=0
extrato=''
saldo=0
limite=500
while True:
    cabeçalho()
    menu=int(input('''MENU PRINCIPAL
    \n[1]-Depósito
    \n[2]-Saque
    \n[3]-Extrato
    \n[4]-Saldo
    \n[5]-Sair
    \nDigite a operação desejada:'''))

    if menu==1:
        valor_deposito=float(input('Digite o valor a ser depositado: '))
        if valor_deposito<=0:
            print('\033[1;30;41m Valor Inválido! INFORME UM VALOR VÁLIDO! \033[m')
        else:
            valor_total_depositos+=valor_deposito
            saldo+=valor_deposito
            extrato+=(f'Depósito: R$ {valor_deposito}\n')
            print(f'\033[1;31;42m Deposito de R${valor_deposito:.2f} efetuado com sucesso! \033[m')
            print(f'Seu saldo atual é:R${saldo:.2f}')
        sleep(2)
        
    elif menu==2:        
        valor_saque=float(input('Digite o valor desejado: '))
        if valor_saque>saldo:
            print('\033[1;30;41m Operação falhou!Valor informado excede o saldo disponível para saque.\033[m')
        elif valor_saque<=0:
            print('\033[1;30;41m Valor Inválido! INFORME UM VALOR VÁLIDO! \033[m')
        elif valor_saque>limite:
            print('\033[1;30;41m Operação falhou!Valor informado excede o limite para saque.\033[m')
        elif numero_de_saques>=limite_de_saques:
            print('\033[1;30;41m Operação falhou!Você excedou o número diário para saques.')
        else:
            print(f'\033[1;31;42m Saque de R${valor_saque:.2f} efetuado com sucesso! \033[m')
            numero_de_saques+=1
            saldo-=valor_saque
            valor_total_saques+=valor_saque
            extrato+= f'Saque:R$ {valor_saque:.2f}\n'
        
        sleep(2)
    elif menu==3:
        linha()
        print('Extrato de Conta Bancária'.center(50))
        linha()
        print(f'''\n{extrato}
              \nValor total de Depósitos:R${valor_total_depositos:.2f}
              \nValor total de saques:R${valor_total_saques:.2f}
              \nSaldo Disponível: R${saldo:.2f}''')
        sleep(2)
    elif menu==4:
        linha()
        print(f'Seu saldo atual é: R${saldo:.2f}')
        linha()
        sleep(2)
    elif menu==5:
        linha()
        print('\033[1;31;42m Obrigado por usar os serviços do Banco Ismael!\n Até a próxima.\033[m')
        linha()
        break
    else:
        print('\033[1;30;41m Opção inválida! Tente novamente.\033[m')
        


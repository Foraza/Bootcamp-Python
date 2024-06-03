MENU = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=>"""

WITHDRAW_LIMIT = 3
MAX_WITHDRAW_VALUE = 500
balance = 0
extract = ''
withdrawCount = 0

while True:

    opt = input(MENU)
    
    if(opt == 'd'):
        value = float(input('\nInforme o valor a ser depositado: '))
        
        if value > 0:
            balance += value
            extract += f"Depósito: R$ {value:.2f}\n"
            
            print('\n-------------Depósito realizado com sucesso!-----------\n\n')
        
        else:
            print('\nPor favor, informe um valor maior que zero para ser depositado!')
        
    elif(opt == 's'):
        value = float(input('\nInforme o valor a ser sacado: '))
        
        if value > balance:
            print('\nSaldo insuficiente para realizar a operação!')
            
        elif value > MAX_WITHDRAW_VALUE:
            print(f'\nO limite máximo por saque é R$ {MAX_WITHDRAW_VALUE:.2f}')
            
        elif withdrawCount > WITHDRAW_LIMIT:
            print(f'\nVocê só pode realizar {WITHDRAW_LIMIT} saques por dia!')
        
        else: 
            balance -= value
            extract += f'Saque: R$ {value:.2f}\n'
            withdrawCount += 1
        
    elif(opt == 'e'):
        print('\n================ EXTRATO ================')
        print('Não foram realizadas movimentações.' if not extract else extract)
        print(f'\nSaldo: R$ {balance:.2f}')
        print('==========================================')
        
    elif(opt == 'q'):
        break
    
    else:
        print('Por favor, selecione uma opção válida!')
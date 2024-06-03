WITHDRAW_LIMIT = 3
MAX_WITHDRAW_VALUE = 500
users = {}
accounts = []

def showMenu():
    MENU = """

        [d] Depositar
        [s] Sacar
        [e] Extrato
        [u] Cadastrar Usuário
        [c] Cadastrar Conta
        [q] Sair

    =>"""
    
    return input(MENU)

def deposit(balance, value, extract, /):
    if value > 0:
        balance += value
        extract += f"Depósito: R$ {value:.2f}\n"
        
        print('\n-------------Depósito realizado com sucesso!-----------\n\n')
    
    else:
        print('\nPor favor, informe um valor maior que zero para ser depositado!')
    
    return balance, extract

def withdraw(*, balance, value, extract, withdrawCount):
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
    
    return balance, extract

def showExtract(balance, /, *, extract):
    print('\n================ EXTRATO ================')
    print('Não foram realizadas movimentações.' if not extract else extract)
    print(f'\nSaldo: R$ {balance:.2f}')
    print('==========================================')
    
def createUser():
    name = input('Informe o nome do usuário:')
    cpf = int(input('Informe o cpf do usuário:'))
    birthday = input('Informe a data de nascimento do usuário:')
    address = input('Informe o endereço do usuário:')
    
    user = {
        'name': name,
        'cpf': cpf,
        'birthday': birthday,
        'addess': address
    }
    
    users.update({cpf: user})
    
    print(f'Usuário criado:\n{user}')
    
    return user

def createAccount():
    cpf = int(input('Informe o CPF do titular da conta:'))
    
    if users.get(cpf):
        
        account = {
            'accNum': 1 if len(accounts) == 0 else accounts[-1]['accNum'] + 1,
            'agency': '0001',
            'user': cpf
        }
        
        accounts.append(account)
        
        print(f'Conta criada:\n{account}')
        
        return account
    else:
        print('Usuário não cadastrado!')

def main():
    balance = 0
    extract = ''
    withdrawCount = 0
    
    while True:

        opt = showMenu()
        
        if(opt == 'd'):
            value = float(input('\nInforme o valor a ser depositado: '))
            
            balance, extract = deposit(balance, value, extract)
            
        elif(opt == 's'):
            value = float(input('\nInforme o valor a ser sacado: '))
            
            balance, extract = withdraw(balance=balance, value=value, extract=extract, withdrawCount=withdrawCount)
            
        elif(opt == 'e'):
            showExtract(balance, extract=extract)
            
        elif(opt == 'u'):
            createUser()
            
        elif(opt == 'c'):
            createAccount()
            
        elif(opt == 'q'):
            break
        
        else:
            print('Por favor, selecione uma opção válida!')
            
main()
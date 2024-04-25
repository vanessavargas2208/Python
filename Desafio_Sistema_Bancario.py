menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("Informe o valor de depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: RS {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")    
        
    elif opcao == "2":
        valor = float(input("Informe valor de saque: "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite 
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Você não possui saldo suficiente.")
            
        elif excedeu_limite:
            print("Operação fallhou! O valor de  saque excede o limite.")
            
        elif excedeu_saques:
            print("Operação falhou! Número de saques excedido.")   
            
        elif valor > 0:
            saldo -= valor
            extrato += valor
            numero_saques += 1
        else:
            print("Operação falhou! Valor informado é inválido.")             
        
    elif opcao == "3":
        print("\n******** EXTRATO ********")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("*************************")
 
        
    elif opcao == "0":
       break
   
else:
       print("Operação inválida, por favor selecione novamente a operação desejada.")         


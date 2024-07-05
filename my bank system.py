Deposito = 1000
saque = 0
extrato = 0


MENU= """
        ========== MENU ==========
    
        Depositar [1]
        Sacar [2]
        Extrato [3]
        Sair [4]
      
        ==========================
      
      """



while True:
    opc = input(MENU)

    if opc == "1":
        dep= float(input("digite um valor para se depositado: "))
        if dep > 0:
            extrato += dep
            print(extrato)
        else:
            print("Valor inválido.")
        
    elif opc == "2":
        sacando = float(input("digite saque: "))
        if sacando > 0:
            extrato -=sacando
            Deposito -= sacando
            saque += 1
            print(Deposito)

        elif saque == 3:
            print("operação bloqueada")
            break

        else:
            print("Valor inválido.")
            
    elif opc == "3":
        print(extrato)
        break

    elif opc == "4":
        print("Obrigado por usar nossos serviços.")
        break
    else:
        print("número não considerado.")
    
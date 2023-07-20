saldo= float()
valorDeSaque = float()
saca =(saldo - valorDeSaque)
valorDeDeposito =float()
deposita =(saldo + valorDeDeposito)
extrato= ("")
opcao= str("")
limiteDeSaque = 0
contadorDeposito = 0
contadorSaque = 0
while True:

    print("""             -------------------------------------------
            |                   Olá                     |
            |            seja bem vindo ao              |  
            |                  IGBANK                   |
             -------------------------------------------
      """                              )

    opcao = (input ("""Escolha qual serviço deseja realizar
             [1] VER EXTRATO 
             [2] DEPOSITAR
             [3] SACAR
             [4] SAIR
             
             """))
    if opcao == "1":
        print ("========== EXTRATO ==========")
        
        print ("você realizou ", contadorDeposito, "depósitos e", contadorSaque, "saques no período")
        print()
        print(extrato)
        print()
        print(f"Seu saldo é R$ {saldo:.2f}")
        print ("=========== IGBANK ===========")
        print()
        print()
        
        
    elif opcao == "2":
        valorDeDeposito = float(input("\nINFORME O VALOR QUE DESEJA DEPOSITAR  "))
        if valorDeDeposito > 0:
            saldo = valorDeDeposito + saldo
            contadorDeposito = contadorDeposito +1
            extrato += f"\n Depósito R$ {valorDeDeposito:.2f}"
            print()
            
        else:
            print("Valor de depósito inválido")
    elif opcao == "3":
        if limiteDeSaque  < 3: 
            valorDeSaque = float(input("\nINFORME O VALOR QUE DESEJA SACAR  "))
            if valorDeSaque <= 500.00:
                    if valorDeSaque <= saldo:
                        saldo = saldo - valorDeSaque
                        limiteDeSaque = int(limiteDeSaque + 1)
                        contadorSaque = contadorSaque +1
                        extrato += f"\n Saque R$ {valorDeSaque:.2f}"
                    else:
                        print("SALDO INSUFICIENTE")
            else:
                print ("Operação não permitida excede valor limite.")
                print("Limite de saque diário restantes ",3 -limiteDeSaque)
                print()
        else:
            print("Você excedeu o limite de saque diário!")
            print("Limite de saque diário restantes ",limiteDeSaque-3)
            print()
            break
    elif opcao == "4":
        print("Até logo!")
        break
    else:
        print("informe uma opção válida!!!")
        print()

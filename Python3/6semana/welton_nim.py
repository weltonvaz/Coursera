def partida():
    
    print(" ")
    
    # Solicita ao usuário os valores de n e m:
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    
    # Define uma variável para controlar a vez do computador:
    is_computer_turn = True
    
    # Decide quem iniciará o jogo:
    if n % (m+1) == 0:
        is_computer_turn = False
        
    # Execute enquanto houver peças no jogo:
    while n > 0:
        
        if is_computer_turn:
            # Vez do usuário:
            print ("\nComputador começa!\n")
            jogada = computador_escolhe_jogada(n, m)
            is_computer_turn = False
            if jogada == 1:
                print("O computador tirou uma peça.")
            else:
                print("Computador retirou {} peças.".format(jogada))
        else:
            # Vez do usuário:
            print ("\nVoce começa!\n")
            jogada = usuario_escolhe_jogada(n, m)
            is_computer_turn = True
            print("Você retirou {} peças.".format(jogada))
            
        # Retira as peças do jogo:
        n = n - jogada
        
        # Mostra o estado atual do jogo:
        print("Restam apenas {} peças em jogo.\n".format(n))
        
    # Fim de jogo, verifica quem ganhou:
    if is_computer_turn:
        print("Fim do jogo! Você ganhou!")
        return 1
    else:
        print("Fim do jogo! O computador ganhou!")
        return 0

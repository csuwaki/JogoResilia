def primeira_escolha():
    primeira_escolha = int(input("Isso! É sua chance de fazer um batom neon incrível! Quando você começa a se aproximar da poça radioativa, você vê a onça Carol com C matando sua sede \n\
calmamente. Ela parece amigável. Próximo a ela, você enxerga um martelo. O que você faz? \n\
    1. Ela não parece perigosa, calmamente você caminha até a poça para coletar a água. \n\
    2. Que medo! Melhor coletar o chinelo e explorar a pilha de ossos. \n "))
    return primeira_escolha

def segunda_escolha():
    segunda_escolha = int(input("Que lugar incrível! Uma pilha de ossos imensa e um chinelo! Você observa a Zumbi Quim Cardaxa fazendo tutoriais para o Zombietube. Você se aproxima, ela diz: \n\
    - Olá, forasteira! Você vai adorar essa sombra triturada de ossos que estou usando! Você pode fazer uma igual, se quiser. \n\
O que você faz? \n\
    1. Triturar os ossos. \n\
    2. Hmmm, não fui com a cara da Quim, melhor coletar o chinelo e ir explorar a pilha de animais mortos. \n "))
    return segunda_escolha

def quarta_escolha():
    quarta_escolha = int(input("Você chegou à pilha de animais mortos e avista a diva Bion-C com um lindo casaco de peles e uma garrafa. Ao se aproximar, ela diz: \n\
    '- Olá, forasteira! Aqui nessa pilha de animais há maravilhosas peles de raposa em decomposição. Mas cuidado! As baratas decompositoras podem te atacar. \n\
    Você decide então...: \n\
    1. Coletar o casaco. \n\
    2. Guardar a garrafa e explorar a Poça Radioativa. \n "))
    return quarta_escolha

def perdeu():
    print("Escolha terrível! Não soube procurar ou não soube aproveitar as ferramentas. No que você estava pensando? Você perdeu! ")
    perdeu = input("Deseja jogar novamente? Responda sim ou não. ")
    if perdeu.title() == "Sim":
        programa_principal()
    else:
        print("Fim de jogo!")
    return perdeu

def escolha_invalida():
    perdeu = input("Escolha inválida! Deseja jogar novamente? Responda sim ou não. ")
    if perdeu.title() == "Sim":
        programa_principal()
    else:
        print("Fim de jogo!")

def venceu_casaco():
    print("Buonasera Gatuxa! Você fez um lindo casaco de peles e vai mostrar sua beleza radiante por aí! Parabéns! Você venceu!")

def venceu_batom():
    print("Buonasera Gatuxa! Você fez um lindo batom neon e vai mostrar sua beleza radiante por aí! Parabéns! Você venceu!")

def venceu_base():
    print("Buonasera Gatuxa! Você fez uma linda base com os ossos e vai mostrar sua beleza radiante por aí! Parabéns! Você venceu!")

def programa_principal():
    print("Você sobreviveu a um apocalipse nuclear e agora precisa lutar pela sobrevivência no mundo pós-apocalíptico. Mas antes, prioridades. \n\
Você percebeu que não tem nenhum item de beleza na sua bolsa Golce & Dabanna para encarar esse mundo cruel e deseja encontrá-los \n\
para arrasar na balada Plutônio Night Club. \n\
Atenção! Para coletar os itens encontrados você precisa de ferramentas que podem estar em outros locais, então procure bem. Boa sorte! \n\
Bem-vindo (a), sobrevivente!")

    nome = input("Como posso te chamar? ")
    print(f"Olá, {nome.title()}.")

    local = input(f"Você decidiu sair do seu bunker para explorar a região. À sua direita há uma 1. poça radioativa; à esquerda, uma 2. pilha de ossos; e à frente uma 3. pilha de animais mortos. \n\
Para onde você deseja ir? ")

    if local.title() == 'Poça Radioativa' or local.title() == '1': 
        pri_e = primeira_escolha() 
        if pri_e == 1:
            perdeu()
        elif pri_e == 2:
            seg_e = segunda_escolha()
            if seg_e == 1:
                venceu_base()
            elif seg_e == 2:
                terceira_escolha = int(input("Você chegou à pilha de animais mortos e avista a diva Bion-C com um lindo casaco de peles. Ao se aproximar, ela diz: \n\
    - Olá, forasteira! Aqui nessa pilha de animais há maravilhosas peles de raposa em decomposição. Mas cuidado! As baratas decompositoras podem te atacar. \n\
    Você decide então...: \n\
    1. Usar o chinelo para matar as baratas. \n\
    2. Desiste, afinal nada chegou aos pés do seu glamour. \n "))
                if terceira_escolha == 1:
                    venceu_casaco()
                elif terceira_escolha == 2:
                    perdeu()
                else:
                    escolha_invalida()
            else:   
                escolha_invalida()
        else:
            escolha_invalida()

    elif local.title() == 'Pilha De Ossos' or local.title() == '2':
        seg_e = segunda_escolha()
        if seg_e == 1:
            perdeu()
        elif seg_e == 2:
            qua_e = quarta_escolha()
            if qua_e == 1:
                venceu_casaco()
            elif qua_e == 2:
                quinta_escolha = int(input("Isso! É sua chance de fazer um batom neon incrível! Quando você começa a se aproximar da poça radioativa, você vê a onça Carol com C matando sua sede \n\
calmamente. Ela parece amigável. Próximo a ela, você enxerga um martelo. O que você faz? \n\
    1. Ela não parece perigosa, calmamente você caminha até a poça para coletar a água. \n\
    2. Desiste, afinal nada chegou aos pés do seu glamour. \n "))
                if quinta_escolha == 1:
                    venceu_batom()
                elif quinta_escolha == 2:
                    perdeu()
                else:   
                    escolha_invalida()
            else:   
                escolha_invalida()
        else:   
            escolha_invalida()


    elif local.title() == 'Pilha De Animais Mortos' or local.title() == '3':
        qua_e  = quarta_escolha()
        if qua_e == 1:
            perdeu()
        elif qua_e == 2:
            sexta_escolha = int(input("Isso! É sua chance de fazer um batom neon incrível! Quando você começa a se aproximar da poça radioativa, você vê a onça Carol com C matando sua sede \n\
calmamente. Ela parece amigável. Próximo a ela, você enxerga um martelo. O que você faz? \n\
    1. Ela não parece perigosa, calmamente você caminha até a poça para coletar a água. \n\
    2. Que medo! Melhor coletar o chinelo e explorar a pilha de ossos. \n "))
            if sexta_escolha == 1:
                venceu_batom()
            elif sexta_escolha == 2:
                setima_escolha =  int(input("Que lugar incrível! Uma pilha de ossos imensa e um chinelo! Você observa a Zumbi Quim Cardaxa fazendo tutoriais para o Zombietube. Você se aproxima, ela diz: \n\
    - Olá, forasteira! Você vai adorar essa sombra triturada de ossos que estou usando! Você pode fazer uma igual, se quiser. \n\
O que você faz? \n\
    1. Triturar os ossos. \n\
    2. Desiste, afinal nada chegou aos pés do seu glamour. \n "))
                if setima_escolha == 1:
                    venceu_base()
                elif setima_escolha == 2:
                    perdeu()
                else:   
                    escolha_invalida()
            else:   
                escolha_invalida()
        else:   
            escolha_invalida()

    else:
        escolha_invalida()
        
        

programa_principal()


'''Projeto final do Módulo 1 - Introdução ao Python do curso vamo AI, parceria entre o iFood e a Resilia.
Autora: Caroline H. Suwaki
Descrição: O jogo acontece em um cenário pós-apocalíptico e a missão do usuário é descobrir a melhor maneira de coletar os itens de beleza.
O usuário poderá navegar entre os cenários (pilha de ossos, poça radioativa e pilha de animais mortos) para coletar os itens disponíveis
(água radiaoativa e martelo; pele de raposa em decomposição e chinelo; ossos e garrafa). Para isso, deverá escolher inicialmente 
para qual local gostaria de ir, e a seguir tomar decisões de coletar os itens ou explorar o próximo local. O usuário deverá ficar atento se possui
a ferramenta adequada para coletar o item escolhido.
'''


def intro(): 
    print("Você sobreviveu a um apocalipse nuclear e agora precisa lutar pela sobrevivência no mundo pós-apocalíptico. Mas antes, prioridades. \n\
Você percebeu que não tem nenhum item de beleza na sua bolsa Golce & Dabanna para encarar esse mundo cruel e deseja encontrá-los \n\
para arrasar na balada Plutônio Night Club, a nova sensação da cidade. Para isso, você precisa navegar entre os locais próximos ao seu bunker e utilizar os itens para produzir itens \n\
de maquiagem. Durante o caminho, você pode encontrar alguns personagens que te darão dicas, mas atenção! Para coletar os itens encontrados você precisa de ferramentas que podem estar em outros locais, então procure bem. Boa sorte! \n\
Bem-vindo (a), sobrevivente! \n")

    
    print(('\033[47;1;30m' + """
  _                                            _                                                              
 |_)  _  ._ _       o ._   _|  _     _.  _    |_ _. |_      |  _   _  _     /\  ._   _   _  _. | o ._   _  _  
 |_) (/_ | | |   \/ | | | (_| (_)   (_| (_)   | (_| |_) |_| | (_) _> (_)   /--\ |_) (_) (_ (_| | | |_) _> (/_ 
                                                                                |                  |          
\n""" + '\033[0;0m')) 

def nome():
    nome = input("Para encarar essa aventura, quem você quer ser? Entre com o nome correspondente. \n\
    1. Cardi C.: Influencer, estilosa, famosa, blogueira sem blog. Nossa mais querida chernogirl. \n\
    2. Cora Aventureira: Surfista, trilheira, atleta. Não abre mão de bons produtos para manter a pose na academia em destroços que frequenta. \n\
    3. Jaque Chan: Lutadora profissional, dizem que seu pai era famoso no Antigo Planeta Terra. Ninguém mexe com ela. Usa produtos especializados para arrasar em suas batalhas. \n")
    while True: 
        if nome.title() == "Cardi C" or nome.title() == "Cora Aventureira" or nome.title() == "Jaque Chan":
            break
        else:
            nome = input("Escolha inválida. Por favor, entre com uma opção válida. Para encarar essa aventura, quem você quer ser? Entre com o nome correspondente. \n\
    1. Cardi C.: Influencer, estilosa, famosa, blogueira sem blog. Nossa mais querida chernogirl. \n\
    2. Cora Aventureira: Surfista, trilheira, atleta. Não abre mão de bons produtos para manter a pose na academia em destroços que frequenta. \n\
    3. Jaque Chan: Lutadora profissional, dizem que seu pai era famoso no Antigo Planeta Terra. Ninguém mexe com ela. Usa produtos especializados para arrasar em suas batalhas. \n")
    print(f"Olá, {nome.title()}! ")
    programa_principal()

def primeira_escolha():
    primeira_escolha = int(input("\n\
Isso! É sua chance de fazer um batom neon incrível! Quando você começa a se aproximar da poça radioativa, você vê a onça Carol com C matando sua sede \n\
calmamente. Ela parece amigável. Próximo a ela, você enxerga um martelo. O que você faz? Entre com o número correspondente. \n\
    \n\
    1. Ela não parece perigosa, calmamente você caminha até a poça para coletar a água. \n\
    2. Que medo! Melhor coletar o chinelo e explorar a pilha de ossos. \n"))
    return primeira_escolha

def segunda_escolha():
    segunda_escolha = int(input("\n\
Que lugar incrível! Uma pilha de ossos imensa e um chinelo! Você observa a Zumbi Quim Cardaxa fazendo tutoriais para o Zombietube. Você se aproxima, ela diz: \n\
    \n\
     - Olá, forasteira! Você vai adorar essa sombra triturada de ossos que estou usando! Você pode fazer uma igual, se quiser. \n\
O que você faz? Entre com o número correspondente.  \n\
    \n\
    1. Triturar os ossos. \n\
    2. Hmmm, não fui com a cara da Quim, melhor coletar o chinelo e ir explorar a pilha de animais mortos. \n"))
    return segunda_escolha

def quarta_escolha():
    quarta_escolha = int(input("\n\
Você chegou à pilha de animais mortos e avista a diva Bion-C com um lindo casaco de peles e uma garrafa. Ao se aproximar, ela diz: \n\
    \n\
     - Olá, forasteira! Aqui nessa pilha de animais há maravilhosas peles de raposa em decomposição. Mas cuidado! As baratas decompositoras podem te atacar. \n\
    Você decide então... Entre com o número correspondente: \n\
    \n\
    1. Coletar o casaco. \n\
    2. Guardar a garrafa e explorar a Poça Radioativa. \n"))
    return quarta_escolha

def perdeu():
    print('\033[0;1;31m' + """
    Escolha terrível! Você não soube explorar as ferramentas ou não as possui. Da próxima vez, pense melhor! Você perdeu!
    \n""" + '\033[0;0m')
    perdeu = input("Deseja jogar novamente? Responda sim ou não. \n")
    while True:
        if perdeu.title() == "Sim":
            programa_principal()
        else:
            print("Fim de jogo!")
        break

def escolha_invalida():
    invalido = input("Escolha inválida! Deseja jogar novamente? Responda sim ou não. \n")
    while True:
        if invalido.title() == "Sim":
            programa_principal()
        else:
            print("Fim de jogo!")
        break

def venceu_casaco():
    print('\033[0;1;33m' + """
    Buonasera Gatuxa! Você fez um lindo casaco de peles de raposa em decomposição após matar as baratas com o chinelo que estava na pilha de ossos e vai mostrar sua beleza radiante por aí! Parabéns! Você venceu!
    \n""" + '\033[0;0m')
    ganhou = input("Deseja jogar novamente? Responda sim ou não. \n")
    if ganhou.title() == "Sim":
        programa_principal()
    else:
        print("Fim de jogo!")
    return ganhou
    
def venceu_batom():
    print('\033[0;1;33m' + """
    Buonasera Gatuxa! Você fez um lindo batom neon coletando a água radioativa com a garrafa encontrada na pilha de animais mortos e vai mostrar sua beleza radiante por aí! Parabéns! Você venceu!
    \n""" + '\033[0;0m')
    ganhou = input("Deseja jogar novamente? Responda sim ou não. \n")
    if ganhou.title() == "Sim":
        programa_principal()
    else:
        print("Fim de jogo!")
    return ganhou

def venceu_base():
    print('\033[0;1;33m' + """
    Buonasera Gatuxa! Você fez uma linda base com os ossos que você triturou com o martelo encontrado na poça radioativa e vai mostrar sua beleza radiante por aí! Parabéns! Você venceu!
    \n""" + '\033[0;0m')
    ganhou = input("Deseja jogar novamente? Responda sim ou não. \n")
    if ganhou.title() == "Sim":
        programa_principal()
    else:
        print("Fim de jogo!")
    return ganhou
    
def programa_principal():
    local = input(f"Você decidiu sair do seu bunker para explorar a região. À sua direita há uma 1. poça radioativa; à esquerda, uma 2. pilha de ossos; e à frente uma 3. pilha de animais mortos. \n\
Para onde você deseja ir? Entre com o nome do local ou com o número correspondente.  \n")

    if local.title() == 'Poça Radioativa' or local.title() == '1': 
        pri_e = primeira_escolha() 
        if pri_e == 1:
            perdeu()
        elif pri_e == 2:
            seg_e = segunda_escolha()
            if seg_e == 1:
                venceu_base()
            elif seg_e == 2:
                terceira_escolha = int(input("\n\
Você chegou à pilha de animais mortos e avista a diva Bion-C com um lindo casaco de peles. Ao se aproximar, ela diz: \n\
    \n\
    - Olá, forasteira! Aqui nessa pilha de animais há maravilhosas peles de raposa em decomposição. Mas cuidado! As baratas decompositoras podem te atacar. \n\
Você decide então... Entre com o número correspondente. : \n\
    \n\
    1. Usar o chinelo para matar as baratas. \n\
    2. Desiste, afinal nada chegou aos pés do seu glamour. \n"))
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
                quinta_escolha = int(input("\n\
Isso! É sua chance de fazer um batom neon incrível! Quando você começa a se aproximar da poça radioativa, você vê a onça Carol com C matando sua sede \n\
calmamente. Ela parece amigável. Próximo a ela, você enxerga um martelo. O que você faz? Entre com o número correspondente.  \n\
    \n\
    1. Ela não parece perigosa, calmamente você caminha até a poça para coletar a água. \n\
    2. Desiste, afinal nada chegou aos pés do seu glamour. \n"))
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
            sexta_escolha = int(input("\n\
Isso! É sua chance de fazer um batom neon incrível! Quando você começa a se aproximar da poça radioativa, você vê a onça Carol com C matando sua sede \n\
calmamente. Ela parece amigável. Próximo a ela, você enxerga um martelo. O que você faz? Entre com o número correspondente.  \n\
    \n\
    1. Ela não parece perigosa, calmamente você caminha até a poça para coletar a água. \n\
    2. Que medo! Melhor coletar o chinelo e explorar a pilha de ossos. \n "))
            if sexta_escolha == 1:
                venceu_batom()
            elif sexta_escolha == 2:
                setima_escolha =  int(input("\n\
Que lugar incrível! Uma pilha de ossos imensa e um chinelo! Você observa a Zumbi Quim Cardaxa fazendo tutoriais para o Zombietube. Você se aproxima, ela diz: \n\
    \n\
    - Olá, forasteira! Você vai adorar essa sombra triturada de ossos que estou usando! Você pode fazer uma igual, se quiser. \n\
O que você faz? Entre com o número correspondente. \n\
    \n\
    1. Triturar os ossos. \n\
    2. Desiste, afinal nada chegou aos pés do seu glamour. \n"))
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
         
intro()
nome()
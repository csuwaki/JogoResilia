def intro():
    print("Você sobreviveu a um apocalipse nuclear e agora precisa lutar pela sua sobrevivência no mundo pós-apocalíptico. Mas antes, as prioridades. \n\
Você percebeu que não tem nenhum item de beleza na sua bolsa Golce & Dabanna para encarar esse mundo cruel e deseja encontrá-los \n\
para arrasar na balada Plutônio Night Club. \n\
Atenção! Para coletar os itens encontrados você precisa de outras ferramentas, então procure bem. Boa sorte! \n\
Bem-vindo (a), sobrevivente!")

    nome = input("Como posso te chamar? ")
    return nome



nome = intro()
print(f"Olá, {nome.title()}. \n\
Você decidiu sair do seu bunker para explorar a região. À sua direita há uma poça radioativa; à esquerda, uma pilha de ossos; à frente uma pilha de animais mortos. \n\
Para onde você deseja ir?")



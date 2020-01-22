def ParOuImpar(numero):
    try:
        numero = int(numero)
    #if(isinstance(numero, int)):
        if(math.fmod(numero,2)>0):
            print(numero, 'é ', "ímpar")
        else:
            print(numero, 'é ', "par")
    #else:
    #    print('Use apenas número!')
    except :
        print("Dado inválido")

ParOuImpar(random.randint(0, 100))
entrada = input("digite um número: ")
ParOuImpar(entrada)
def jogar():
    import random

    #Entrada do jogo.
    print("********************************");
    print("Bem vindo ao jogo da Advinhação!");
    print("********************************");

    #A variavel ira receber um numero aleatorio dentro do intervalo entre 1 e 100 atraves da biblioteca ""Random"
    numero_secreto = random.randint(1,100);
    print(numero_secreto);

    pontos = 1000;

    """
    O laço while True cria um loop infinito ate que o jogador insira um numero valido proposto para acionar o break.
    Enquanto o jogador não fizer uma escolha válida, o código dentro do loop será repetido continuamente, exibindo as opções de dificuldade e solicitando ao jogador que faça uma escolha. 
    O loop só será interrompido quando o jogador fizer uma escolha válida e uma instrução break for executada, permitindo que o código continue com a próxima etapa.
    """
    total_de_tentativas = 0;
    while True: 
        print("Qual o nivel de dificuldade voce deseja?");
        print("(1) Facil (2) Medio (3) Dificil");
        
        try:
            nivel = int(input("Defina o nivel: "))
        except ValueError:
            nivel = None
        """
        A ideia do try-except é tentar executar um bloco de código dentro do bloco try e, se uma exceção ocorrer, capturá-la e executar um bloco de código específico dentro do bloco except.
        Se a conversão for bem-sucedida, ou seja, se o jogador digitar um valor numérico válido, a variável nivel será definida com esse valor convertido. Ou seja, Numeros no geral, se digitar 1, sera def como 1.
        
        No entanto, se a conversão falhar, isso significa que o jogador digitou algo que não pode ser convertido para um número inteiro, como uma letra. Nesse caso, uma exceção do tipo ValueError será lançada.
        O bloco except ValueError captura essa exceção específica e, dentro desse bloco, o valor da variável nivel é definido como None. 
        Ou seja, quando ocorrer uma exceção de ValueError, a variável nivel terá o valor None.
        
        Nesta situacao, se o jogador digitar um letra ira cair no "Case _"
        """
        match nivel:
            case 1:
                total_de_tentativas = 20;
                break;                      
            case 2:
                total_de_tentativas = 10;
                break;
            case 3:
                total_de_tentativas = 5;
                break;
            case _:
                print("Dificuldade inválida! Tente novamente digitando um numero de 1 a 3!");
        """
        O match avalia o valor de nivel e executa o bloco de código correspondente ao caso que satisfaz o padrão de correspondência. 
        O caso curinga _ é usado para capturar qualquer outro valor que não corresponda aos casos específicos anteriores.
        """
    print("Voce possui um total de {} tentativas para acertar o numero secreto".format(total_de_tentativas));
    
    for tentativas in range (1, total_de_tentativas + 1):
        """
        A variável tentativas é uma variável que vai assumir o valor de cada elemento da sequência à medida que o loop é executado. 
        Por exemplo, quando começar, o looping vai começar em 1, logo, ela assume esse valor.
        É como se fosse um contador para acompanhar o número da tentativa atual.
        
        O range(1, total_de_tentativas + 1) cria uma sequência de números começando em 1 e indo até total_de_tentativas(5 no caso).
        O + 1 é necessário para garantir que a última tentativa seja incluída na sequência, pois, o range é exclusivo, entao se colocar de 1 a 5, ele so chega ate o 4, pq o 5 é exclusivo.
        """
      
        chute = int(input("Digite o seu numero dentro de 1 e 100: "));
        print("Voce digitou:", chute);
        """
        O programa ira perguntar o numero do jogador e irá guardar na variavel chute em forma de inteiro, pois esta dentro da função "int"
        
        O numero digitado pelo jogador sera recebido em STR para a variavel 'chute', contudo colocamos o 'chute' dentro de um int para transformar a variavel em um inteiro,
        entao o numero digitado pelo jogador sera guardado na variavel 'chute' como um INT e posteriormente mostrado pelo sistema em print.
        """
        #Caso o jogador digite um numero fora do intervalo 1 e 100, sera dado como invalido e o jogador perdera a tentativa, o programa entao irá seguir o looping.
        if(chute < 1 or chute > 100):
            print("Voce digitou um numero invalido!\nDigite um numero entre 1 e 100.\nRestam {} tentativas.". format(total_de_tentativas - tentativas))
            continue;           
        
        match chute:
                case chute if chute == numero_secreto:
                        print("Voce acertou e fez {} pontos!" .format(pontos));
                        break;
                case chute if chute > numero_secreto:
                        print("Voce errou! :( Seu chute foi maior que o numero secreto.");
                        pontos -= abs(numero_secreto - chute);
                case chute if chute < numero_secreto:
                        print("Voce errou! :( Seu chute foi menor que o numero secreto.");
                        pontos -= abs(numero_secreto - chute);
        
        
        #Se o numero de tentativas for igual ao total de tentativas (5), o jogo encerra.
        if tentativas == total_de_tentativas:
            print("Suas tentativas acabaram. O numero secreto era {}." .format(numero_secreto));
            print("FIM DE JOGO");
            break;
        
        #Sempre que o jogador errar, teremos tentativas - o total de tentivas, ou seja, se ele tentou 2, sera 5 - 2, errou 4, 5 - 4, errou 5, o programa encerra sem passar por esta condição.
        tentativas_restantes = total_de_tentativas - tentativas;
        print("Tente Novamente! Restam {} de {} tentativas." .format(tentativas_restantes, total_de_tentativas));
        
if(__name__ == "__main__"):
    jogar();
    """
    Verificacao para ver se o arquivo esta sendo executado diretamente como um programa ou nao
    Quando um arquivo Python é executado diretamente como um programa, o valor de __name__ é definido como "__main__". 
    Por outro lado, se o arquivo é importado como um módulo em outro arquivo, o valor de __name__ será o nome do módulo.
    """
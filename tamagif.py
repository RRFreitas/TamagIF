#Imports
import time
import BDTamagushy
import sqlite3
import InterfaceTamagushy
import MenuTamagushy
import novoJogo

#Variaveis auxiliares
continuar = True # Variavel para determinar se ele ira continuar a rodar o progama
animal = None  # Feita para a função iniciarBD poder aza-la para iniciar a class bichinho

def iniciarBD(newBd,tela,fontePadrao,cores,rosto):
    BDTamagushy.conectarBD()
    #Verificando se a tabela existe
    if (not BDTamagushy.tabela_existe("dados")):
        print("Banco de dados não existe.")
        print("Criando banco de dados...")
        print()
        
        #Chama a função para criar a tabela
        
        BDTamagushy.criarBD()
        continuar = True
        # Chama a variavel animal GLobal
        global animal
        # Chamara a função newGame de novojogo que está encarregada de mostrar a tela de novo jogo e retornar uma tupla com o nome 
        # e com uma tupla de interiros representando a cor
        print('antes')
        nomeCor = novoJogo.newGAme(tela, fontePadrao, cores, rosto)
        #Separando valores retornados da função newGAme para melhor utilização
        print('dps')
        nome = nomeCor[0]
        cor = nomeCor[1]

        print(nome, cor)
        #adiciona as informações obtdas no Banco de dados
        BDTamagushy.adicionarInformacoes(nome, 0, 100, 100)
        # diz para o progama que não será presciso criar um novo bichinho, pois ja fio criado
        newBd = False
    
    #função para criar um novo bichinho, ou novo jogo
    if(newBd):
        #Realiza a mesma coisa que o if anterior, mas dessa vez ele atualiza os dados ao inves de adiciona-los
        continuar = True
        global animal
        nomeCor = novoJogo.newGAme(tela,fontePadrao,cores,rosto)
        nome = nomeCor[0]
        cor = nomeCor[1]
        BDTamagushy.atualizarDados(nome,0,100,100)


    #ler os dados do banco de Dados !!!! ELE ESTÁ COM PROBLEMA, ELE NÃO IDENTIFICA NADA DENTRO DO BANCO DE DADOS!!!
    #Acho que magicamente ajeitei
    dadosT = BDTamagushy.ler_todos_clientes()
    linha = 0
    print('asjidojas')
    print(dadosT) # essa variavelfoi criado para eu ver se ele cria o banco de dados corretamento
    # Iniciar a classe bichinho  e atribui a animal com os valores do banco de dados
    animal = bichinho(dadosT[linha][1], dadosT[linha][2], dadosT[linha][3], dadosT[linha][4])

    print("--------------------")
    print("Seu Nome:", animal.getNome())
    print("Sua Saúde:", animal.getSaude())
    print("Fome:", animal.getFome())
    print("Sua Idade:", animal.getIdade())
    print("--------------------")


#Essa parte vocÊ sabe;)
class bichinho():
    def __init__(self, nome, idade, fome, saude):
        self.nome = nome
        self.idade = idade
        self.fome = fome
        self.saude = saude
        self.nascimento = horasEmSegundos()
        self.ultimaAlimentacao = horasEmSegundos()
        self.ultimaMedicacao = horasEmSegundos()
        # Alterar

    def setNome(self, n):
        self.nome = n
        print("Nome alterado com sucesso.")

    def setFome(self, f):
        tempoSC = horasEmSegundos() - self.ultimaAlimentacao
        fome = tempoSC // 5
        self.ultimaAlimentacao = horasEmSegundos()
        ultimaAlimentacao = horasEmSegundos
        self.fome = self.fome - fome + f

    def setSaude(self, s):
        tempoSaude = horasEmSegundos() - self.ultimaMedicacao
        saude = tempoSaude // 10
        self.ultimaMedicacao = horasEmSegundos()
        self.saude = s

    # Retornadores
    def getIdade(self):
        return self.idade + ((horasEmSegundos() - self.nascimento) // 10)

    def getNome(self):
        return self.nome

    # tempoSC -->> tempo Sem Comer4

    # TEMOS UM PROBLEMA AQUI ENVOLVENDO O BD
    def getFome(self):
        tempoSC = horasEmSegundos() - self.ultimaAlimentacao
        fome = tempoSC // 5

        self.fome = 100 - fome
        return self.fome

    def getSaude(self):
        tempoSaude = horasEmSegundos() - self.ultimaMedicacao
        saude = tempoSaude // 5

        self.saude = self.saude - saude
        self.ultimaMedicacao = horasEmSegundos()
        return self.saude


def Ver():
    print()
    print("--------------------")
    print("Seu Nome:", animal.getNome())
    print("Sua Saúde:", animal.getSaude())
    print("Fome:", animal.getFome())
    print("Sua Idade:", animal.getIdade())
    print("--------------------")
    print()


def horasEmSegundos():
    horario = ((time.localtime().tm_hour - 3) * 3600) + (time.localtime().tm_min * 60) + time.localtime().tm_sec
    return horario

#Esses parametros são para ele fazer a tela
#newBD = Identifica se deverá ser criado um novo bichinho
#tela = é a tela prncipal onde será exibido as informaõe e interações
#é a fonte padrao para todo texto no progaa
#Cores é aquele dicionario de cores
#E rosto é a imagem que criasse

def tamagif(newBd,tela,fontePadrao,cores,rosto):
    global continuar
    print('tamagif')

    iniciarBD(newBd,tela,fontePadrao,cores,rosto)

    horarioInicial = horasEmSegundos()

    while (continuar):
        print("chegou")

        horasEmSegundos()
        print(
            "Opções:\n 1-Alterar Nome \n 2-Dar comida \n 3-Dar remédio \n 4-Ver informações \n 5-Sair e salvar informações")
        #Para identificar a decisão do usuario ele chamará a tela rincipal e analizara a escolha
        escolha = InterfaceTamagushy.janelaPrincipal(tela, rosto)

        if (escolha == 1):
            n = input("Digite o novo nome do seu bichinho: ")
            animal.setNome(n)

        elif (escolha == 2):
            Qcomida = float(input("Digite quantas comidas você vai dar a seu bichinho: "))
            f = Qcomida

            animal.setFome(f)

        elif (escolha == 3):
            Qremedio = int(input("Digite quantas pilulas você vai dar a seu bichinho: "))
            s = animal.getSaude()
            s = s + Qremedio
            print(s)
            animal.setSaude(s)

        elif (escolha == 4):
            Ver()

        elif (escolha == 5):
            print()
            print("Volte Sempre!")

            continuar = False

            BDTamagushy.atualizarDados(animal.getNome(), animal.getIdade(), animal.getFome(), animal.getSaude())


        else:
            print()
            print("Tente Novamente.")
            print()

executar = True
while(executar):
    #chama o menu e analiza oque o usuario deseja fazer
    respostaMenu = MenuTamagushy.menu()
    newBd = respostaMenu[0]
    tela = respostaMenu[2]
    fontePadrao = respostaMenu[3]
    cores = respostaMenu[4]
    rosto = respostaMenu[5]
    print(respostaMenu)

    if (respostaMenu[1] == 1):
        print('resposta 1')
        tamagif(newBd,tela,fontePadrao,cores,rosto)

    elif (respostaMenu[1] == 2):
        print('resposta 2')
        tamagif(newBd,tela,fontePadrao,cores,rosto)

    elif (respostaMenu[1] == 3):
        executar = False


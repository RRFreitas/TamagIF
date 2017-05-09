#Imports
import time
import BDTamagushy
import sqlite3
import novoJogo
import InterfaceTamagushy
import MenuTamagushy
import jogo1

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
        nomeCor = novoJogo.newGAme(tela, fontePadrao, cores, rosto)

        nome = nomeCor[0]
        cor = nomeCor[1]
        r = cor[0]
        g = cor[1]
        b = cor[2]
        #adiciona as informações obtdas no Banco de dados
        BDTamagushy.adicionarInformacoes(nome, 0, 100, 100,r,g,b)
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
        r = cor[0]
        g = cor[1]
        b = cor[2]
        BDTamagushy.atualizarDados(nome,0,100,100,r,g,b)


    #ler os dados do banco de Dados !!!! ELE ESTÁ COM PROBLEMA, ELE NÃO IDENTIFICA NADA DENTRO DO BANCO DE DADOS!!!
    dadosT = BDTamagushy.ler_todos_clientes()
    linha = 0
    print(dadosT) # essa variavelfoi criado para eu ver se ele cria o banco de dados corretamento

    ajudinha = dadosT[linha]
    animal = bichinho(dadosT[linha][1], dadosT[linha][2], dadosT[linha][3], dadosT[linha][4],dadosT[linha][5],dadosT[linha][6],dadosT[linha][7])

    print("--------------------")
    print("Seu Nome:", animal.getNome())
    print("Sua Saúde:", animal.getSaude())
    print("Fome:", animal.getFome())
    print("Sua Idade:", animal.getIdade())
    print("--------------------")


#Essa parte vocÊ sabe;)
class bichinho():
    def __init__(self, nome, idade, fome, saude,r,g,b):
        self.nome = nome
        self.idade = idade
        self.fome = fome
        self.saude = saude
        self.cor = (r,g,b)
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
    def getCor (self):
        return self.cor

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
    continuar = True
      
    iniciarBD(newBd,tela,fontePadrao,cores,rosto)

    horarioInicial = horasEmSegundos()

    while (continuar):
        print("chegou")

        horasEmSegundos()
        print(
            "Opções:\n 1-Alterar Nome \n 2-Dar comida \n 3-Dar remédio \n 4-Ver informações \n 5-Sair e salvar informações")
        #Para identificar a decisão do usuario ele chamará a tela rincipal e analizara a escolha

        nome = animal.getNome()
        escolha = InterfaceTamagushy.janelaPrincipal(tela, rosto,fontePadrao,animal)
        #Eu havia retitado a escolha 2 e 3 , mas vou só vou retirar quando terinarmos de fazer isso na tela rincial
        if (escolha[0] == 2):
            Qcomida = float(input("Digite quantas comidas você vai dar a seu bichinho: "))
            f = Qcomida

        elif (escolha == 3):
            Qremedio = int(input("Digite quantas pilulas você vai dar a seu bichinho: "))
            s = animal.getSaude()
            s = s + Qremedio
            print(s)
            animal.setSaude(s)

        elif (escolha[0] == 4):
            jogo1.jogoNave()

        elif (escolha[0] == 5):
            print()
            print("Volte Sempre!")

            nome = escolha[1]
            continuar = False
            cor = animal.getCor()
            r = cor[0]
            g = cor[1]
            b = cor[2]
            print(nome)
            print(escolha[1])
            print(escolha[2])
            print(animal.getFome)

            BDTamagushy.atualizarDados(escolha[1], escolha[2], escolha[3], escolha[4],r,g,b)




executar = True
while(executar):
    #chama o menu e analiza oque o usuario deseja fazer
    respostaMenu = MenuTamagushy.menu()
    newBd = respostaMenu[0]
    resposta = respostaMenu[1]
    tela = respostaMenu[2]
    fontePadrao = respostaMenu[3]
    cores = respostaMenu[4]
    rosto = respostaMenu[5]
    print("oi",respostaMenu)

    if (resposta == 1):
        tamagif(newBd,tela,fontePadrao,cores,rosto)

    elif (resposta == 2):
        tamagif(newBd,tela,fontePadrao,cores,rosto)

    elif (resposta == 3):
        executar = False


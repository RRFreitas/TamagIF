# Imports
import time
import BDTamagushy
import sqlite3
import novoJogo
import InterfaceTamagushy
import MenuTamagushy
import jogo1
import jogo2

# Variaveis auxiliares
continuar = True  # Variavel para determinar se ele ira continuar a rodar o progama
animal = None  # Feita para a função iniciarBD poder aza-la para iniciar a class bichinho


def iniciarBD(newBd, tela, fontePadrao, cores, rosto):
    BDTamagushy.conectarBD()
    # Verificando se a tabela existe
    if (not BDTamagushy.tabela_existe("dados")):
        print("Banco de dados não existe.")
        print("Criando banco de dados...")
        print()

        # Chama a função para criar a tabela

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
        # adiciona as informações obtdas no Banco de dados
        BDTamagushy.adicionarInformacoes(nome, 0, 100, 100, r, g, b,0,0,5,5)
        # diz para o progama que não será presciso criar um novo bichinho, pois ja fio criado
        newBd = False

    # função para criar um novo bichinho, ou novo jogo
    if (newBd):
        # Realiza a mesma coisa que o if anterior, mas dessa vez ele atualiza os dados ao inves de adiciona-los
        continuar = True
        global animal
        nomeCor = novoJogo.newGAme(tela, fontePadrao, cores, rosto)
        nome = nomeCor[0]
        cor = nomeCor[1]
        r = cor[0]
        g = cor[1]
        b = cor[2]
        BDTamagushy.atualizarDados(nome, 0, 100, 100, r, g, b,0,0,5,5)

    # ler os dados do banco de Dados !!!! ELE ESTÁ COM PROBLEMA, ELE NÃO IDENTIFICA NADA DENTRO DO BANCO DE DADOS!!!
    dadosT = BDTamagushy.ler_todos_clientes()
    linha = 0
    print(dadosT)  # essa variavelfoi criado para eu ver se ele cria o banco de dados corretamento

    animal = bichinho(dadosT[linha][1], dadosT[linha][2], dadosT[linha][3], dadosT[linha][4], dadosT[linha][5],dadosT[linha][6], dadosT[linha][7],dadosT[linha][8],dadosT[linha][9],dadosT[linha][10],dadosT[linha][11])




# Essa parte vocÊ sabe;)
class bichinho():
    def __init__(self, nome, idade, fome, saude, r, g, b,recordJG1,recordJG2,comidas,pilulas):
        self.nome = nome
        self.idade = idade
        self.fome = fome
        self.saude = saude
        self.cor = (r, g, b)
        self.recordJG1 = recordJG1
        self.recordJG2 = recordJG2
        self.comidas = comidas
        self.pilulas = pilulas
        self.nascimento = horasEmSegundos()
        self.ultimaAlimentacao = horasEmSegundos()
        self.ultimaMedicacao = horasEmSegundos()
        self.auxiliarTempo = horasEmSegundos()
        # Alterar

    def setNome(self, n):
        self.nome = n
        print("Nome alterado com sucesso.")

    def setFome(self, f):
        tempoSC = horasEmSegundos() - self.ultimaAlimentacao
        fome = tempoSC // 5
        self.ultimaAlimentacao = horasEmSegundos()
        self.fome = self.fome - fome + f
        return self.fome

    def setSaude(self, s):
        tempoSaude = horasEmSegundos() - self.ultimaMedicacao
        saude = tempoSaude // 10
        if self.saude < 100:
            for n in range(0,s):
                self.saude +=1
                if self.saude == 100:
                    break
        return self.saude

    def setComidas (self,c):
        self.comidas += c
        return  self.pilulas

    def setPilulas (self,p):
        self.pilulas += p
        return self.pilulas

    def getComidas(self,comeu):
        if comeu:
            self.comidas -= 1
        return self.comidas

    def getPilulas(self,medicou):
        if medicou:
            self.pilulas -= 1
        return self.pilulas

    def getRecordJG1(self,pontos):
        if pontos > self.recordJG1:
            self.recordJG1 = pontos
        return self.recordJG1

    def getRecordJG2(self,pontos):
        if pontos > self.recordJG2:
            self.recordJG2 = pontos
        return self.recordJG2


    # Retornadores
    def getCor(self):
        return self.cor

    def getIdade(self,idade):
        if idade < 30:
            if ((horasEmSegundos() - self.auxiliarTempo) // 10) > 0:
                self.idade =  self.idade + ((horasEmSegundos() - self.auxiliarTempo) // 10)
                self.auxiliarTempo = horasEmSegundos()
        return self.idade




    def getNome(self):
        return self.nome

    # tempoSC -->> tempo Sem Comer4

    # TEMOS UM PROBLEMA AQUI ENVOLVENDO O BD
    def getFome(self,fomeAuxiliar):
        if fomeAuxiliar > 0:

            tempoSC = horasEmSegundos() - self.ultimaAlimentacao
            fome = tempoSC // 5

            if fome > 0:
                self.fome = self.fome - fome
                self.ultimaAlimentacao = horasEmSegundos()
                print(self.fome)

        else:
            continuar = False
            print("Game Over")


        return self.fome

    def getSaude(self,saudeAuxiliar):
        if saudeAuxiliar > 0:
            tempoSaude = horasEmSegundos() - self.ultimaMedicacao
            saude = tempoSaude // 5

            if saude > 0:
                self.saude = self.saude - saude
                self.ultimaMedicacao = horasEmSegundos()

        else:
            continuar = False
            print("Game Over")

        return self.saude


def horasEmSegundos():
    horario = ((time.localtime().tm_hour - 3) * 3600) + (time.localtime().tm_min * 60) + time.localtime().tm_sec
    return horario


# Esses parametros são para ele fazer a tela
# newBD = Identifica se deverá ser criado um novo bichinho
# tela = é a tela prncipal onde será exibido as informaõe e interações
# é a fonte padrao para todo texto no progaa
# Cores é aquele dicionario de cores
# E rosto é a imagem que criasse

def tamagif(newBd, tela, fontePadrao, cores, rosto):
    continuar = True

    iniciarBD(newBd, tela, fontePadrao, cores, rosto)

    horarioInicial = horasEmSegundos()

    while (continuar):
        print("chegou")

        horasEmSegundos()
        print(
            "Opções:\n 1-Alterar Nome \n 2-Dar comida \n 3-Dar remédio \n 4-Ver informações \n 5-Sair e salvar informações")
        # Para identificar a decisão do usuario ele chamará a tela rincipal e analizara a escolha

        nome = animal.getNome()
        escolha = InterfaceTamagushy.janelaPrincipal(tela, rosto, fontePadrao, animal)
        # Eu havia retitado a escolha 2 e 3 , mas vou só vou retirar quando terinarmos de fazer isso na tela rincial


        if (escolha[0] == 4):
            cor = escolha[5]
            minigame = escolha[6]

            h = ((escolha[2] // 2) * 10) + 50
            print(h)
            w = h - (100 - escolha[4])
            print(w)
            if minigame == 1:
                pontos = jogo1.jogoNave(cor,w,h,fontePadrao,escolha[2])
                animal.getRecordJG1(pontos)
                animal.setComidas(pontos)

            if minigame == 2:
                pontos = jogo2.jogo2(w,h,cor)
                print("EI",pontos)
                animal.getRecordJG2(pontos)
                animal.setPilulas(pontos)


        elif (escolha[0] == 5):
            print()
            print("Volte Sempre!")

            nome = escolha[1]
            continuar = False
            cor = escolha[5]
            r = cor[0]
            g = cor[1]
            b = cor[2]

            print(escolha[1], escolha[2], escolha[3], escolha[4], r, g, b)

            nome = escolha[1]
            idade = escolha[2]
            fome = escolha[3]
            saude = escolha[4]
            recordJG1 = escolha[7]
            recordJG2 = escolha[8]
            comidas = escolha[9]
            pilulas = escolha[10]
            print(r,g,b)

            BDTamagushy.atualizarDados(nome, idade, fome, saude, r, g, b,recordJG1,recordJG2,comidas,pilulas)


        elif(escolha[0] == 6):
            BDTamagushy.deletarDados()
            continuar = False


executar = True
while (executar):
    # chama o menu e analiza oque o usuario deseja fazer
    respostaMenu = MenuTamagushy.menu()
    newBd = respostaMenu[0]
    resposta = respostaMenu[1]
    tela = respostaMenu[2]
    fontePadrao = respostaMenu[3]
    cores = respostaMenu[4]
    rosto = respostaMenu[5]

    if (resposta == 1):
        tamagif(newBd, tela, fontePadrao, cores, rosto)

    elif (resposta == 2):
        tamagif(newBd, tela, fontePadrao, cores, rosto)

    elif (resposta == 3):
        executar = False

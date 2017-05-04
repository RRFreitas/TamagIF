import time
import BDTamagushy
import sqlite3
import novoJogo
import InterfaceTamagushy
import MenuTamagushy


continuar = True
animal = None

def iniciarBD(newBd,tela,fontePadrao,cores,rosto):
    BDTamagushy.conectarBD()

    if (not BDTamagushy.tabela_existe("dados")):
        print("Banco de dados não existe.")
        print("Criando banco de dados...")
        print()
        BDTamagushy.criarBD()
        continuar = True
        global animal
        nomeCor = novoJogo.newGAme(tela, fontePadrao, cores, rosto)
        nome = nomeCor[0]
        cor = nomeCor[1]
        BDTamagushy.adicionarInformacoes(nome, 0, 100, 100)
        newBd = False

    if(newBd):
        continuar = True
        global animal
        nomeCor = novoJogo.newGAme(tela,fontePadrao,cores,rosto)
        nome = nomeCor[0]
        cor = nomeCor[1]
        BDTamagushy.atualizarDados(nome,0,100,100)



    dadosT = BDTamagushy.ler_todos_clientes()
    linha = 0
    print(dadosT)
    animal = bichinho(dadosT[linha][1], dadosT[linha][2], dadosT[linha][3], dadosT[linha][4])

    print("--------------------")
    print("Seu Nome:", animal.getNome())
    print("Sua Saúde:", animal.getSaude())
    print("Fome:", animal.getFome())
    print("Sua Idade:", animal.getIdade())
    print("--------------------")



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


def tamagif(newBd,tela,fontePadrao,cores,rosto):
    global continuar

    iniciarBD(newBd,tela,fontePadrao,cores,rosto)

    horarioInicial = horasEmSegundos()

    while (continuar):
        print("chegou")

        horasEmSegundos()
        print(
            "Opções:\n 1-Alterar Nome \n 2-Dar comida \n 3-Dar remédio \n 4-Ver informações \n 5-Sair e salvar informações")
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
    respostaMenu = MenuTamagushy.menu()
    newBd = respostaMenu[0]
    tela = respostaMenu[2]
    fontePadrao = respostaMenu[3]
    cores = respostaMenu[4]
    rosto = respostaMenu[5]
    print(respostaMenu)

    if (respostaMenu[1] == 1):
        tamagif(newBd,tela,fontePadrao,cores,rosto)

    elif (respostaMenu[1] == 2):
        tamagif(newBd,tela,fontePadrao,cores,rosto)

    elif (respostaMenu[1] == 3):
        executar = False


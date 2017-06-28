from Main import horasEmSegundos

class Bichinho():
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
import pygame
import random
import bichinho2_1
#Algumas variaveis
clock = pygame.time.Clock()
bichinhos = []
criar = True
ajudas = []

#Textos
pygame.font.init()
fontePadrao = pygame.font.SysFont("Segoe Script",25)
textoBt1 = fontePadrao.render("Novo Jogo", 1, (0,0,0))
textoBt2 = fontePadrao.render("Continuar", 1, (0,0,0))
textoBt3 = fontePadrao.render("Sair", 1, (0,0,0))

#Tamanho dos textos
txt1Width = textoBt1.get_width()
txt1Height = textoBt1.get_height()

txt2Width = textoBt2.get_width()
txt2Height = textoBt2.get_height()

txt3Width = textoBt3.get_width()
txt3Height = textoBt3.get_height()



# Cores:
cores = {}
cores["preto"] = (0,0,0)
cores["vermelho"] = (247,17,0)
cores["aquamarine"] = (127,255,212)

# Cores:
def RGBrandom ():
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)

    return (r,g,b)

#Imagens
#Imagens
rosto = pygame.image.load("imagens/rosto.png")
colorkey = rosto.get_at((0,0))
rosto.set_colorkey(colorkey)
fundoMenu = pygame.image.load("imagens/Teste2.png")

class menu ():

    def __init__ (self):
        pygame.init()
        pygame.display.set_caption("Tamagushy")
        self.tela = pygame.display.set_mode([800,600])

        self.tela.fill((255,255,255))

        #outtras configuraçoes


        continuar = True
        print("tudo")

        vx = 3
        vy = 2

        x = 400
        y = 300

        Bwidth = 100
        Bheight = 100

        corB = RGBrandom()

        while (continuar):

            #Detectar evento
            for event in pygame.event.get():
                if (event.type == pygame.QUIT ):
                    continuar = False

                elif (event.type == pygame.MOUSEBUTTONDOWN):
                    posicao = pygame.mouse.get_pos()
                    if (posicao[0] >= 350 and posicao[0] <= 500):
                        #Selecionando o botao
                        if(posicao[1] >= 150 and posicao[1] <= 200):
                            print("oi")

                        elif(posicao[1] >= 250 and posicao[1] <= 300):
                            print("Tudo")

                        elif (posicao[1] >= 350 and posicao[1] <= 400):
                            print("bom")









            self.tela.blit(fundoMenu,(0,0))
            global criar

            #Verificação de colisão com as extremidades da tela

            if (x < 50 or x > 750 ):
                vx = -vx
                corB = RGBrandom()
                corO = RGBrandom()
            if (y < 50 or y > 550):
                vy = -vy
                corB = RGBrandom()
                corO = RGBrandom()

            #Posiçoes
            x += vx
            y += vy

            bichinho2_1.bixo(x, y, Bwidth, Bheight, corB, self.tela, rosto)


            #Butoes


            self.bt1 = pygame.draw.rect(self.tela, cores["aquamarine"],[300,150,200,50])
            self.tela.blit(textoBt1,( 300 + 200 // 2 - txt1Width // 2 , 150 + 50 / 2 - txt1Height // 2))

            self.bt2 = pygame.draw.rect(self.tela, (102,205,170),[300,250,200,50])
            self.tela.blit(textoBt2, (300 + 200 // 2 - txt2Width // 2 , 250 + 50 // 2 - txt2Height // 2))


            self.bt3 = pygame.draw.rect(self.tela, cores["vermelho"],[300,350,200,50])
            self.tela.blit(textoBt3, (300 + 200 // 2 - txt3Width // 2, 350 + 50 // 2 - txt3Height // 2))




            pygame.display.update()
            clock.tick(60)
        quit()


m = menu()

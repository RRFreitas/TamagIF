import pygame
import random
import bichinho2_1


# Tela Principal






#Algumas variaveis
clock = pygame.time.Clock()
bichinhos = []
criar = True
ajudas = []

#Textos
pygame.font.init()
fontePadrao = pygame.font.SysFont("Segoe Script",25)
fonteTitulo = pygame.font.SysFont("Segoe Script", 90)
textoBt1 = fontePadrao.render("Novo Jogo", 1, (0,0,0))
textoBt2 = fontePadrao.render("Continuar", 1, (0,0,0))
textoBt3 = fontePadrao.render("Sair", 1, (0,0,0))
nomeJogo = fonteTitulo.render("Tamagushy",1 ,(0,0,0))


#Tamanho dos textos em pixels
txt1Width = textoBt1.get_width()
txt1Height = textoBt1.get_height()

txt2Width = textoBt2.get_width()
txt2Height = textoBt2.get_height()

txt3Width = textoBt3.get_width()
txt3Height = textoBt3.get_height()

nomeJogoWidth = nomeJogo.get_width()
nomeJogoHeight = nomeJogo.get_height()



# Cores:
cores = {}
cores["preto"] = (0,0,0)
cores["vermelho"] = (247,17,0)
cores["aquamarine"] = (127,255,212)
cores["red"] = (255,0,0)
cores["green"] = (0,255,0)
cores["blue"] = (0,0,255)

# Cor aleatória:
def RGBrandom ():
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)

    return (r,g,b)

#Imagens
rosto = pygame.image.load("imagens/rosto.png")
fundoMenu = pygame.image.load("imagens/Teste2.png")

pygame.init()
pygame.display.set_caption("Tamagushy")
tela = pygame.display.set_mode([800, 600])
newBd = None




def menu ():

    continuar = True
    newBd = None
    resposta = 0

    vx = 5
    vy = 3

    x = 400
    y = 300

    Bwidth = 100
    Bheight = 100

    corB = RGBrandom()
    corO = RGBrandom()

    while (continuar):

        #Detectar evento
        for event in pygame.event.get():



            if (event.type == pygame.QUIT ):
                continuar = False
                resposta = 3

            elif (event.type == pygame.MOUSEBUTTONDOWN):
                posicao = pygame.mouse.get_pos()
                if (posicao[0] >= 350 and posicao[0] <= 500):
                    #Selecionando o botao
                    if(posicao[1] >= 150 and posicao[1] <= 200):
                        newBd  = True
                        resposta = 1
                        continuar = False

                    elif(posicao[1] >= 250 and posicao[1] <= 300):
                        newBd = False
                        resposta = 2
                        continuar = False

                    elif (posicao[1] >= 350 and posicao[1] <= 400):
                        newBd = False
                        resposta = 3
                        continuar = False




        tela.blit(fundoMenu,(0,0))
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

        bichinho2_1.bixo(x, y, Bwidth, Bheight, corB, tela, rosto)


        #Butoes


        bt1 = pygame.draw.rect(tela, cores["aquamarine"],[300,150,200,50])
        tela.blit(textoBt1,( 300 + 200 // 2 - txt1Width // 2 , 150 + 50 / 2 - txt1Height // 2))

        bt2 = pygame.draw.rect(tela, (102,205,170),[300,250,200,50])
        tela.blit(textoBt2, (300 + 200 // 2 - txt2Width // 2 , 250 + 50 // 2 - txt2Height // 2))


        bt3 = pygame.draw.rect(tela, cores["vermelho"],[300,350,200,50])
        tela.blit(textoBt3, (300 + 200 // 2 - txt3Width // 2, 350 + 50 // 2 - txt3Height // 2))

        tela.blit(nomeJogo, (800 / 2 - nomeJogoWidth // 2, 150/2 - nomeJogoHeight //2))




        pygame.display.update()
        clock.tick(60)
    if resposta == 3:
        quit()
    return (newBd,resposta,tela,fontePadrao,cores,rosto)


#InterfaceTamagushy.executar()
menu()

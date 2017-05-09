import pygame
import bichinho2_1



fundoPrincipal = pygame.image.load("imagens/FundoPrincipal_azulClaro.png")
clock = pygame.time.Clock()

def newGAme(tela ,fontePrincipal,cores,rosto):
    #Algumas Variaveis importante
    pygame.init()
    clock = pygame.time.Clock()
    fundoPrincipal = pygame.image.load("imagens/FundoPrincipal_azulClaro.png")
    nome = ""
    text = fontePrincipal.render(nome, True, (0, 0, 0))
    escrever = False
    destaque = pygame.font.SysFont("arial",35)
    text1 = destaque.render("Digite o nome do seu Tamagushy:",True,(0,0,0))
    nomeOk = False
    corOk = False
    cor = None

    continuar = True

    while (continuar):
        # Verificando Eventos
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                continuar = False

            #Verificando posicao do click
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                if (corOk):
                    xm =  pygame.mouse.get_pos()[0]
                    ym =  pygame.mouse.get_pos()[1]
                    if (ym >= yc and ym <= yc + radio):
                        if (xm >= xc - radio//2 and xm <= xc + radio // 2):
                            cor = cores["red"]
                            corOk = True
                            continuar = False

                        if (xm >= xc + 150 - radio//2 and xm <= xc + radio//2 +150 ):
                            cor = cores["green"]
                            print("oi")
                            corOk = True
                            continuar = False


                        if (xm >= xc + 300 - radio//2 and xm <= xc + radio//2 +300):
                            cor = cores["blue"]
                            corOk = True
                            continuar = False

            #Entrada do nome do tamagif
            elif (event.type == pygame.KEYDOWN):



                if (nomeOk == False):
                    corOk = True
                    press = pygame.key.get_pressed()
                    for i in range(0, len(press)):
                        #print(i)
                        #print(pygame.key.name(i))
                        if (press[i] == 1):
                            if (len(nome )== 12):
                                if (i == 8):
                                    if (nome != ""):
                                        nome = list(nome)
                                        #print(nome)
                                        nome.pop()
                                        nome = "".join(nome)
                                        #print(nome)

                                else:
                                    fonte_aviso = pygame.font.SysFont("arial", 25)
                                    aviso = "O nome do seu bichinho só pode ter no maximo 12 Caracteres :)"
                                    txtAviso = fonte_aviso.render(aviso, True, (0, 0, 0))
                            else:
                                if (i == 8):
                                    if (nome != ""):
                                        nome = list(nome)
                                        #print(nome)
                                        nome.pop()
                                        nome = "".join(nome)
                                        #print(nome)

                                elif (i == 13):
                                    nomeOk = True

                                elif (i == 32):
                                    nome = " "

                                elif (i >= 97 and i <= 122):
                                    nome = nome + pygame.key.name(i)

                                else:
                                    fonte_aviso = pygame.font.SysFont("arial", 25)
                                    aviso = "Só são permitidas letras;)"
                                    txtAviso = fonte_aviso.render(aviso, True, (0, 0, 0))
                            text = fontePrincipal.render(nome,True,(0,0,0))








        text_width = text.get_width()
        text_height = text.get_height()
        tela.blit(fundoPrincipal, (0, 0))
        x = 400 - text_width // 2
        y = 100

        tela.blit(text, (x, y))
        tela.blit(text1,(190,10))

        caixa = pygame.draw.line(tela,(0,0,0),(x,y + text_height + 2), (x + text_width,y + text_height + 2 ))
        if (nomeOk):
            selecionarCor = fontePrincipal.render("Selecione a cor:",True,(0,0,0))
            tela.blit(selecionarCor,(300,y + text_height + 10))
            xc = 250
            yc = 250
            radio = 100
            bichinho2_1.bixo(xc, yc,radio,radio,cores["red"],tela,rosto)
            bichinho2_1.bixo(xc + 150, yc,radio,radio,cores["green"],tela,rosto)
            bichinho2_1.bixo(xc + 300, yc,radio,radio,cores["blue"],tela,rosto)

            bt1 = pygame.draw.rect(tela,(255,0,0),(xc - 50,yc + radio + 10,100,25))
            bt2 = pygame.draw.rect(tela,(0,255,0),(xc + 100,yc + radio + 10, 100,25))
            bt3 = pygame.draw.rect(tela,(0,0,255),(xc + 250,yc + radio + 10,100,25))

            fonteTest = pygame.font.SysFont("Segoe Script",15)
            textBts = fonteTest.render("Selecionar", True,(0,0,0))
            tela.blit(textBts,(210,312))
            tela.blit(textBts,(360,312))
            tela.blit(textBts,(510,312))


        pygame.display.update()
        clock.tick(60)
    return (nome,cor)

import pygame
import bichinho2_1


fundoPrincipal = pygame.image.load("imagens/FundoPrincipal_azulClaro.png")
clock = pygame.time.Clock()
escolha = None
pygame.font.init()
fonte = pygame.font.SysFont("Segoe Script", 19)

text1 = ("Alterar o"
         " nome")
text2 = ("Dar"
         " Comida")

text3 = ("Dar"
         " Remedio")

text4 = ("Mini Game")

text5 = ("Fome")

text6 = ("Saude")

text7 = ("Idade :")


def janelaPrincipal(tela,rosto,fontePadrao,animal):
    clock = pygame.time.Clock()
    continuar = True
    fundoPrincipal = pygame.image.load("imagens/FundoPrincipal_azulClaro.png")
    print("ds")
    sair = False

    nome = animal.getNome()
    fome = animal.getFome()
    saude = animal.getSaude()
    idade = animal.getIdade()
    cor = animal.getCor()



    textNome = fonte.render(nome,True,(0,0,0))
    textNomeW = textNome.get_width()


    #Textos dos butoes
    txtbt1 = fonte.render(text1, True, (0, 0, 0))
    txtbt1W = txtbt1.get_width()
    txtbt1H = txtbt1.get_height()



    txtbt2 = fonte.render(text2,True,(0,0,0))
    txtbt2W = txtbt2.get_width()
    txtbt2H = txtbt2.get_height()

    txtbt3 = fonte.render(text3,True,(0,0,0))
    txtbt3W = txtbt3.get_width()
    txtbt3H = txtbt3.get_height()

    txtbt4 = fonte.render(text4, True, (0, 0, 0))
    txtbt4W = txtbt2.get_width()
    txtbt4H = txtbt2.get_height()

    #Textos de informaçoes do Tamagif
    txtF = fonte.render(text5, True, (0, 0, 0))
    txtFW = txtF.get_width()
    txtFH = txtF.get_height()

    txtS = fonte.render(text6, True, (0, 0, 0))
    txtSW = txtS.get_width()
    txtSH = txtS.get_height()


    txtI = fonte.render(text7, True, (0, 0, 0))
    txtIW = txtI.get_width()
    txtIH = txtI.get_height()

    escolha = 0


    while (continuar):
        idadeSTR = str(idade)
        idadetxt = fonte.render(idadeSTR,True,(0,0,0))
        # Verificando Eventos
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                sair = True
                continuar = False
                escolha = 5
                
                print("ELe fdfd")


            elif (event.type == pygame.MOUSEBUTTONDOWN):
                if not escolha == 1:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if (x >= 10 and x <= 160):
                        if (y >= 100 and y <= 150):
                            escolha = 1

                        elif (y >= 200 and y <= 250):
                            escolha = 2



                    elif (x >= 640 and x <= 790):
                        if (y >= 100 and y <= 150):
                            escolha = 3
                            continuar = False

                        elif (y >= 200 and y <= 250):
                            escolha = 4
                            continuar = False


            if (event.type == pygame.KEYDOWN):

                if (escolha == 1):
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
                                    escolha = 0

                                elif (i == 32):
                                    nome = " "

                                elif (i >= 97 and i <= 122):
                                    nome = nome + pygame.key.name(i)

                                else:
                                    fonte_aviso = pygame.font.SysFont("arial", 25)
                                    aviso = "Só são permitidas letras;)"
                                    txtAviso = fonte_aviso.render(aviso, True, (0, 0, 0))
                            text = fonte.render(nome,True,(0,0,0))


        fome = animal.getFome()
        saude = animal.getSaude()
        idade = animal.getIdade()
        cor = animal.getCor()


        tela.blit(fundoPrincipal, (0, 0))

        textNome = fontePadrao.render(nome, True, (0, 0, 0))
        textNomeW = textNome.get_width()
        tela.blit(textNome,(400 - textNomeW//2,10))

        h = ((idade // 2) * 10) + 50
        w = h - (100 - fome)



        bichinho2_1.bixo(400 ,320,w,h,cor,tela,rosto)
        bt1 = pygame.draw.rect(tela, (204, 255, 255), (10, 100, 150, 50))
        tela.blit(txtbt1,(12 +75 - txtbt1W // 2, 100 + 25 - txtbt1H //2 ))

        bt2 = pygame.draw.rect(tela, (204, 255, 255), (10, 200, 150, 50))
        tela.blit(txtbt2, (12 + 75 - txtbt1W // 2, 200 + 25 - txtbt1H // 2))

        bt3 = pygame.draw.rect(tela, (204, 255, 255), (640, 100, 150, 50))
        tela.blit(txtbt3, (642 + 75 - txtbt1W // 2, 100 + 25 - txtbt1H // 2))

        bt4 = pygame.draw.rect(tela, (204, 255, 255), (640, 200, 150, 50))
        tela.blit(txtbt4,(642 + 75 - txtbt1W // 2, 200 + 25 - txtbt1H // 2))

        tela.blit(txtF,(9,539))
        barraFome1 = pygame.draw.rect(tela,(255,255,255),(9 +txtFW ,539,102,22),1)
        barraFome2 = pygame.draw.rect(tela, (0, 255, 0), (10 + txtFW, 540, fome, 20))

        tela.blit(txtS,(300,539))
        barraSaude1 = pygame.draw.rect(tela, (255, 255, 255), (300 + txtSW  , 539, 102, 22), 1)
        barraSaude2 = pygame.draw.rect(tela, (0, 255, 0), (301 + txtSW  , 540, saude, 20))

        tela.blit(txtI, (600, 539))
        idadeSTR = str(idade)
        idadetxt = fonte.render(idadeSTR,True,(0,0,0))
        tela.blit(idadetxt,(670,539))


        if escolha == 2:
            comidas = 0
            mais = pygame.draw.rect(tela,(255,0,0),(425 - w - 50 ,327 ,20,30))
            menos = pygame.draw.rect(tela,(255,255,0),(425 + w//2 + 10,327,20,30))



        pygame.display.update()
        clock.tick(60)
    fome = animal.getFome()
    saude = animal.getSaude()
    idade = animal.getIdade()
    cor = animal.getCor()

     if (sair):
            escolha = 5
            return escolha
    print(escolha,nome,saude,fome,idade)
    return (escolha,nome,saude,fome,idade)

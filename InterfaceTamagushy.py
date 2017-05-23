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
    fome = animal.getFome(50)
    saude = animal.getSaude(50)
    idade = animal.getIdade(50)




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
    escolha2 = False
    escolha3 = False
    escolha4 = False
    minigame = 0
    comida = 0
    pilulas = 0

    corf = (0,255,0)
    cors = (0, 255, 0)


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
                if not escolha == 1 or not escolha2 or not escolha3:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if (x >= 10 and x <= 160):
                        if (y >= 100 and y <= 150):
                            escolha = 1

                        elif (y >= 200 and y <= 250):
                            escolha = 2
                            escolha2 = True



                    elif (x >= 640 and x <= 790):
                        if (y >= 100 and y <= 150):
                            escolha = 3
                            escolha3 = True

                        elif (y >= 200 and y <= 250):
                            escolha = 4
                            escolha4 = True

                if escolha2:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if y >= 330 and y <= 350:
                        if x >= (400 - w ) and x <= (400 - w) + 20:
                            if comidas > 0:
                                fome = animal.setFome(1)
                                comidas = animal.getComidas(True)


                    if y >= 300 + w and y <= 300 + w + 30:
                        if x >= 300 and x <= 500:
                            escolha2 = False




                #Caso a opção escolhda seja mdicar verificar onde  clicou
                if escolha3:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if y >= 330 and y <= 350:
                        if x >= (400 - w ) and x <= (400 - w) + 20:
                            if pilulas > 0:
                                saude = animal.setSaude(1)
                                animal.getPilulas(True)

                    if y >= 300 + w and y <= 300 + w + 30:
                        if x >= 300 and x <= 500:
                            escolha3 = False
                        

                if escolha4:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if (y >= 300 and y <= 350):
                        if(x >= 20 and x <= 220 ):
                            escolha = 4
                            minigame = 1
                            continuar = False

                        elif(x >= 580 and x <= 780):
                            escolha = 4
                            minigame = 2
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

        fome = animal.getFome(fome)
        saude = animal.getSaude(saude)
        idade = animal.getIdade(idade)
        recordJG1 = animal.getRecordJG1(0)
        recordJG2 = animal.getRecordJG2(0)
        comidas = animal.getComidas(False)
        pilulas = animal.getPilulas(False)
        corauxiliar = animal.getCor()
        r = corauxiliar[0]
        g = corauxiliar[1]
        b = corauxiliar[2]

        if (fome <= 0 or saude <= 0):
            print("TESTE#$")
            print("Game Over")
            escolha = 6
            continuar = False

        if (r == 255):
            for n in range(0,(100 - saude)):
                if g < 255.0:
                    g += 2.5
                if b < 255.0:
                    b += 2.5

        if (g == 255):
            for n in range(0, (100 - saude)):
                if r < 255.0:
                    r += 2.5
                if b < 255.0:
                    b += 2.5

        if (b == 255):
            for n in range(0, (100 - saude)):
                if r < 255.0:
                    r += 2.5
                if g < 255.0:
                    g += 2.5

        cor = (r,g,b)

        tela.blit(fundoPrincipal, (0, 0))

        textNome = fontePadrao.render(nome, True, (0, 0, 0))
        textNomeW = textNome.get_width()
        tela.blit(textNome,(400 - textNomeW//2,10))

        h = ((idade // 2) * 10) + 50
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

        #Selecionando a cor da barra de fome e saude
        if (fome >=75):
            corf = (0,255,0)
        elif (fome >= 50 and fome <=74):
            corf = (255,215,0)
        elif (fome >= 25 and fome <= 49):
            corf = (255,140,0)
        elif (fome >=0 and fome <= 24):
            corf = (255,2,1)

        if (saude >=75):
            cors = (0,255,0)
        elif (saude >= 50 and saude <=74):
            cors = (255,215,0)
        elif (saude >= 25 and saude <= 49):
            cors = (255,140,0)
        elif (saude >=0 and saude <= 24):
            cors = (255,2,1)


        barraFome1 = pygame.draw.rect(tela,(0,0,0),(9 +txtFW ,539,102,22),1)
        barraFome2 = pygame.draw.rect(tela, corf, (10 + txtFW, 540, fome, 20))

        tela.blit(txtS,(300,539))
        barraSaude1 = pygame.draw.rect(tela, (0, 0, 0), (300 + txtSW  , 539, 102, 22), 1)
        barraSaude2 = pygame.draw.rect(tela, cors, (301 + txtSW  , 540, saude, 20))

        tela.blit(txtI, (600, 539))
        idadeSTR = str(idade)
        idadetxt = fonte.render(idadeSTR,True,(0,0,0))
        tela.blit(idadetxt,(670,539))


        if escolha2:

            textF1 = fontePadrao.render("+",True,(0,0,0))
            textF2 = fontePadrao.render("-", True, (0, 0, 0))
            textF3 = fonte.render("Alimentar",True,(0,0,0))
            #Quantidade de comidas
            textF4 = fonte.render(str(comida),True,(0,0,0))
            textF4W = textF4.get_width()

            mais = pygame.draw.rect(tela,(255,0,0),(400 - w  ,330 ,20,20))
            tela.blit(textF1,(400 - w + 2,319))
            menos = pygame.draw.rect(tela,(255,255,0),(400 + w ,330,20,20))
            tela.blit(textF2, (400 + w , 320))
            comidaok = pygame.draw.rect(tela,(255,255,255),(300,300 + w,200,30))
            tela.blit(textF3,(350,300 + w))
            tela.blit(textF4,(400 - textF4W //2,330 + w))
            print(comida)

        #Dar Remedio
        if escolha3:

            textS1 = fontePadrao.render("+",True,(0,0,0))
            textS2 = fontePadrao.render("-", True, (0, 0, 0))
            textS3 = fonte.render("Medicar",True,(0,0,0))
            #Quantidade de pilulas
            textS4 = fonte.render(str(pilulas),True,(0,0,0))
            textS4W = textS4.get_width()

            mais = pygame.draw.rect(tela,(255,0,0),(400 - w  ,337 ,20,20))
            tela.blit(textS1,(400 - w + 2,328))
            menos = pygame.draw.rect(tela,(255,255,0),(400 + w ,330,20,20))
            tela.blit(textS2, (400 + w , 328))
            pilulasok = pygame.draw.rect(tela,(255,255,255),(300,300 + w,200,30))
            tela.blit(textS3,(350,300 + w))
            tela.blit(textS4,(400 - textS4W //2,320 + w))
            print(pilulas)

        if escolha4:
            #MG = Minigames
            tela.blit(fundoPrincipal,(0,0))
            textMG1 = fontePadrao.render("tiro ao alvo",True,(0,0,0))
            textMG1W = textMG1.get_width()
            textMG1H = textMG1.get_height()
            textMG2 = fontePadrao.render("Desviando",True,(0,0,0))
            textMG2W = textMG2.get_width()
            textMG2H = textMG2.get_height()

            #Titulo
            textJogos = fontePadrao.render("Mini Games",True,(0,0,0))
            textJogosW = textJogos.get_width()
            tela.blit(textJogos,(400 - textJogosW // 2,10))

            #Desenhando butões
            bt1 = pygame.draw.rect(tela,(0,0,255),(20,300,200,50))
            bt2 = pygame.draw.rect(tela,(0,0,255),(580,300,200,50))


            #Digitando texto nos butoes
            tela.blit(textMG1,((100 - textMG1W // 2) + 20, 325 - textMG1H // 2))
            tela.blit(textMG2, ((100 - textMG2W // 2) + 580, 325 - textMG1H // 2))



        pygame.display.update()
        clock.tick(60)



    return (escolha,nome,idade,fome,saude,cor,minigame,recordJG1,recordJG2,comidas)

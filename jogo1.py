import random

def RGBrandom ():
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)

    return (r,g,b)

pygame.init()
tela = pygame.display.set_mode([800,600])
clock = pygame.time.Clock()
rost = pygame.image.load("imagens/rosto.png")


fundo = pygame.image.load("imagens/fundoPrincipal.png")





def jogoNave():
    continuar = True
    x = 400
    pressionadoR = False
    pressionadoL = False
    yb = 490
    xb = None
    novoTiro = False
    balas = 5
    atirou = False
    atirados = []
    atirados_auxiliar = []

    while(continuar):
        tela.blit(fundo, (0, 0))

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                continuar = False

            elif(event.type == pygame.KEYDOWN):
                pressed_keys = pygame.key.get_pressed()

                if pressed_keys[pygame.K_LEFT]:

                    pressionadoL = True
                if pressed_keys[pygame.K_RIGHT]:
                    pressionadoR = True

                if pressed_keys[pygame.K_SPACE]:
                    if (balas > 0):
                        novoTiro = True
                    atirou = True



            elif(event.type == pygame.KEYUP):
                pressed_keys = pygame.key.get_pressed()

                if not pressed_keys[pygame.K_LEFT]:
                    pressionadoL = False
                if not pressed_keys[pygame.K_RIGHT]:
                    pressionadoR = False



        if (pressionadoL):
            if (x - 7 >= 50):
                x -= 7
        if (pressionadoR):
            if (x + 7 <= 750):
                x += 7
        if (atirou):
            if balas > 0 and novoTiro:
                xb = x
                yb = 490
                pos = (xb,yb)
                atirados.append(pos)
                balas -=1
                novoTiro = False
                print("0",atirados)

            atirados_auxiliar = atirados.copy()
            atirados.clear()
            print("1",atirados)
            print("2",atirados_auxiliar)

            for pos in atirados_auxiliar:
                bala = pygame.draw.circle(tela, RGBrandom(), pos, 10)
                yb = pos[1] - 10
                xb = pos[0]
                pos = (xb, yb)
                print("3",atirados_auxiliar)
                atirados.append(pos)
                print("4",atirados)



                if yb <= 10:
                    balas += 1
                    atirados.pop()

            if atirados == []:
                atirou = False

        xtiros = 782

        for n in range(0,balas):
            bala = pygame.draw.circle(tela, RGBrandom(), (xtiros,580), 10)
            xtiros -= 20


        bichinho2_1.bixo(x,490,100,100,(255,235,2),tela,rost)
        pygame.display.update()
        clock.tick(60)



jogoNave()

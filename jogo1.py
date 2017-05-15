import random
import pygame
import bichinho2_1
import time

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
natela = []
atingiu = False

bala = 1


def fase(inimigos,w,h,cor,atirados,wUsuario,hUsusario,xUsuario,vidas,vi,vb):


    natela_a = natela.copy()
    natela.clear()
    global bala
    global atingiu

    for n,vi,xbala,ybala in natela_a:


        if atirados == []:
            atirou = False


        if (n >=0 and n <= 800 - w):
            vi = vi

        else:
            vi = -vi


        x = n + vi

        if x >= 0 and x <=800:
            print("DEsenhou",w,h)
            inimigo1 = pygame.draw.rect(tela, cor, (x, 10, w, h))

        tiro = pygame.draw.circle(tela,(0,0,0),(xbala,ybala + h),5)
        ybala += vb





        for xb,yb in atirados:
            if (xb >= x  and xb <= x + w):
                if (yb  >=  10 and yb <= 30  ):
                    print("vai tirar")
                    x =  - 100


        if ybala >= 490 and ybala <= 490 + h:
            if xbala >= xUsuario - wUsuario//2 and xbala <= xUsuario + wUsuario//2:
                vidas -= 1
                atingiu = True

        if atingiu:
            xbala = x
            ybala = 10
            atingiu = False



        if ybala > 490 + h + 12:
            ybala = 10
            xbala = x


        natela.append((x, vi, xbala, ybala))

        if x < 0 and ybala >= 490 + h + 10:
            natela.pop()

    if len(natela) <= 1:
        contador = 5
        print("Oi")
        while(contador >=0):
            print("eeee")
            x = random.randint(0, 700)
            if  inimigos !=[]:
                print("iiiii")
                inimigos.pop()
                vi = vi
                xbala = x
                ybala = 10
                natela.append((x,vi,xbala,ybala))
            contador -=1


    print(natela)
    if natela == [] and inimigos == []:
        return (True,vidas)




    return (False,vidas)





def jogoNave(cor,w,h,fontePadrao,idade):
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
    fase1 = True
    inimigos1 = list(range(0, 5))
    fase2 = False
    inimigos2 = list(range(0,10))
    fase3 = False
    inimigos3 = list(range(0,20))
    vidas = idade + 1
    auxiliar = 2

    #Variaveis dos inimigos
    wi = 100
    hi = 20
    cori = RGBrandom()
    vi = 2
    vbi = 1
    numero = 1


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
                bala = pygame.draw.circle(tela, RGBrandom(), pos, w // 10)
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

        resposta =fase(inimigos1,wi,hi,cori,atirados,w,h,x,vidas,vi,vbi)
        vidas = resposta[1]
        if resposta[0] == True:
            inimigos1 = list(range(0,auxiliar * 5))
            auxiliar += 1
            wi -=10
            hi -= 2
            cori = RGBrandom()
            vi += 2
            vbi += 1
            numero += 1
            print("EEEEEIIIII")

        numeroFase = str(numero)

        faseN = "FASE:  " + numeroFase

        if vidas < 1:
            print("Game Over")
            continuar = False

        informarVidas = "Vidas: " + str(vidas)

        fontePrincipaJ1 = pygame.font.SysFont("Verdana",25)
        textFase = fontePadrao.render(informarVidas,True,(0,0,0))
        tela.blit(textFase,(10,550))
        textVidas = fontePrincipaJ1.render(faseN,True,(0,0,0))
        textVidasW = textVidas.get_width()
        tela.blit(textVidas,(400 - textVidasW//2,550))

        bichinho2_1.bixo(x,490,w,h,cor,tela,rost)


        pygame.display.update()
        clock.tick(60)
    escolha4 = False
    minigame = 0
    return (escolha4,minigame)





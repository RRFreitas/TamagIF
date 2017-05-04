import pygame
import bichinho2_1
from MenuTamagushy import RGBrandom

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
    atirou = False

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
                    if not atirou:
                        xb = x
                        yb = 490
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
            balas = pygame.draw.circle(tela, RGBrandom(), (xb, yb),10)
            yb -= 5

            if yb <= 10:
                atirou = False

        bichinho2_1.bixo(x,490,100,100,(255,235,2),tela,rost)
        pygame.display.update()
        clock.tick(60)



jogoNave()

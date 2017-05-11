import random
import pygame
import bichinho2_1
import math

def RGBrandom ():
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)

    return (r,g,b)

pygame.init()
tela = pygame.display.set_mode([800,600])
clock = pygame.time.Clock()

pontos = 0

fonte = pygame.font.SysFont("Segoe Script", 15)
textoVida = fonte.render("Vida:", 1, (0,0,0))
textoW = textoVida.get_width()
textoPontos = fonte.render("Pontos: " + str(pontos), 1, (0,0,0))

rost = pygame.image.load("imagens/rosto.png")
fundo = pygame.image.load("imagens/fundoPrincipal.png")
natela = []

vidas = 5
x = 400

execTime = 0

continuar = True

def drawPoly(type, x, y, color):
    if type == 1:
        pygame.draw.rect(tela, color, (x, y, 50, 50)) #Desenhar quadrado
    if type == 2:
        pygame.draw.circle(tela, color, (x, y), 50) #Desenhar círculo
    if type == 3:
        pygame.draw.polygon(tela, color, ((x, y), (x + 50, y), (x + 25, y - 50))) #Desenhar triângulo

def randomPolygon():
    return [random.randint(1, 3), random.randint(50, 750), 0, RGBrandom()]

def checkColision():
    global vidas
    global pontos

    for i in range(0, len(natela) - 1):
        if(natela[i][2] >= 600):
            pontos += 1
            natela.pop(i)
            return

        if(natela[i][0] == 1): #Calcula colisão quadrado-círculo
            if(natela[i][1] < x - 50 < natela[i][1] + 50 or natela[i][1] < x + 50 < natela[i][1] + 50 or x - 50 < natela[i][1] < natela[i][1] + 50 < x + 50):
                if(440 > natela[i][2] + 50 > 540 or 440 < natela[i][2] < 540):
                    if (vidas > 0):
                        vidas -= 1
                    natela.pop(i)
        elif(natela[i][0] == 2): #Calcula colisão circulo-circulo
            distanciaX = math.fabs(x - natela[i][1])
            distanciaY = math.fabs(490 - natela[i][2])
            distancia = math.sqrt((distanciaX * distanciaX) + (distanciaY * distanciaY))
            distanciaMinima = 100

            if(distancia < distanciaMinima):
                if(vidas > 0):
                    vidas -= 1
                natela.pop(i)
        else: #Calcula colisão triângulo-círculo
            if (natela[i][1] < x - 50 < natela[i][1] + 50 or natela[i][1] < x + 50 < natela[i][1] + 50 or x - 50 < natela[i][1] < natela[i][1] + 50 < x + 50):
                if (440 > natela[i][2] > 540 or 440 < natela[i][2] - 5 < 540):
                    if (vidas > 0):
                        vidas -= 1
                    natela.pop(i)
def update():
    global tela
    global vidas
    global continuar

    if vidas == 0:
        continuar = False

    if(execTime % 12 == 0): #A cada 12 no contador, adicionar novo polígono
        natela.append(randomPolygon())

    for i in range(0, len(natela) - 1):
        drawPoly(natela[i][0], natela[i][1], natela[i][2], natela[i][3])
        natela[i][2] += 10 + execTime // 20

    tela.blit(textoVida, (10, 570))
    pygame.draw.rect(tela, (255, 255, 255), (15 + textoW, 570, 200, 20), 1)
    if vidas >= 4:
        pygame.draw.rect(tela, (0, 255, 0), (15 + textoW, 570, 200 * (vidas / 5), 20))
    elif vidas >=2:
        pygame.draw.rect(tela, (255, 235, 2), (15 + textoW, 570, 200 * (vidas / 5), 20))
    else:
        pygame.draw.rect(tela, (255, 0, 0), (15 + textoW, 570, 200 * (vidas / 5), 20))

    textoPontos = fonte.render("Pontos: " + str(pontos), 1, (0, 0, 0))
    tela.blit(textoPontos, (10, 10))

    checkColision()

def jogo2():
    pressionadoR = False
    pressionadoL = False

    global continuar

    while (continuar):
        global execTime
        execTime +=1

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
            elif(event.type == pygame.KEYUP):
                pressed_keys = pygame.key.get_pressed()

                if not pressed_keys[pygame.K_LEFT]:
                    pressionadoL = False
                if not pressed_keys[pygame.K_RIGHT]:
                    pressionadoR = False

        global x

        if (pressionadoL):
            if (x - 10 >= 50):
                x -= 10 + execTime // 30
        if (pressionadoR):
            if (x + 10 <= 750):
                x += 10 + execTime // 30

        bichinho2_1.bixo(x, 490, 100, 100, (255, 235, 2), tela, rost)
        update()
        pygame.display.update()
        clock.tick(60)

#jogo2()
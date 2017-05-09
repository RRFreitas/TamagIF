import pygame
import bichinho2_1


fundoPrincipal = pygame.image.load("imagens/FundoPrincipal_azulClaro.png")
clock = pygame.time.Clock()
escolha = None

def janelaPrincipal(tela,rosto):
    clock = pygame.time.Clock()
    continuar = True
    sair = False
    fundoPrincipal = pygame.image.load("imagens/FundoPrincipal_azulClaro.png")
    print("ds")
    while (continuar):

        # Verificando Eventos
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                sair = True
                continuar = False



            elif (event.type == pygame.MOUSEBUTTONDOWN):
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if (x >= 10 and x <= 160):
                    if (y >= 100 and y <= 150):
                        escolha = 1
                        continuar = False
                    elif (y >= 200 and y <= 250):
                        escolha = 2
                        continuar = False

                elif (x >= 640 and x <= 790):
                    if (y >= 100 and y <= 150):
                        escolha = 3
                        continuar = False

                    elif (y >= 200 and y <= 250):
                        escolha = 4
                        continuar = False




        tela.blit(fundoPrincipal, (0, 0))
        bichinho2_1.bixo(400,300,50,50,(255,255,255),tela,rosto)
        bt1 = pygame.draw.rect(tela, (204, 255, 255), (10, 100, 150, 50))
        bt2 = pygame.draw.rect(tela, (204, 255, 255), (10, 200, 150, 50))
        bt3 = pygame.draw.rect(tela, (204, 255, 255), (640, 100, 150, 50))
        bt4 = pygame.draw.rect(tela, (204, 255, 255), (640, 200, 150, 50))

        pygame.display.update()
        clock.tick(60)
    if (sair):
        escolha = 5
    return escolha

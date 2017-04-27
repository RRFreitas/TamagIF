import pygame

bicho = []
def bixo(x, y, w, h, corB, corO, superficie, rosto):

    b = pygame.draw.ellipse(superficie, corB, (x - w//2, y - h//2, w, h), h//2)
    #olhod = pygame.draw.circle(superficie,corO,(x + 19,y - 10),10)
    #olhoe = pygame.draw.circle(superficie,corO,(x - 18,y - 10),10)

    superficie.blit(rosto, (x - 32.5, y - 32.5))

    bicho.append((b))
    return bicho

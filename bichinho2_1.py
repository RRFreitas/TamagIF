import pygame

bicho = []
def bixo(x, y, w, h, corB, superficie, rosto):

    if(w > h):
        b = pygame.draw.ellipse(superficie, corB, (x - w // 2, y - h // 2, w, h), h // 2)
    else:
        b = pygame.draw.ellipse(superficie, corB, (x - w // 2, y - h // 2, w, h), w // 2)


    superficie.blit(rosto, (x - 32.5, y - 32.5))

    bicho.append((b))
    return bicho

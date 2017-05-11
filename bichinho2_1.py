import pygame

bicho = []
def bixo(x, y, w, h, corB, superficie, rosto):

    b = pygame.draw.ellipse(superficie, corB, (x - w // 2, y - h // 2, w, h), 0)
    superficie.blit(rosto, (x - rosto.get_width() / 2, y - rosto.get_height() / 2))

    bicho.append((b))
    return bicho

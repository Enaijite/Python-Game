import pygame
from Settings import*

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('Rock.png').convert_alpha()
        self.image.set_colorkey(GREEN)
        self.rect = self.image.get_rect(topleft = pos)

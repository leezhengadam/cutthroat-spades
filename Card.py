import pygame
from Utilities import load_image


class Card(pygame.sprite.Sprite):
    def __init__(self, suit, value):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.suit = suit
        self.value = value
        self.image, self.rect = load_image('images/card-back.jpg', -1)

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

    def set_position(self, x, y):
        self.rect.midtop = (x, y)

    def flip_card(self):
        filename = 'images/card_images/' + self.value + '_of_' + self.suit + '.jpg'
        self.image, self.rect = load_image(filename, (20,60,20,0))




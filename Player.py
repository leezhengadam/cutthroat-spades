import Card
import pygame
from Utilities import load_image, suits, values


class Player():
    def __init__(self, location, background):
        self.bid = 0
        self.tricks_won = 0
        self.cards = []
        self.location = location
        self.num_cards = 0
        self.background = background
        self.playerIcon = PlayerIcon(location, background)

    def assign_card(self, card):
        if self.num_cards < 13:
            self.cards.append(card)
            self.num_cards += 1
            return True
        else:
            return False

    def set_card_locations(self):
        if self.location == 'N':
            x = 520
            for card in self.cards:
                card.set_position(x,130)
                x += 20

        elif self.location == 'W':
            y = 240
            for card in self.cards:
                card.set_position(180, y)
                y += 20

        elif self.location == 'E':
            y = 240
            for card in self.cards:
                card.set_position(1100, y)
                y += 20

        elif self.location == 'S':
            self.sort_cards()
            x = 90
            for card in self.cards:
                card.flip_card()
                card.set_position(x, 680)
                x += 90

    def sort_cards(self):
        new_cards = []
        for suit in suits:
            for value in values:
                for card in self.cards:
                    if card.suit == suit and card.value == value:
                        new_cards.append(card)
        self.cards = new_cards


class PlayerIcon(pygame.sprite.Sprite):
    def __init__(self, location, background):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.image, self.rect = load_image('images/person-icon.png', -1)
        self.location = location
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

        # display labels and icons
        font = pygame.font.Font(None, 36)
        if location == 'N':
            self.rect.midtop = background.get_width() / 2, 10
            text = font.render("Tim", 1, (255, 255, 255))
            textpos = text.get_rect(centerx=background.get_width() / 2, centery=100)
            background.blit(text, textpos)
        elif location == 'S':
            self.rect.midbottom = 650, 950
            text = font.render("Mark", 1, (255, 255, 255))
            textpos = text.get_rect(centerx=background.get_width() / 2, centery=background.get_height() - 130)
            background.blit(text, textpos)
        elif location == 'W':
            self.rect.midleft = 10, 480
            text = font.render("Gary", 1, (255, 255, 255))
            textpos = text.get_rect(centerx=35, centery=background.get_height() / 2 + 50)
            background.blit(text, textpos)
        elif location == 'E':
            self.rect.midright = 1290, 480
            text = font.render("Sam", 1, (255, 255, 255))
            textpos = text.get_rect(centerx=background.get_width() - 40, centery=background.get_height() / 2 + 50)
            background.blit(text, textpos)


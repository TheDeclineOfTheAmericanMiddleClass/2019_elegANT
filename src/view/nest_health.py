import pygame
from view_element import ViewElement


class Nest_health(ViewElement):

    def __init__(self, view, identifier, x, y, width, height):
        super(Nest_health, self).__init__(view, identifier, x, y, width, height)
        # self.color = color
        self.width = width
        self.height = height
        # self.rect = pygame.Rect(x, y, width, height)
        self.surf.fill((0, 0, 0))
        self.surf = pygame.Surface((100, 20))
        self.health = 100

    def draw(self):

        #Elements of health bar
        pygame.draw.rect(self.surf, RED, [x, y, width, height], 3)
        pygame.draw.rect(self.surf, GREEN, [x, y, width - (5*(100-self.health)), height]) # counts down by 5 hit points

    def event_handler(self, event):
        if self.health > 0:
            if "hit" in self.events:
                for fnct, args in self.events["hit"]:
                    fnct(**args)

    def click_event(self):
        pass

class Button:

    def __init__(self, color, pygame, window, position, image_path, press_image_path):
        self.position = position
        self.color = color
        self.image = pygame.image.load(image_path)
        self.press_image = pygame.image.load(press_image_path)
        self.image_area = self.image.get_rect(x = self.position[0], y = self.position[1])
        window.blit(self.image, self.image_area)
        pygame.display.update()

    def Press(self, pygame, window):
        pygame.draw.rect(window, self.color, self.position)
        window.blit(self.press_image, self.image_area)
        pygame.display.update()

    def NoPress(self, pygame, window):
        pygame.draw.rect(window, self.color, self.position)
        window.blit(self.image, self.image_area)
        pygame.display.update()
class Wall:

    def __init__(self, outline_width, color, number, variables, canvas_height, user_x1, user_y1, user_x2, user_y2):

        self.width = outline_width
        self.color = color
        self.number = number
        self.user_x1 = user_x1
        self.x1 = int(self.user_x1 / variables.units_per_pixel_x)
        self.user_y1 = user_y1
        self.y1 = int((canvas_height * variables.units_per_pixel_y - self.user_y1) / variables.units_per_pixel_y)
        self.user_x2 = user_x2
        self.x2 = int(self.user_x2 / variables.units_per_pixel_x)
        self.user_y2 = user_y2
        self.y2 = int((canvas_height * variables.units_per_pixel_y - self.user_y2) / variables.units_per_pixel_y)

    def Draw(self, canvas, pygame):
        pygame.draw.line(canvas, self.color, (self.x1, self.y1), (self.x2, self.y2), self.width)
        pygame.draw.rect(canvas, self.color, (self.x1 - self.width, self.y1 - self.width,
                                              self.width * 2, self.width * 2))
        pygame.draw.rect(canvas, self.color, (self.x2 - self.width, self.y2 - self.width,
                                              self.width * 2, self.width * 2))
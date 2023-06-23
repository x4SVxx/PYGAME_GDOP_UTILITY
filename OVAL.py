class Oval:

    def __init__(self, outline_width, color, number, variables, canvas_height, user_x, user_y, user_width, user_height):

        self.outline_width = outline_width
        self.color = color
        self.number = number
        self.user_x = user_x
        self.x = int(self.user_x / variables.units_per_pixel_x)
        self.user_width = user_width
        self.width = int(self.user_width / variables.units_per_pixel_x)
        self.user_y = user_y
        self.y = int((canvas_height * variables.units_per_pixel_y - self.user_y) / variables.units_per_pixel_y)
        self.user_height = user_height
        self.height = int(self.user_height / variables.units_per_pixel_y)

    def Draw(self, canvas, pygame):
        pygame.draw.ellipse(canvas, self.color, (self.x, self.y, self.width, self.height), self.outline_width)
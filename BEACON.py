class Beacon:

    def __init__(self, radius, color, number, ID, variables, canvas_height, user_x, user_y):
        self.radius = radius
        self.color = color
        self.number = number
        self.ID = ID
        self.user_x = str(round(float(user_x), 2))
        self.x = int(float(self.user_x) / variables.units_per_pixel_x)
        self.user_y = str(round(float(user_y), 2))
        self.y = int((canvas_height * variables.units_per_pixel_y - float(self.user_y)) / variables.units_per_pixel_y)

    def Draw(self, canvas, pygame, canvas_width, canvas_height):
        pygame.draw.circle(canvas, self.color, (self.x, self.y), self.radius)

        font = pygame.font.SysFont('ebrima', 12)
        beacon_ID_text = font.render(self.ID, True, (0, 0, 0))
        beacon_ID_text_place = beacon_ID_text.get_rect(center=(self.x, self.y - self.radius))
        beacon_ID_text_place.y = self.y - self.radius - beacon_ID_text_place.height
        if beacon_ID_text_place.y <= 0: beacon_ID_text_place.y = self.y + self.radius - 4
        if beacon_ID_text_place.y + beacon_ID_text_place.height < 0: beacon_ID_text_place.y = 0
        if beacon_ID_text_place.y > canvas_height: beacon_ID_text_place.y = canvas_height - beacon_ID_text_place.height
        if beacon_ID_text_place.x <= 0: beacon_ID_text_place.x = 0
        elif beacon_ID_text_place.x + beacon_ID_text_place.width >= canvas_width: beacon_ID_text_place.x = canvas_width - beacon_ID_text_place.width - 1
        canvas.blit(beacon_ID_text, beacon_ID_text_place)
import PARAMETERS as Parameters
import math


def DrawRuler(pygame, canvas, canvas_width, canvas_height, variables):
    pygame.draw.line(canvas, (0, 0, 0), variables.ruler_start_pos, variables.ruler_finish_pos, 2)
    ruler_text = Parameters.ruler_font.render(str(round(math.sqrt(math.pow(variables.ruler_finish_pos[0] * variables.units_per_pixel_x - \
                                                                           variables.ruler_start_pos[0] * variables.units_per_pixel_x, 2) + \
                                                                  math.pow(variables.ruler_finish_pos[1] * variables.units_per_pixel_y - \
                                                                           variables.ruler_start_pos[1] * variables.units_per_pixel_y, 2)), 2)),
                                              False, (255, 255, 255))
    ruler_text_place = ruler_text.get_rect(center=(int(abs(variables.ruler_finish_pos[0] +
                                                           variables.ruler_start_pos[0]) / 2),
                                                   int(abs(variables.ruler_finish_pos[1] +
                                                           variables.ruler_start_pos[1]) / 2)))
    if ruler_text_place.x <= 0:
        ruler_text_place.x = 0
    elif ruler_text_place.x + ruler_text_place.width >= canvas_width:
        ruler_text_place.x = canvas_width - ruler_text_place.width - 2
    if ruler_text_place.y <= 0:
        ruler_text_place.y = 0
    elif ruler_text_place.y + ruler_text_place.height >= canvas_height:
        ruler_text_place.y = canvas_height - ruler_text_place.height - 2
    pygame.draw.rect(canvas, (0, 0, 0), (ruler_text_place.x - 3, ruler_text_place.y,
                                         ruler_text_place.width + 5, ruler_text_place.height))
    canvas.blit(ruler_text, ruler_text_place)
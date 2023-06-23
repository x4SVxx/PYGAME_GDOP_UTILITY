import PARAMETERS as Parameters
from CROSS import  CrossDotWithAllElements
import time
from numba import prange

def Coverage(variables, canvas_width, canvas_height, pygame, window):
    start_time = time.monotonic()

    progressbar_width = 0
    pygame.draw.rect(window, (0, 0, 0),
                     (variables.button_coverage.image_area.x - 1, variables.coverage_text_place.y + variables.coverage_text_place.height + 2,
                      variables.button_coverage.image_area.width + 1, 7))
    for x in prange(canvas_width + 1):
        if x % 3 == 0:
            for y in prange(canvas_height + 1):
                if y % 3 == 0:
                    count_visible_beacons = 0
                    for i in prange(len(variables.beacons_mas)):
                        if not CrossDotWithAllElements(x, y, variables.beacons_mas[i], variables.ovals_mas, variables.rectangles_mas, variables.walls_mas):
                          count_visible_beacons += 1
                    if count_visible_beacons <= 4:
                        variables.coverage_colors_mas[x][y] = Parameters.coverage_colors[count_visible_beacons]
                    else:
                        variables.coverage_colors_mas[x][y] = Parameters.coverage_colors[4]

                    """Progressbar"""
                    if int(((x * y) / (canvas_width * canvas_height)) * variables.button_coverage.image_area.width) - progressbar_width == 2:
                        progressbar_width = int(((x * y) / (canvas_width * canvas_height)) * variables.button_coverage.image_area.width)
                        pygame.draw.rect(window, (0, 230, 0),
                                         (variables.button_coverage.image_area.x, variables.coverage_text_place.y + variables.coverage_text_place.height + 3,
                                          progressbar_width, 5))
                        pygame.display.update()
    """Delete progressbar"""
    pygame.draw.rect(window, Parameters.display_color,
                     (variables.button_coverage.image_area.x - 1, variables.coverage_text_place.y + variables.coverage_text_place.height + 2,
                      variables.button_coverage.image_area.width + 1, 7))

    Helpbar(pygame, window, canvas_width, canvas_height)

    variables.coverage_enabled_flag = True
    print('Расчеты: ' + str(time.monotonic() - start_time))

def Helpbar(pygame, window, canvas_width, canvas_height):
    pygame.draw.rect(window, Parameters.display_color, (Parameters.canvas_offset_left + canvas_width + 5, Parameters.canvas_offset_top, 20, canvas_height))

    pygame.draw.rect(window, Parameters.coverage_colors[0], (Parameters.canvas_offset_left + canvas_width + 5,
                                                             Parameters.canvas_offset_top,
                                                             20,
                                                             int(canvas_height / 5)))
    pygame.draw.rect(window, Parameters.coverage_colors[1], (Parameters.canvas_offset_left + canvas_width + 5,
                                                             Parameters.canvas_offset_top + int(canvas_height / 5),
                                                             20,
                                                             int(canvas_height / 5)))
    pygame.draw.rect(window, Parameters.coverage_colors[2], (Parameters.canvas_offset_left + canvas_width + 5,
                                                             Parameters.canvas_offset_top + int(canvas_height / 5) * 2,
                                                             20,
                                                             int(canvas_height/ 5)))
    pygame.draw.rect(window, Parameters.coverage_colors[3], (Parameters.canvas_offset_left + canvas_width + 5,
                                                             Parameters.canvas_offset_top + int(canvas_height / 5) * 3,
                                                             20,
                                                             int(canvas_height / 5)))
    pygame.draw.rect(window, Parameters.coverage_colors[4], (Parameters.canvas_offset_left + canvas_width + 5,
                                                             Parameters.canvas_offset_top + int(canvas_height / 5) * 4,
                                                             20,
                                                             int(canvas_height / 5) + 5))

    text = Parameters.buttons_font.render('0', True, (0, 0, 0))
    text_place = text.get_rect(center=(Parameters.canvas_offset_left + canvas_width + 5 + 10,
                                       Parameters.canvas_offset_top + int((canvas_height - 40) / 5) / 2))
    window.blit(text, text_place)
    text = Parameters.buttons_font.render('1', True, (0, 0, 0))
    text_place = text.get_rect(center=(Parameters.canvas_offset_left + canvas_width + 5 + 10,
                                       Parameters.canvas_offset_top + int((canvas_height - 40) / 5) + int((canvas_height - 40) / 5) / 2 + 10))
    window.blit(text, text_place)
    text = Parameters.buttons_font.render('2', True, (0, 0, 0))
    text_place = text.get_rect(center=(Parameters.canvas_offset_left + canvas_width + 5 + 10,
                                       Parameters.canvas_offset_top + int((canvas_height - 40) / 5) * 2 + int((canvas_height - 40) / 5) / 2 + 20))
    window.blit(text, text_place)
    text = Parameters.buttons_font.render('3', True, (0, 0, 0))
    text_place = text.get_rect(center=(Parameters.canvas_offset_left + canvas_width + 5 + 10,
                                       Parameters.canvas_offset_top + int((canvas_height - 40) / 5) * 3 + int((canvas_height - 40) / 5) / 2 + 30))
    window.blit(text, text_place)
    text = Parameters.buttons_font.render('>3', True, (0, 0, 0))
    text_place = text.get_rect(center=(Parameters.canvas_offset_left + canvas_width + 5 + 10,
                                       Parameters.canvas_offset_top + int((canvas_height - 40) / 5) * 4 + int((canvas_height - 40) / 5) / 2 + 40))
    window.blit(text, text_place)

    pygame.draw.rect(window, (0, 0, 0), (Parameters.canvas_offset_left + canvas_width + 5, Parameters.canvas_offset_top, 20, canvas_height), 1)

def DrawCoverage(variables, pygame, canvas, canvas_width, canvas_height):
    for x in prange(canvas_width + 1):
        if x % 3 == 0:
            for y in prange(canvas_height + 1):
                if y % 3 == 0:
                    pygame.draw.rect(canvas, variables.coverage_colors_mas[x][y], (x - 1, y - 1, 3, 3))
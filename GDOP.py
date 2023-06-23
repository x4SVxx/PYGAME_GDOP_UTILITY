import numpy as np
import time
from CROSS import  CrossDotWithAllElements
import math
from numba import  prange
import PARAMETERS as Parameters

def GDOP(variables, canvas_width, canvas_height, pygame, window):
    start_time = time.monotonic()

    """Frame for progressbar / Рамка для загрузки"""
    pygame.draw.rect(window, (0, 0, 0),
                     (variables.button_GDOP.image_area.x - 1, variables.GDOP_text_place.y + variables.GDOP_text_place.height + 2,
                      variables.button_GDOP.image_area.width + 1, 7))

    if variables.choice_ToF_method_flag:
        GDOPcalculationsToF(variables, pygame, window, canvas_width, canvas_height)
    elif variables.choice_TDoA_method_flag:
        GDOPcalculationsTDoA(variables, pygame, window, canvas_width, canvas_height)

    """Delete progressbar / Удаление загрузки"""
    pygame.draw.rect(window, Parameters.display_color,
                     (variables.button_GDOP.image_area.x - 1, variables.GDOP_text_place.y + variables.GDOP_text_place.height + 2,
                      variables.button_GDOP.image_area.width + 1, 7))
    variables.progressbar_width = 0

    Helpbar(pygame, window, canvas_width, canvas_height)

    variables.GDOP_enabled_flag = True
    print('Расчеты: ' + str(time.monotonic() - start_time))

def GDOPcalculationsToF(variables, pygame, window, canvas_width, canvas_height):
    for x in prange(canvas_width + 1):
        if x % 3 == 0:
            for y in prange(canvas_height + 1):
                if y % 3 == 0:
                    visible_beacons = []
                    for i in prange(len(variables.beacons_mas)):
                        if not CrossDotWithAllElements(x, y, variables.beacons_mas[i], variables.ovals_mas, variables.rectangles_mas, variables.walls_mas):
                            visible_beacons.append(variables.beacons_mas[i])
                    if len(visible_beacons) < 2:
                        ColorsCalculations(x, y, 0, variables, pygame, window, canvas_width, canvas_height)
                    else:
                        H = np.zeros((len(visible_beacons), 2))
                        for i in prange(len(visible_beacons)):
                            try:
                                H[i][0] = (x - visible_beacons[i].x) / math.sqrt(pow(x - visible_beacons[i].x, 2) + pow(y - visible_beacons[i].y, 2))
                                H[i][1] = (y - visible_beacons[i].y) / math.sqrt(pow(x - visible_beacons[i].x, 2) + pow(y - visible_beacons[i].y, 2))
                            except:
                                H[i][0] = 0
                                H[i][1] = 0
                        try:
                            Hinv = np.linalg.inv(np.transpose(H).dot(H))
                            math.sqrt(pow(Hinv[0][0], 2) + pow(Hinv[1][1], 2))
                            ColorsCalculations(x, y, math.sqrt(pow(Hinv[0][0], 2) + pow(Hinv[1][1], 2)),
                                               variables, pygame, window, canvas_width, canvas_height)
                        except:
                            ColorsCalculations(x, y, 0, variables, pygame, window, canvas_width, canvas_height)

def GDOPcalculationsTDoA(variables, pygame, window, canvas_width, canvas_height):
    for x in prange(canvas_width + 1):
        if x % 3 == 0:
            for y in prange(canvas_height + 1):
                if y % 3 == 0:
                    visible_beacons = []
                    for i in prange(len(variables.beacons_mas)):
                        if not CrossDotWithAllElements(x, y, variables.beacons_mas[i], variables.ovals_mas, variables.rectangles_mas, variables.walls_mas):
                            visible_beacons.append(variables.beacons_mas[i])
                    if len(visible_beacons) < 3:
                        ColorsCalculations(x, y, 0, variables, pygame, window, canvas_width, canvas_height)
                    else:
                        H = np.zeros((len(visible_beacons), 3))
                        for i in prange(len(visible_beacons)):
                            try:
                                H[i][0] = (x - visible_beacons[i].x) / math.sqrt(pow(x - visible_beacons[i].x, 2) + pow(y - visible_beacons[i].y, 2))
                                H[i][1] = (y - visible_beacons[i].y) / math.sqrt(pow(x - visible_beacons[i].x, 2) + pow(y - visible_beacons[i].y, 2))
                                H[i][2] = 1
                            except:
                                H[i][0] = 0
                                H[i][1] = 0
                                H[i][1] = 0
                        try:
                            Hinv = np.linalg.inv(np.transpose(H).dot(H))
                            ColorsCalculations(x, y, math.sqrt(pow(Hinv[0][0], 2) + pow(Hinv[1][1], 2) + pow(Hinv[2][2], 2)),
                                               variables, pygame, window, canvas_width, canvas_height)
                        except:
                            ColorsCalculations(x, y, 0, variables, pygame, window, canvas_width, canvas_height)

def ColorsCalculations(x, y, GDOP_var, variables, pygame, window, canvas_width, canvas_height):
    """ПОСТРОЕНИЕ ГРАДИЕНТА"""
    """ПЛОХАЯ ВИДИМОСТЬ - КРАСНЫЙ ЦВЕТ В RGB R=255
       СРЕДНЯЯ ВИДИМОСТЬ - ЖЕЛТЫЙ ЦВЕТ В RGB R=255, G=255
       ХОРОШАЯ ВИДИМОСТЬ - ЗЕЛЕНЫЙ ЦВЕТ В RGB G=255"""
    """ЗДЕСЬ ИСПОЛЬЗУЕТСЯ 240 ВМЕСТО 255, Т.К. УДОБНО ИСПОЛЬЗОВАТЬ ДЛЯ ДИАПОЗОН (ОТ 0 ДО 6)"""
    """ДИАПОЗОН ПОДЕЛЕН НА 2 УЧАТСКА (ДО СЕРЕДИНЫ (ОТ ЗЕЛЕНОГО ДО ЖЕЛТОГО)
       И ПОСЛЕ СЕРЕДИНЫ (ОТ ЖЕЛТОГО ДО КРАСНОГО)"""
    """УМНОЖЕНИЕ НА 40 НУЖНО ДЛЯ RGB ПРИВОДА (6*40=240)
       УМНОЖЕНИЕ НА 2 ДЛЯ РАЗДЕЛЕНИЯ ДО СЕРЕДИНЫ И ПОСЛЕ"""
    """В УСЛОВИИ > 3 ЗЕЛЕНЫЙ ЦВЕТ РАСТЕТ С УМЕНЬШЕНИЕМ GDOP и цвет переходит от красного в желтый
       В УСЛОВИИ 0.1 < < 3 КРАСНЫЙ ЦВЕТ УМЕНЬШАЕТСЯ С УМЕНЬШЕНИЕМ GDOP и цвет переходит в зеленый"""
    try:
        if GDOP_var <= 0:
            variables.GDOP_colors_mas[x][y] = (240, 0, 0)
        elif GDOP_var > 6:
            variables.GDOP_colors_mas[x][y] = (240, 0, 0)
        elif GDOP_var > 3:
            variables.GDOP_colors_mas[x][y] = (240, int(math.fabs((GDOP_var * 40 - 240) * 2)), 0)
        else:
            variables.GDOP_colors_mas[x][y] = (int(math.fabs(120 + GDOP_var * 40)), 240, 0)
    except:
        variables.GDOP_colors_mas[x][y] = (240, 0, 0)

    Progressbar(x, y, variables, pygame, window, canvas_width, canvas_height)

def Progressbar(x, y, variables, pygame, window, canvas_width, canvas_height):
    if int(((x * y) / (canvas_width * canvas_height)) * variables.button_GDOP.image_area.width) - variables.progressbar_width == 2:
        variables.progressbar_width = int(((x * y) / (canvas_width * canvas_height)) * variables.button_GDOP.image_area.width)
        pygame.draw.rect(window, (0, 230, 0),
                         (variables.button_GDOP.image_area.x, variables.GDOP_text_place.y + variables.GDOP_text_place.height + 3,
                          variables.progressbar_width, 5))
        pygame.display.update()

def Helpbar(pygame, window, canvas_width, canvas_height):
    pygame.draw.rect(window, Parameters.display_color, (Parameters.canvas_offset_left + canvas_width + 5, Parameters.canvas_offset_top, 20, canvas_height))

    color_rect = pygame.Surface((3, 3))  # 3x3 bitmap
    pygame.draw.line(color_rect, (255, 0 , 0), (0, 0), (2, 0))  # left color line
    pygame.draw.line(color_rect, (255, 255, 0), (0, 1), (2, 1))  # middle color line
    pygame.draw.line(color_rect, (0, 255, 0), (0, 2), (2, 2))  # right color line
    color_rect = pygame.transform.smoothscale(color_rect, (20, canvas_height))  # stretch
    window.blit(color_rect, (Parameters.canvas_offset_left + canvas_width + 5, Parameters.canvas_offset_top, 20, canvas_height))

    finish_text = Parameters.buttons_font.render('>6', True, (0, 0, 0))
    finish_text_place = finish_text.get_rect(center=(Parameters.canvas_offset_left + canvas_width + 5 + 10, Parameters.canvas_offset_top + 30))
    window.blit(finish_text, finish_text_place)
    middle_text = Parameters.buttons_font.render('3', True, (0, 0, 0))
    middle_text_place = middle_text.get_rect(center=(Parameters.canvas_offset_left + canvas_width + 5 + 10, Parameters.canvas_offset_top + canvas_height / 2))
    window.blit(middle_text, middle_text_place)
    finish_text = Parameters.buttons_font.render('1', True, (0, 0, 0))
    finish_text_place = finish_text.get_rect(center=(Parameters.canvas_offset_left + canvas_width + 5 + 10, Parameters.canvas_offset_top + canvas_height - 30))
    window.blit(finish_text, finish_text_place)

    pygame.draw.rect(window, (0, 0, 0), (Parameters.canvas_offset_left + canvas_width + 5, Parameters.canvas_offset_top, 20, canvas_height), 1)

def DrawGDOP(canvas, canvas_width, canvas_height, pygame, variables):
    for x in prange(canvas_width + 1):
        if x % 3 == 0:
            for y in prange(canvas_height + 1):
                if y % 3 == 0:
                    pygame.draw.rect(canvas, variables.GDOP_colors_mas[x][y], (x - 1, y - 1, 3, 3))
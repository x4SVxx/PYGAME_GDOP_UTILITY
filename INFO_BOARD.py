from BEACON import  Beacon
import PARAMETERS as Parameters
from BUTTON import  Button


def BeaconsInfo(display_width, display_height, pygame, window, beacon, display_color, canvas_offset_top, canvas_offset_right, variables, x=0, y=0):
    if isinstance(beacon, Beacon):
        pygame.draw.rect(window, display_color, (display_width - (canvas_offset_right - 30), canvas_offset_top - 10, canvas_offset_right, 400))
        ID_font = pygame.font.SysFont('ebrima', 14)
        coordinates_font = pygame.font.SysFont('ebrima', 12)
        ID_text = ID_font.render('ID', True, (0, 0, 0))
        ID_var = ID_font.render(str(beacon.ID), True, (0, 0, 0))
        x_text = coordinates_font.render('X', True, (0, 0, 0))
        y_text = coordinates_font.render('Y', True, (0, 0, 0))
        x_var = coordinates_font.render(str(beacon.user_x), True, (0, 0, 0))
        y_var = coordinates_font.render(str(beacon.user_y), True, (0, 0, 0))
        """140 центр теста для ID (ширина дисплея 1440 - (ID текст.x + 20 + половина ширины вводного поля 80 = 140)"""
        ID_text_place = ID_text.get_rect(center=(display_width - 240, canvas_offset_top + 60))
        ID_text_place.x = display_width - 240
        ID_var_place = ID_var.get_rect(center=(display_width - 140, canvas_offset_top + 60))
        x_text_place = x_text.get_rect(center=(display_width - 190, canvas_offset_top + 125))
        y_text_place = y_text.get_rect(center=(display_width - 190, canvas_offset_top + 145))
        """+45 чтобы значение отображалось по центру воодного поля"""
        x_var_place = x_var.get_rect(center=(display_width - 190 + 48, canvas_offset_top + 126))
        y_var_place = y_var.get_rect(center=(display_width - 190 + 48, canvas_offset_top + 146))
        window.blit(ID_text, ID_text_place)
        window.blit(ID_var, ID_var_place)
        window.blit(x_text, x_text_place)
        window.blit(y_text, y_text_place)
        window.blit(x_var, x_var_place)
        window.blit(y_var, y_var_place)
        """+2 пикселя по оси y для корректного отоброжения прямоугольника с полем ввода"""
        if variables.input_beacon_ID_flag:
            pygame.draw.rect(window, (255, 0, 0), (ID_text_place.x + 20, ID_text_place.y + 2, 160, ID_var_place.height), 1)
        else:
            pygame.draw.rect(window, (0, 0, 0), (ID_text_place.x + 20, ID_text_place.y + 2, 160, ID_var_place.height), 1)
        if variables.input_beacon_x_flag:
            pygame.draw.rect(window, (255, 0, 0), (x_text_place.x + 15, x_text_place.y + 2, 75, x_text_place.height), 1)
        else:
            pygame.draw.rect(window, (0, 0, 0), (x_text_place.x + 15, x_text_place.y + 2, 75, x_text_place.height), 1)
        if variables.input_beacon_y_flag:
            pygame.draw.rect(window, (255, 0, 0), (y_text_place.x + 15, y_text_place.y + 2, 75, y_text_place.height), 1)
        else:
            pygame.draw.rect(window, (0, 0, 0), (y_text_place.x + 15, y_text_place.y + 2, 75, y_text_place.height), 1)

        if ID_text_place.x + 20 <= x <= ID_text_place.x + 20 + 160 and \
                ID_text_place.y + 2 <= y <= ID_text_place.y + 2 + ID_var_place.height:
            if not variables.input_beacon_ID_flag:
                variables.input_beacon_ID_flag = True
                variables.refactor_beacon = beacon
                pygame.draw.rect(window, (255, 0, 0), (ID_text_place.x + 20, ID_text_place.y + 2, 160, ID_var_place.height), 1)

        if x_text_place.x + 15 <= x <= x_text_place.x + 15 + 75 and x_text_place.y + 2 <= y <= x_text_place.y + 2 + x_text_place.height:
            if not variables.input_beacon_x_flag:
                variables.input_beacon_x_flag = True
                variables.refactor_beacon = beacon
                pygame.draw.rect(window, (255, 0, 0), (x_text_place.x + 15, x_text_place.y + 2, 75, x_text_place.height), 1)

        if y_text_place.x + 15 <= x <= y_text_place.x + 15 + 75 and y_text_place.y + 2 <= y <= y_text_place.y + 2 + y_text_place.height:
            if not variables.input_beacon_y_flag:
                variables.input_beacon_y_flag = True
                variables.refactor_beacon = beacon
                pygame.draw.rect(window, (255, 0, 0), (y_text_place.x + 15, y_text_place.y + 2, 75, y_text_place.height), 1)

        pygame.draw.rect(window, (0, 100, 0), (display_width - 225, y_text_place[1] + 90, 30, 20))
        pygame.draw.rect(window, (0, 230, 0), (display_width - 185, y_text_place[1] + 90, 30, 20))
        pygame.draw.rect(window, (255, 0, 0), (display_width - 145, y_text_place[1] + 90, 30, 20))
        pygame.draw.rect(window, (255, 0, 255), (display_width - 105, y_text_place[1] + 90, 30, 20))

        pygame.draw.rect(window, (0, 0, 255), (display_width - 225, y_text_place[1] + 120, 30, 20))
        pygame.draw.rect(window, (0, 150, 255), (display_width - 185, y_text_place[1] + 120, 30, 20))
        pygame.draw.rect(window, (255, 200, 0), (display_width - 145, y_text_place[1] + 120, 30, 20))
        pygame.draw.rect(window, (255, 255, 0), (display_width - 105, y_text_place[1] + 120, 30, 20))

        pygame.draw.rect(window, (180, 30, 30), (display_width - 225, y_text_place[1] + 150, 30, 20))
        pygame.draw.rect(window, (255, 70, 0), (display_width - 185, y_text_place[1] + 150, 30, 20))
        pygame.draw.rect(window, (170, 50, 100), (display_width - 145, y_text_place[1] + 150, 30, 20))
        pygame.draw.rect(window, (150, 0, 200), (display_width - 105, y_text_place[1] + 150, 30, 20))

        pygame.draw.rect(window, (0, 0, 0), (display_width - 225, y_text_place[1] + 180, 30, 20))
        pygame.draw.rect(window, (75, 75, 75), (display_width - 185, y_text_place[1] + 180, 30, 20))
        pygame.draw.rect(window, (150, 150, 150), (display_width - 145, y_text_place[1] + 180, 30, 20))
        pygame.draw.rect(window, (255, 255, 255), (display_width - 105, y_text_place[1] + 180, 30, 20))

        if display_width - 225 <= x <= display_width - 225 + 30 and y_text_place[1] + 90 <= y <= y_text_place[1] + 90 + 20:
            beacon.color = (0, 100, 0)
        elif display_width - 185 <= x <= display_width - 185 + 30 and y_text_place[1] + 90 <= y <= y_text_place[1] + 90 + 20:
            beacon.color = (0, 230, 0)
        elif display_width - 145 <= x <= display_width - 145 + 30 and y_text_place[1] + 90 <= y <= y_text_place[1] + 90 + 20:
            beacon.color = (255, 0, 0)
        elif display_width - 105 <= x <= display_width - 105 + 30 and y_text_place[1] + 90 <= y <= y_text_place[1] + 90 + 20:
            beacon.color = (255, 0, 255)

        elif display_width - 225 <= x <= display_width - 225 + 30 and y_text_place[1] + 120 <= y <= y_text_place[1] + 120 + 20:
            beacon.color = (0, 0, 255)
        elif display_width - 185 <= x <= display_width - 185 + 30 and y_text_place[1] + 120 <= y <= y_text_place[1] + 120 + 20:
            beacon.color = (0, 150, 255)
        elif display_width - 145 <= x <= display_width - 145 + 30 and y_text_place[1] + 120 <= y <= y_text_place[1] + 120 + 20:
            beacon.color = (255, 200, 0)
        elif display_width - 105 <= x <= display_width - 105 + 30 and y_text_place[1] + 120 <= y <= y_text_place[1] + 120 + 20:
            beacon.color = (255, 255, 0)

        elif display_width - 225 <= x <= display_width - 225 + 30 and y_text_place[1] + 150 <= y <= y_text_place[1] + 150 + 20:
            beacon.color = (180, 30, 30)
        elif display_width - 185 <= x <= display_width - 185 + 30 and y_text_place[1] + 150 <= y <= y_text_place[1] + 150 + 20:
            beacon.color = (255, 70, 0)
        elif display_width - 145 <= x <= display_width - 145 + 30 and y_text_place[1] + 150 <= y <= y_text_place[1] + 150 + 20:
            beacon.color = (170, 50, 100)
        elif display_width - 105 <= x <= display_width - 105 + 30 and y_text_place[1] + 150 <= y <= y_text_place[1] + 150 + 20:
            beacon.color = (150, 0, 200)

        elif display_width - 225 <= x <= display_width - 225 + 30 and y_text_place[1] + 180 <= y <= y_text_place[1] + 180 + 20:
            beacon.color = (0, 0, 0)
        elif display_width - 185 <= x <= display_width - 185 + 30 and y_text_place[1] + 180 <= y <= y_text_place[1] + 180 + 20:
            beacon.color = (75, 75, 75)
        elif display_width - 145 <= x <= display_width - 145 + 30 and y_text_place[1] + 180 <= y <= y_text_place[1] + 180 + 20:
            beacon.color = (150, 150, 150)
        elif display_width - 105 <= x <= display_width - 105 + 30 and y_text_place[1] + 180 <= y <= y_text_place[1] + 180 + 20:
            beacon.color = (255, 255, 255)

        if beacon.color == (0, 100, 0):
            pygame.draw.rect(window, (255, 0, 0), (display_width - 230, y_text_place[1] + 85, 40, 30), 1)
        elif beacon.color == (0, 230, 0):
            pygame.draw.rect(window, (255, 0, 0), (display_width - 190, y_text_place[1] + 85, 40, 30), 1)
        elif beacon.color == (255, 0, 0):
            pygame.draw.rect(window, (255, 0, 0), (display_width - 150, y_text_place[1] + 85, 40, 30), 1)
        elif beacon.color == (255, 0, 255):
            pygame.draw.rect(window, (255, 0, 0), (display_width - 110, y_text_place[1] + 85, 40, 30), 1)

        elif beacon.color == (0, 0, 255):
            pygame.draw.rect(window, (255, 0, 0), (display_width - 230, y_text_place[1] + 115, 40, 30), 1)
        elif beacon.color == (0, 150, 255):
            pygame.draw.rect(window, (255, 0, 0), (display_width - 190, y_text_place[1] + 115, 40, 30), 1)
        elif beacon.color == (255, 200, 0):
            pygame.draw.rect(window, (255, 0, 0), (display_width - 150, y_text_place[1] + 115, 40, 30), 1)
        elif beacon.color == (255, 255, 0):
            pygame.draw.rect(window, (255, 0, 0), (display_width - 110, y_text_place[1] + 115, 40, 30), 1)

        elif beacon.color == (180, 30, 30):
            pygame.draw.rect(window, (255, 0, 0), (display_width - 230, y_text_place[1] + 145, 40, 30), 1)
        elif beacon.color == (255, 70, 0):
            pygame.draw.rect(window, (255, 0, 0), (display_width - 190, y_text_place[1] + 145, 40, 30), 1)
        elif beacon.color == (170, 50, 100):
            pygame.draw.rect(window, (255, 0, 0), (display_width - 150, y_text_place[1] + 145, 40, 30), 1)
        elif beacon.color == (150, 0, 200):
            pygame.draw.rect(window, (255, 0, 0), (display_width - 110, y_text_place[1] + 145, 40, 30), 1)

        elif beacon.color == (0, 0, 0):
            pygame.draw.rect(window, (255, 0, 0), (display_width - 230, y_text_place[1] + 175, 40, 30), 1)
        elif beacon.color == (75, 75, 75):
            pygame.draw.rect(window, (255, 0, 0), (display_width - 190, y_text_place[1] + 175, 40, 30), 1)
        elif beacon.color == (150, 150, 150):
            pygame.draw.rect(window, (255, 0, 0), (display_width - 150, y_text_place[1] + 175, 40, 30), 1)
        elif beacon.color == (255, 255, 255):
            pygame.draw.rect(window, (255, 0, 0), (display_width - 110, y_text_place[1] + 175, 40, 30), 1)

        pygame.draw.rect(window, (0, 0, 0), (display_width - 250, canvas_offset_top, 200, 370), 1)
        info_text = Parameters.information_font.render('INFORMATION', True, (0, 0, 0))
        info_text_place = info_text.get_rect(center=(display_width - 150, canvas_offset_top))
        info_text_place.x = display_width - 250
        """Закрашивание области для корректного отображения надписи"""
        pygame.draw.rect(window, display_color, (display_width - 250, canvas_offset_top, info_text_place.width + 5, info_text_place.height / 2 + 5))
        window.blit(info_text, info_text_place)

        """Ширина прямоугольника как у ID окна"""
        """-17 для выравнивания прямоугольника по центру"""
        """Ширины 180 шватает для 10 символов"""
        pygame.draw.rect(window, (0, 0, 0), (display_width - 240, x_text_place.y - 17, 180, 75), 1)
        coordinates_text = Parameters.buttons_font.render('COORDINATES', True, (0, 0, 0))
        """-15 т.к. сдвиг на 2 пикселя вниз для текста"""
        coordinates_text_place = coordinates_text.get_rect(center=(display_width - 150, x_text_place.y - 15))
        coordinates_text_place.x = display_width - 240
        """Закрашивание области для корректного отображения надписи"""
        pygame.draw.rect(window, display_color, (display_width - 240, x_text_place.y - 17, coordinates_text_place.width + 5, coordinates_text_place.height / 2 + 5))
        window.blit(coordinates_text, coordinates_text_place)

        pygame.draw.rect(window, (0, 0, 0), (display_width - 240, y_text_place[1] + 70, 180, 145), 1)
        color_text = Parameters.buttons_font.render('COLOR', True, (0, 0, 0))
        """72 т.к. сдвиг на 2 пикселя вниз для текста"""
        color_text_place = color_text.get_rect(center=(display_width - 150, y_text_place[1] + 72))
        color_text_place.x = display_width - 240
        """Закрашивание области для корректного отображения надписи"""
        pygame.draw.rect(window, display_color, (display_width - 240, y_text_place[1] + 70, color_text_place.width + 5, color_text_place.height / 2 + 5))
        window.blit(color_text, color_text_place)

        """Close_info_board_button / Кнопка закрытия информационного табло"""
        close_info_board_button = Button(Parameters.display_color, pygame, window,
                                        (display_width - 250 + 200 - 20 - 3,
                                         canvas_offset_top + 3,
                                         20,
                                         20),
                                        'Images/button_close_info_board.png', 'Images/button_close_info_board.png')

        if close_info_board_button.image_area.x <= x <= close_info_board_button.image_area.x + close_info_board_button.image_area.width and \
            close_info_board_button.image_area.y <= y <= close_info_board_button.image_area.y + close_info_board_button.image_area.height:
            pygame.draw.rect(window, display_color, (display_width - (canvas_offset_right - 30), canvas_offset_top - 10, canvas_offset_right, 400))
            variables.info_board_active_flag = False

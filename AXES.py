import PARAMETERS as Parameters


def Axes(pygame, window, variables, display_width, display_height, canvas_width, canvas_height, input_flag_x, input_flag_y):

    pygame.draw.rect(window, Parameters.display_color, (0, Parameters.canvas_offset_top + canvas_height, display_width, 30))
    pygame.draw.rect(window, Parameters.display_color, (0, 0, Parameters.canvas_offset_left, display_height))
    axes_text_0 = Parameters.axes_font.render('0', True, (0, 0, 0))
    exes_text_0_place = axes_text_0.get_rect(center=(Parameters.canvas_offset_left / 2,
                                                     Parameters.canvas_offset_top + canvas_height))
    window.blit(axes_text_0, exes_text_0_place)
    variables.units_per_pixel_x = variables.axes_max_x / canvas_width
    variables.units_per_pixel_y = variables.axes_max_y / canvas_height
    if variables.units_per_pixel_x == 0:
        variables.units_per_pixel_x = float(0.000001)
    if variables.units_per_pixel_y == 0:
        variables.units_per_pixel_y = float(0.000001)
    if variables.text_axes_max_x != '':
        for i in range(1, Parameters.axes_count + 1):
            """Для максимального значения отдельный ввод напрямую из переменной. т.к. может быть точка в конце"""
            if i == Parameters.axes_count:
                axes_text_x = Parameters.axes_font.render(variables.text_axes_max_x, True, (0, 0, 0))
            else:
                """Если число целое убираем лишние нули"""
                if variables.axes_max_x != 0:
                    if int(variables.axes_max_x / 10 * i) / round(float(variables.axes_max_x / 10 * i), 2) != 1.0:
                        axes_text_x = Parameters.axes_font.render(str(round(float(variables.axes_max_x / 10 * i), 2)), True, (0, 0, 0))
                    else:
                        axes_text_x = Parameters.axes_font.render(str(int(variables.axes_max_x / 10 * i)), True, (0, 0, 0))
                else:
                    axes_text_x = Parameters.axes_font.render('0', True, (0, 0, 0))
            axes_text_place_x = axes_text_x.get_rect(center=(int(Parameters.canvas_offset_left + canvas_width * i / 10),
                                                             int(Parameters.canvas_offset_top + canvas_height + 20)))
            window.blit(axes_text_x, axes_text_place_x)
    if variables.text_axes_max_y != '':
        for i in range(1, Parameters.axes_count + 1):
            """Для максимального значения отдельный ввод напрямую из переменной. т.к. может быть точка в конце"""
            if i == Parameters.axes_count:
                axes_text_y = Parameters.axes_font.render(variables.text_axes_max_y, True, (0, 0, 0))
            else:
                """Если число целое убираем лишние нули"""
                if variables.axes_max_y != 0:
                    if int(variables.axes_max_y / 10 * i) / round(float(variables.axes_max_y / 10 * i), 2) != 1.0:
                        axes_text_y = Parameters.axes_font.render(str(round(float(variables.axes_max_y / 10 * i), 2)), True, (0, 0, 0))
                    else:
                        axes_text_y = Parameters.axes_font.render(str(int(variables.axes_max_y / 10 * i)), True, (0, 0, 0))
                else:
                    axes_text_y = Parameters.axes_font.render('0', True, (0, 0, 0))
            axes_text_place_y = axes_text_y.get_rect(center=(int(Parameters.canvas_offset_left / 2),
                                                             int(Parameters.canvas_offset_top + canvas_height * (10 - i) / 10)))
            window.blit(axes_text_y, axes_text_place_y)
    if not input_flag_x:
        """55 - ширина вводного окна (65 - полный отступ слева)"""
        """55 / 2 - выравнивание по центру"""
        """16 - отступ по 2 пикселя сверху и снизу (высота шрифта - 14)"""
        pygame.draw.rect(window, (0, 0, 0),
                         (int(Parameters.canvas_offset_left + canvas_width - 55 / 2),
                          int(Parameters.canvas_offset_top + canvas_height + 13), 55, 16), 1)
    else:
        pygame.draw.rect(window, (255, 0, 0), (int(Parameters.canvas_offset_left + canvas_width - 55 / 2),
                                               int(Parameters.canvas_offset_top + canvas_height + 13), 55, 16), 1)
    if not input_flag_y:
        pygame.draw.rect(window, (0, 0, 0), (5, int(Parameters.canvas_offset_top - 7), 55, 16), 1)
    else:
        pygame.draw.rect(window, (255, 0, 0), (5, int(Parameters.canvas_offset_top - 7), 55, 16), 1)

    for beacon in variables.beacons_mas:
        beacon.x = int(float(beacon.user_x) / variables.units_per_pixel_x)
        beacon.y = int((canvas_height * variables.units_per_pixel_y - float(beacon.user_y)) / variables.units_per_pixel_y)
    for oval in variables.ovals_mas:
        oval.x = int(float(oval.user_x) / variables.units_per_pixel_x)
        oval.width = int(float(oval.user_width) / variables.units_per_pixel_x)
        oval.y = int((canvas_height * variables.units_per_pixel_y - float(oval.user_y)) / variables.units_per_pixel_y)
        oval.height = int(float(oval.user_height) / variables.units_per_pixel_y)
    for rectangle in variables.rectangles_mas:
        rectangle.x = int(float(rectangle.user_x) / variables.units_per_pixel_x)
        rectangle.width = int(float(rectangle.user_width) / variables.units_per_pixel_x)
        rectangle.y = int((canvas_height * variables.units_per_pixel_y - float(rectangle.user_y)) / variables.units_per_pixel_y)
        rectangle.height = int(float(rectangle.user_height) / variables.units_per_pixel_y)
    for wall in variables.walls_mas:
        wall.x1 = int(float(wall.user_x1) / variables.units_per_pixel_x)
        wall.x2 = int(float(wall.user_x2) / variables.units_per_pixel_x)
        wall.y1 = int((canvas_height * variables.units_per_pixel_y - float(wall.user_y1)) / variables.units_per_pixel_y)
        wall.y2 = int((canvas_height * variables.units_per_pixel_y - float(wall.user_y2)) / variables.units_per_pixel_y)

def DrawAxes(pygame, variables, canvas, canvas_width, canvas_height):
    for i in range(1, Parameters.axes_count + 1):
        if variables.displaying_axes_flag:
            pygame.draw.line(canvas, Parameters.axes_color,
                             (int(canvas_width * i / 10), canvas_height), (int(canvas_width * i / 10), 0), 1)
            pygame.draw.line(canvas, Parameters.axes_color,
                             (0, int(canvas_height * (10 - i) / 10) - 1), (canvas_width, int(canvas_height * (10 - i) / 10) - 1), 1)
        pygame.draw.line(canvas, (0, 0, 0),
                         (int(canvas_width * i / 10), canvas_height), (int(canvas_width * i / 10), canvas_height - 5), 2)
        pygame.draw.line(canvas, (0, 0, 0),
                         (0, int(canvas_height * (10 - i) / 10) - 1), (5, int(canvas_height * (10 - i) / 10) - 1), 2)
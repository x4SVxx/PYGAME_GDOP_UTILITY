from AXES import  Axes
import INFO_BOARD
import PARAMETERS as Parameters
import BUTTONS_FUNCTIONS as ButtonFunctions
import MOUSE as Mouse
import sys


def EventsHandler(event, pygame, window, variables, display_width, display_height,
                  canvas, canvas_place, canvas_width, canvas_height):

    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
        """Mouse press / Нажатие мыши"""

        """Removing flags / Снятие флагов"""
        if variables.input_axes_x_flag or variables.input_axes_y_flag:
            variables.input_axes_x_flag = False
            variables.input_axes_y_flag = False
            Axes(pygame, window, variables, display_width, display_height, canvas_width, canvas_height, False, False)
        elif variables.input_beacon_ID_flag:
            variables.input_beacon_ID_flag = False
            INFO_BOARD.BeaconsInfo(display_width, display_height, pygame, window, variables.info_beacon,
                                   Parameters.display_color, Parameters.canvas_offset_top,
                                   Parameters.canvas_offset_right, variables)
        elif variables.input_beacon_x_flag:
            variables.input_beacon_x_flag = False
            INFO_BOARD.BeaconsInfo(display_width, display_height, pygame, window, variables.info_beacon,
                                   Parameters.display_color, Parameters.canvas_offset_top,
                                   Parameters.canvas_offset_right, variables)
        elif variables.input_beacon_y_flag:
            variables.input_beacon_y_flag = False
            INFO_BOARD.BeaconsInfo(display_width, display_height, pygame, window, variables.info_beacon,
                                   Parameters.display_color, Parameters.canvas_offset_top,
                                   Parameters.canvas_offset_right, variables)

        if event.button == 1:
            """Left mouse buttom press / Нажатие левой кнопки мыши"""

            """Beacon color selection / Выбор цвета для маяка"""
            if variables.info_board_active_flag:
                INFO_BOARD.BeaconsInfo(display_width, display_height, pygame, window, variables.info_beacon,
                                       Parameters.display_color, Parameters.canvas_offset_top,
                                       Parameters.canvas_offset_right, variables, event.pos[0], event.pos[1])

            if variables.button_close.image_area.x <= event.pos[0] <= variables.button_close.image_area.x + variables.button_close.image_area.width and \
                    variables.button_close.image_area.y <= event.pos[1] <= variables.button_close.image_area.y + variables.button_close.image_area.height:
                """Close program button / Кнопка закрытия"""
                ButtonFunctions.CloseButtonFunctions(pygame)

            elif variables.button_beacon.image_area.x <= event.pos[0] <= variables.button_beacon.image_area.x + variables.button_beacon.image_area.width and \
                    variables.button_beacon.image_area.y <= event.pos[1] <= variables.button_beacon.image_area.y + variables.button_beacon.image_area.height:
                """Beacons button / Кнопка маяков"""
                ButtonFunctions.BeaconButtonFunctions(variables, pygame, window)

            elif variables.button_oval.image_area.x <= event.pos[0] <= variables.button_oval.image_area.x + variables.button_oval.image_area.width and \
                    variables.button_oval.image_area.y <= event.pos[1] <= variables.button_oval.image_area.y + variables.button_oval.image_area.height:
                """Ovals button / Кнопка овалов"""
                ButtonFunctions.OvalButtonFunctions(variables, pygame, window)

            elif variables.button_rectangle.image_area.x <= event.pos[0] <= variables.button_rectangle.image_area.x + variables.button_rectangle.image_area.width and \
                    variables.button_rectangle.image_area.y <= event.pos[1] <= variables.button_rectangle.image_area.y + variables.button_rectangle.image_area.height:
                """Rectangles button / Кнопка прямоугольников"""
                ButtonFunctions.RectangleButtonFunctions(variables, pygame, window)

            elif variables.button_wall.image_area.x <= event.pos[0] <= variables.button_wall.image_area.x + variables.button_wall.image_area.width and \
                    variables.button_wall.image_area.y <= event.pos[1] <= variables.button_wall.image_area.y + variables.button_wall.image_area.height:
                """Walls button / Кнопка стен"""
                ButtonFunctions.WallButtonFunctions(variables, pygame, window)

            elif variables.button_delete_beacon.image_area.x <= event.pos[0] <= variables.button_delete_beacon.image_area.x + variables.button_delete_beacon.image_area.width and \
                    variables.button_delete_beacon.image_area.y <= event.pos[1] <= variables.button_delete_beacon.image_area.y + variables.button_delete_beacon.image_area.height:
                """Delete beacons button / Кнопка удаления маяков"""
                ButtonFunctions.BeaconDeleteButton(variables, pygame, window, Parameters.display_color, display_width,
                                                   Parameters.canvas_offset_right, Parameters.canvas_offset_top)

            elif variables.button_delete_oval.image_area.x <= event.pos[0] <= variables.button_delete_oval.image_area.x + variables.button_delete_oval.image_area.width and \
                    variables.button_delete_oval.image_area.y <= event.pos[1] <= variables.button_delete_oval.image_area.y + variables.button_delete_oval.image_area.height:
                """Delete ovals button / Кнопка удаления овалов"""
                ButtonFunctions.OvalDeleteButton(variables, pygame, window)

            elif variables.button_delete_rectangle.image_area.x <= event.pos[0] <= variables.button_delete_rectangle.image_area.x + variables.button_delete_rectangle.image_area.width and \
                    variables.button_delete_rectangle.image_area.y <= event.pos[1] <= variables.button_delete_rectangle.image_area.y + variables.button_delete_rectangle.image_area.height:
                """Delete rectangles button / Кнопка удаления прямоугольников"""
                ButtonFunctions.RectangleDeleteButton(variables, pygame, window)

            elif variables.button_delete_wall.image_area.x <= event.pos[0] <= variables.button_delete_wall.image_area.x + variables.button_delete_wall.image_area.width and \
                    variables.button_delete_wall.image_area.y <= event.pos[1] <= variables.button_delete_wall.image_area.y + variables.button_delete_wall.image_area.height:
                """Delete walls button / Кнопка удаления стен"""
                ButtonFunctions.WallDeleteButton(variables, pygame, window)

            elif variables.button_delete_all.image_area.x <= event.pos[0] <= variables.button_delete_all.image_area.x + variables.button_delete_all.image_area.width and \
                    variables.button_delete_all.image_area.y <= event.pos[1] <= variables.button_delete_all.image_area.y + variables.button_delete_all.image_area.height:
                """All delete button / Кнопка удаления всего"""
                ButtonFunctions.AllDelete(variables, pygame, window, Parameters.display_color, display_width,
                                          Parameters.canvas_offset_right, Parameters.canvas_offset_top)

            elif variables.button_connect.image_area.x <= event.pos[0] <= variables.button_connect.image_area.x + variables.button_connect.image_area.width and \
                    variables.button_connect.image_area.y <= event.pos[1] <= variables.button_connect.image_area.y + variables.button_connect.image_area.height:
                """Connect button / Кнопка соединений"""
                ButtonFunctions.ConnectButtonFunctions(variables, pygame, window, canvas, canvas_place)

            elif variables.button_coverage.image_area.x <= event.pos[0] <= variables.button_coverage.image_area.x + variables.button_coverage.image_area.width and \
                    variables.button_coverage.image_area.y <= event.pos[1] <= variables.button_coverage.image_area.y + variables.button_coverage.image_area.height:
                """Coverage button / Кнопка покрытия"""
                ButtonFunctions.CoverageButtonFunctions(variables, pygame, window, canvas_width, canvas_height)

            elif variables.button_GDOP.image_area.x <= event.pos[0] <= variables.button_GDOP.image_area.x + variables.button_GDOP.image_area.width and \
                    variables.button_GDOP.image_area.y <= event.pos[1] <= variables.button_GDOP.image_area.y + variables.button_GDOP.image_area.height:
                """GDOP button / Кнопка GDOP"""
                ButtonFunctions.GDOPButtonFunctions(variables, pygame, window, canvas_width, canvas_height)

            elif variables.button_axes.image_area.x <= event.pos[0] <= variables.button_axes.image_area.x + variables.button_axes.image_area.width and \
                    variables.button_axes.image_area.y <= event.pos[1] <= variables.button_axes.image_area.y + variables.button_axes.image_area.height:
                """Axes displaying button / Кнопка отображения осей"""
                ButtonFunctions.AxesButton(variables, pygame, window)

            elif variables.button_ruler.image_area.x <= event.pos[0] <= variables.button_ruler.image_area.x + variables.button_ruler.image_area.width and \
                    variables.button_ruler.image_area.y <= event.pos[1] <= variables.button_ruler.image_area.y + variables.button_ruler.image_area.height:
                """Ruler button / Кнопка включения линейки"""
                ButtonFunctions.RulerButton(pygame, window, variables)

            elif variables.button_save.image_area.x <= event.pos[0] <= variables.button_save.image_area.x + variables.button_save.image_area.width and \
                    variables.button_save.image_area.y <= event.pos[1] <= variables.button_save.image_area.y + variables.button_save.image_area.height:
                """Save configuration button / Кнопка сохранения конфигурации"""
                ButtonFunctions.SaveButton(pygame, window, canvas, variables, canvas_width, canvas_height)

            elif variables.button_load.image_area.x <= event.pos[0] <= variables.button_load.image_area.x + variables.button_load.image_area.width and \
                    variables.button_load.image_area.y <= event.pos[1] <= variables.button_load.image_area.y + variables.button_load.image_area.height:
                """Load configuration button / Кнопка загрузки конфигурации"""
                ButtonFunctions.LoadButton(pygame, window, canvas, variables, canvas_width, canvas_height)


            elif variables.button_save_image.image_area.x <= event.pos[0] <= variables.button_save_image.image_area.x + variables.button_save_image.image_area.width and \
                    variables.button_save_image.image_area.y <= event.pos[1] <= variables.button_save_image.image_area.y + variables.button_save_image.image_area.height:
                """Save image button / Кнопка сохранения фотографии холста"""
                ButtonFunctions.SaveImageButton(pygame, window, canvas, variables, canvas_width, canvas_height)

            elif variables.button_load_plan.image_area.x <= event.pos[0] <= variables.button_load_plan.image_area.x + variables.button_load_plan.image_area.width and \
                    variables.button_load_plan.image_area.y <= event.pos[1] <= variables.button_load_plan.image_area.y + variables.button_load_plan.image_area.height:
                """Load plan button / Кнопка загрузки плана помещения"""
                ButtonFunctions.LoadPlanButton(pygame, window, canvas, variables, canvas_width, canvas_height)

            elif variables.load_plan_flag and \
                    variables.button_enabled_disabled_plan.image_area.x <= event.pos[0] <= variables.button_enabled_disabled_plan.image_area.x + variables.button_enabled_disabled_plan.image_area.width and \
                    variables.button_enabled_disabled_plan.image_area.y <= event.pos[1] <= variables.button_enabled_disabled_plan.image_area.y + variables.button_enabled_disabled_plan.image_area.height:
                """Disabled or enabled plan button / Кнопка показать или убрать план помещения"""
                ButtonFunctions.EnabledDisabledPlanButton(pygame, window, variables)

            elif variables.load_plan_flag and \
                    variables.button_delete_plan.image_area.x <= event.pos[0] <= variables.button_delete_plan.image_area.x + variables.button_delete_plan.image_area.width and \
                    variables.button_delete_plan.image_area.y <= event.pos[1] <= variables.button_delete_plan.image_area.y + variables.button_delete_plan.image_area.height:
                """Delete plan button / Удаление плана помещения"""
                ButtonFunctions.DeletePlanButton(pygame, window, variables)

            elif variables.button_choice_ToF_method.image_area.x <= event.pos[0] <= variables.button_choice_ToF_method.image_area.x + variables.button_choice_ToF_method.image_area.width and \
                    variables.button_choice_ToF_method.image_area.y <= event.pos[1] <= variables.button_choice_ToF_method.image_area.y + variables.button_choice_ToF_method.image_area.height:
                """Button choice ToF / TDoA method / Кнопка выбора ToF / TDoA метода"""
                ButtonFunctions.ToFButton(pygame, window, variables)

            elif variables.button_choice_TDoA_method.image_area.x <= event.pos[0] <= variables.button_choice_TDoA_method.image_area.x + variables.button_choice_TDoA_method.image_area.width and \
                    variables.button_choice_TDoA_method.image_area.y <= event.pos[1] <= variables.button_choice_TDoA_method.image_area.y + variables.button_choice_TDoA_method.image_area.height:
                """Button choice ToF / TDoA method / Кнопка выбора ToF / TDoA метода"""
                ButtonFunctions.TDoAButton(pygame, window, variables)

            elif Parameters.canvas_offset_left <= event.pos[0] <= display_width - Parameters.canvas_offset_right and \
                    Parameters.canvas_offset_top <= event.pos[1] <= display_height - Parameters.canvas_offset_bottom:
                """Processing of clicks on the canvas / Обработка кликов по холсту"""
                Mouse.MouseButtonDownLeft(event.pos[0] - Parameters.canvas_offset_left, event.pos[1] - Parameters.canvas_offset_top,
                                          variables, pygame, window, display_width,
                                          display_height, canvas_width, canvas_height, Parameters.canvas_offset_top, Parameters.canvas_offset_right)

            elif int(Parameters.canvas_offset_left + canvas_width - 55 / 2) <= event.pos[0] <= int(
                    Parameters.canvas_offset_left + canvas_width - 55 / 2) + 55 and \
                    int(Parameters.canvas_offset_top + canvas_height + 13) <= event.pos[1] <= int(Parameters.canvas_offset_top + canvas_height + 13) + 16:
                """13 пикселей смещение сверху для выравнивания по высоте"""
                """Input coordinates button on the x-axis / Кнопка воода координат по оси x"""
                variables.input_axes_x_flag = True
                variables.input_axes_y_flag = False
                Axes(pygame, window, variables, display_width, display_height, canvas_width, canvas_height, True, False)
            elif 5 <= event.pos[0] <= 5 + 55 and \
                    int(Parameters.canvas_offset_top - 7) <= event.pos[1] <= int(Parameters.canvas_offset_top - 7) + 16:
                """7 пикселей смещение сверху для выравнивания по высоте"""
                """Input coordinates button on the y-axis / Кнопка воода координат по оси y"""
                variables.input_axes_y_flag = True
                variables.input_axes_x_flag = False
                Axes(pygame, window, variables, display_width, display_height, canvas_width, canvas_height, False, True)

        elif event.button == 3:
            """Right mouse buttom press / Нажатие правой кнопки мыши"""
            Mouse.MouseButtonDownRight(event.pos[0] - Parameters.canvas_offset_left,
                                       event.pos[1] - Parameters.canvas_offset_top,
                                       variables, pygame, window, Parameters.display_color, display_width,
                                       Parameters.canvas_offset_right, Parameters.canvas_offset_top)
        elif event.button == 4:
            """Wheel mouse buttom down / Прокручивание колесика мыши вниз"""
            Mouse.MouseWheel(event.pos[0] - Parameters.canvas_offset_left, event.pos[1] - Parameters.canvas_offset_top,
                             1, canvas_height, variables, pygame, window)

        elif event.button == 5:
            """Wheel mouse buttom up / Прокручивание колесика мыши вверх"""
            Mouse.MouseWheel(event.pos[0] - Parameters.canvas_offset_left, event.pos[1] - Parameters.canvas_offset_top,
                             -1, canvas_height, variables, pygame, window)

    elif event.type == pygame.MOUSEMOTION:
        """Mouse motion / Движение мыши"""
        Mouse.MouseMotion(event.pos[0] - Parameters.canvas_offset_left, event.pos[1] - Parameters.canvas_offset_top,
                          canvas_width, canvas_height, variables, display_width, display_height,
                          pygame, window, Parameters.canvas_offset_top, Parameters.canvas_offset_right)

    elif event.type == pygame.MOUSEBUTTONUP:
        """Release mouse / Отпускание мыши"""
        if event.button == 1:
            """Left mouse button release / Отпускание левой кнопки мыши"""
            Mouse.MouseButtonUpLeft(variables)

    elif event.type == pygame.KEYDOWN and variables.input_axes_x_flag:
        """Input coordinates on the x-axis/ Ввод координат по оси x"""
        if event.key == pygame.K_RETURN:
            variables.input_axes_x_flag = False
            Axes(pygame, window, variables, display_width, display_height, canvas_width, canvas_height, False, False)
        elif event.key == pygame.K_BACKSPACE:
            variables.text_axes_max_x = variables.text_axes_max_x[:-1]
            if variables.text_axes_max_x == '':
                variables.axes_max_x = 0
            elif variables.text_axes_max_x[-1] == '.':
                variables.axes_max_x = round(float(str(variables.text_axes_max_x + '0')), 2)

            else:
                variables.axes_max_x = round(float(variables.text_axes_max_x), 2)
            Axes(pygame, window, variables, display_width, display_height, canvas_width, canvas_height, True, False)
        else:
            if len(variables.text_axes_max_x) <= 7 and variables.text_axes_max_x != '0':
                dot_flag = False
                for symbol in variables.text_axes_max_x:
                    if symbol == '.':
                        dot_flag = True
                if event.unicode == '.' and variables.text_axes_max_x != '' and not dot_flag and variables.text_axes_max_x[-1] != '.':
                    variables.text_axes_max_x += event.unicode
                    variables.axes_max_x = round(float(str(variables.text_axes_max_x + '0')), 2)
                    Axes(pygame, window, variables, display_width, display_height, canvas_width, canvas_height, True, False)
                elif event.unicode.isdigit():
                    variables.text_axes_max_x += event.unicode
                    variables.axes_max_x = round(float(variables.text_axes_max_x), 2)
                    Axes(pygame, window, variables, display_width, display_height, canvas_width, canvas_height, True, False)

    elif event.type == pygame.KEYDOWN and variables.input_axes_y_flag:
        """Input coordinates on the y-axis/ Ввод координат по оси y"""
        if event.key == pygame.K_RETURN:
            variables.input_axes_y_flag = False
            Axes(pygame, window, variables, display_width, display_height, canvas_width, canvas_height, False, False)
        elif event.key == pygame.K_BACKSPACE:
            variables.text_axes_max_y = variables.text_axes_max_y[:-1]
            if variables.text_axes_max_y == '':
                variables.axes_max_y = 0
            elif variables.text_axes_max_y[-1] == '.':
                variables.axes_max_y = round(float(str(variables.text_axes_max_y + '0')), 2)

            else:
                variables.axes_max_y = round(float(variables.text_axes_max_y), 2)
            Axes(pygame, window, variables, display_width, display_height, canvas_width, canvas_height, False, True)
        else:
            if len(variables.text_axes_max_y) <= 7 and variables.text_axes_max_y != '0':
                dot_flag = False
                for symbol in variables.text_axes_max_y:
                    if symbol == '.':
                        dot_flag = True
                if event.unicode == '.' and variables.text_axes_max_y != '' and not dot_flag and variables.text_axes_max_y[-1] != '.':
                    variables.text_axes_max_y += event.unicode
                    variables.axes_max_y = round(float(str(variables.text_axes_max_y + '0')), 2)
                    Axes(pygame, window, variables, display_width, display_height, canvas_width, canvas_height, False, True)
                elif event.unicode.isdigit():
                    variables.text_axes_max_y += event.unicode
                    variables.axes_max_y = round(float(variables.text_axes_max_y), 2)
                    Axes(pygame, window, variables, display_width, display_height, canvas_width, canvas_height, False, True)

    elif event.type == pygame.KEYDOWN and variables.input_beacon_ID_flag:
        """Input beacon's ID / Ввод ID маяка"""
        if event.key == pygame.K_RETURN:
            variables.input_beacon_ID_flag = False
        elif event.key == pygame.K_BACKSPACE:
            text_ID = variables.refactor_beacon.ID
            text_ID = text_ID[:-1]
            variables.refactor_beacon.ID = text_ID
        else:
            text_ID = variables.refactor_beacon.ID
            if len(text_ID) <= 9:
                text_ID += event.unicode
                variables.refactor_beacon.ID = text_ID
        INFO_BOARD.BeaconsInfo(display_width, display_height, pygame, window, variables.info_beacon,
                               Parameters.display_color, Parameters.canvas_offset_top, Parameters.canvas_offset_right, variables)

    elif event.type == pygame.KEYDOWN and variables.input_beacon_x_flag:
        """Input coordinate x beacon's/ Ввод координаты x маяка"""
        if event.key == pygame.K_RETURN:
            variables.input_beacon_x_flag = False
        elif event.key == pygame.K_BACKSPACE:
            variables.refactor_beacon.user_x = variables.refactor_beacon.user_x[:-1]
            if variables.refactor_beacon.user_x == '':
                variables.refactor_beacon.x = 0
            elif variables.refactor_beacon.user_x[-1] == '.':
                variables.refactor_beacon.x = round(float(float(variables.refactor_beacon.user_x + '0') / variables.units_per_pixel_x), 2)
            else:
                variables.refactor_beacon.x = round(float(float(variables.refactor_beacon.user_x) / variables.units_per_pixel_x), 2)
        else:
            if event.unicode.isdigit() or event.unicode == '.':
                dot_flag = False
                double_dot_flag = False
                for symbol in variables.refactor_beacon.user_x:
                    if symbol == '.':
                        dot_flag = True
                if dot_flag and event.unicode == '.':
                    double_dot_flag = True
                if event.unicode == '.' and variables.refactor_beacon.user_x != '' and not dot_flag and \
                        variables.refactor_beacon.user_x[-1] != '.':
                    variables.refactor_beacon.user_x += event.unicode
                    variables.refactor_beacon.x = round(float(float(variables.refactor_beacon.user_x + '0') / variables.units_per_pixel_x))
                elif variables.refactor_beacon.user_x == '':
                    """Проверка на пустоту, т.к. в последующем уловии есть проверка с использованием этой переменной"""
                    variables.refactor_beacon.user_x += event.unicode
                    variables.refactor_beacon.x = round(float(float(variables.refactor_beacon.user_x) / variables.units_per_pixel_x), 2)
                elif not double_dot_flag and 0 <= float(variables.refactor_beacon.user_x + event.unicode) <= variables.axes_max_x and \
                        variables.refactor_beacon.user_x != '0' and len(variables.refactor_beacon.user_x + event.unicode) <= 7:
                    variables.refactor_beacon.user_x += event.unicode
                    variables.refactor_beacon.x = round(float(float(variables.refactor_beacon.user_x) / variables.units_per_pixel_x), 2)
        INFO_BOARD.BeaconsInfo(display_width, display_height, pygame, window, variables.info_beacon,
                               Parameters.display_color, Parameters.canvas_offset_top, Parameters.canvas_offset_right, variables)
        variables.GDOP_enabled_flag = False
        variables.coverage_enabled_flag = False
        variables.button_coverage.NoPress(pygame, window)
        variables.button_GDOP.NoPress(pygame, window)

    elif event.type == pygame.KEYDOWN and variables.input_beacon_y_flag:
        """Input coordinate y beacon's/ Ввод координаты y маяка"""
        if event.key == pygame.K_RETURN:
            variables.input_beacon_y_flag = False
        elif event.key == pygame.K_BACKSPACE:
            variables.refactor_beacon.user_y = variables.refactor_beacon.user_y[:-1]
            if variables.refactor_beacon.user_y == '':
                variables.refactor_beacon.y = 0
            elif variables.refactor_beacon.user_y[-1] == '.':
                variables.refactor_beacon.y = round(float((canvas_height * variables.units_per_pixel_y - float(variables.refactor_beacon.user_y + '0'))
                                                          / variables.units_per_pixel_y), 2)
            else:
                variables.refactor_beacon.y = round(float((canvas_height * variables.units_per_pixel_y - float(variables.refactor_beacon.user_y))
                                                          / variables.units_per_pixel_y), 2)
        else:
            if event.unicode.isdigit() or event.unicode == '.':
                dot_flag = False
                double_dot_flag = False
                for symbol in variables.refactor_beacon.user_y:
                    if symbol == '.':
                        dot_flag = True
                if dot_flag and event.unicode == '.':
                    double_dot_flag = True
                if event.unicode == '.' and variables.refactor_beacon.user_y != '' and not dot_flag and \
                        variables.refactor_beacon.user_y[-1] != '.':
                    variables.refactor_beacon.user_y += event.unicode
                    variables.refactor_beacon.y = round(float((canvas_height * variables.units_per_pixel_y - float(variables.refactor_beacon.user_y + '0'))
                                                              / variables.units_per_pixel_y), 2)
                elif variables.refactor_beacon.user_y == '':
                    """Проверка на пустоту, т.к. в последующем уловии есть проверка с использованием этой переменной"""
                    variables.refactor_beacon.user_y += event.unicode
                    variables.refactor_beacon.y = round(float((canvas_height * variables.units_per_pixel_y - float(variables.refactor_beacon.user_y))
                                                              / variables.units_per_pixel_y), 2)
                elif not double_dot_flag and 0 <= float(variables.refactor_beacon.user_y + event.unicode) <= variables.axes_max_y and \
                        variables.refactor_beacon.user_y != '0' and len(variables.refactor_beacon.user_y + event.unicode) <= 7:
                    variables.refactor_beacon.user_y += event.unicode
                    variables.refactor_beacon.y = round(float((canvas_height * variables.units_per_pixel_y - float(variables.refactor_beacon.user_y))
                                                              / variables.units_per_pixel_y), 2)
        INFO_BOARD.BeaconsInfo(display_width, display_height, pygame, window, variables.info_beacon,
                               Parameters.display_color, Parameters.canvas_offset_top, Parameters.canvas_offset_right, variables)
        variables.GDOP_enabled_flag = False
        variables.coverage_enabled_flag = False
        variables.button_coverage.NoPress(pygame, window)
        variables.button_GDOP.NoPress(pygame, window)
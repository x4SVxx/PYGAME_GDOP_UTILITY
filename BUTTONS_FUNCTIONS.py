from CONNECT import Connect
from COVERAGE import Coverage
from GDOP import GDOP
import sys
from PyQt5.QtWidgets import QApplication
import LOADER_SAVER
import time
import PARAMETERS as Parameters
from BUTTON import Button


def ButtonsCreate(pygame, window, variables, display_width, display_height):

    variables.button_close = Button(Parameters.display_color, pygame, window,
                                    (display_width - Parameters.button_close_width - Parameters.button_close_right_offset,
                                     Parameters.buttons_top_offset,
                                     Parameters.button_close_width,
                                     Parameters.button_close_height),
                                    'Images/button_close.png', 'Images/button_close.png')

    variables.button_beacon = Button(Parameters.display_color, pygame, window,
                                     (Parameters.button_beacon_left_offset,
                                      Parameters.buttons_top_offset,
                                      Parameters.buttons_width,
                                      Parameters.buttons_height),
                                     'Images/button_beacon.png', 'Images/press_button_beacon.png')

    variables.button_oval = Button(Parameters.display_color, pygame, window,
                                   (variables.button_beacon.image_area.x + Parameters.buttons_width + Parameters.button_beacon_and_buttons_barriers_offset,
                                    Parameters.buttons_top_offset,
                                    Parameters.buttons_width,
                                    Parameters.buttons_height),
                                   'Images/button_oval.png', 'Images/press_button_oval.png')

    variables.button_rectangle = Button(Parameters.display_color, pygame, window,
                                        (variables.button_oval.image_area.x + Parameters.buttons_width + Parameters.buttons_group_offset,
                                         Parameters.buttons_top_offset,
                                         Parameters.buttons_width,
                                         Parameters.buttons_height),
                                        'Images/button_rectangle.png', 'Images/press_button_rectangle.png')

    variables.button_wall = Button(Parameters.display_color, pygame, window,
                                   (variables.button_rectangle.image_area.x + Parameters.buttons_width + Parameters.buttons_group_offset,
                                    Parameters.buttons_top_offset,
                                    Parameters.buttons_width,
                                    Parameters.buttons_height),
                                   'Images/button_wall.png', 'Images/press_button_wall.png')

    variables.button_axes = Button(Parameters.display_color, pygame, window,
                                   (variables.button_wall.image_area.x + Parameters.buttons_width + Parameters.buttons_barriers_and_buttons_options_offset,
                                    Parameters.buttons_top_offset,
                                    Parameters.buttons_width,
                                    Parameters.buttons_height),
                                   'Images/axes.png', 'Images/press_axes.png')

    variables.button_ruler = Button(Parameters.display_color, pygame, window,
                                    (variables.button_axes.image_area.x + Parameters.buttons_width + Parameters.buttons_options_group_offset,
                                     Parameters.buttons_top_offset,
                                     Parameters.buttons_width,
                                     Parameters.buttons_height),
                                    'Images/button_ruler.png', 'Images/press_button_ruler.png')

    """По умолчанию оси сразу включены"""
    variables.button_axes.Press(pygame, window)

    variables.button_connect = Button(Parameters.display_color, pygame, window,
                                      (variables.button_ruler.image_area.x + Parameters.buttons_width + Parameters.buttons_options_group_offset,
                                       Parameters.buttons_top_offset,
                                       Parameters.buttons_width,
                                       Parameters.buttons_height),
                                      'Images/connect.png', 'Images/press_connect.png')

    variables.button_coverage = Button(Parameters.display_color, pygame, window,
                                       (variables.button_connect.image_area.x + Parameters.buttons_width + Parameters.buttons_options_group_offset,
                                        Parameters.buttons_top_offset,
                                        Parameters.buttons_width,
                                        Parameters.buttons_height),
                                       'Images/coverage.png', 'Images/press_coverage.png')

    variables.button_GDOP = Button(Parameters.display_color, pygame, window,
                                   (variables.button_coverage.image_area.x + Parameters.buttons_width + Parameters.buttons_options_group_offset,
                                    Parameters.buttons_top_offset,
                                    Parameters.buttons_width,
                                    Parameters.buttons_height),
                                   'Images/GDOP.png', 'Images/press_GDOP.png')

    variables.button_delete_beacon = Button(Parameters.display_color, pygame, window,
                                            (variables.button_GDOP.image_area.x + Parameters.buttons_width + Parameters.buttons_options_and_buttons_delete_offset,
                                             Parameters.buttons_top_offset,
                                             Parameters.buttons_width,
                                             Parameters.buttons_height),
                                            'Images/delete_beacon.png', 'Images/press_delete_beacon.png')

    variables.button_delete_oval = Button(Parameters.display_color, pygame, window,
                                          (variables.button_delete_beacon.image_area.x + Parameters.buttons_width + Parameters.buttons_group_offset,
                                           Parameters.buttons_top_offset,
                                           Parameters.buttons_width,
                                           Parameters.buttons_height),
                                          'Images/delete_oval.png', 'Images/press_delete_oval.png')

    variables.button_delete_rectangle = Button(Parameters.display_color, pygame, window,
                                               (variables.button_delete_oval.image_area.x + Parameters.buttons_width + Parameters.buttons_group_offset,
                                                Parameters.buttons_top_offset,
                                                Parameters.buttons_width,
                                                Parameters.buttons_height),
                                               'Images/delete_rectangle.png', 'Images/press_delete_rectangle.png')

    variables.button_delete_wall = Button(Parameters.display_color, pygame, window,
                                          (variables.button_delete_rectangle.image_area.x + Parameters.buttons_width + Parameters.buttons_group_offset,
                                           Parameters.buttons_top_offset,
                                           Parameters.buttons_width,
                                           Parameters.buttons_height),
                                          'Images/delete_wall.png', 'Images/press_delete_wall.png')

    variables.button_delete_all = Button(Parameters.display_color, pygame, window,
                                         (variables.button_delete_wall.image_area.x + Parameters.buttons_width + Parameters.buttons_group_offset,
                                          Parameters.buttons_top_offset,
                                          Parameters.buttons_width,
                                          Parameters.buttons_height),
                                         'Images/delete_all.png', 'Images/press_delete_all.png')

    variables.button_save = Button(Parameters.display_color, pygame, window,
                                   (Parameters.button_save_offset_left,
                                    display_height - Parameters.button_save_and_load_height * 2 - Parameters.button_save_and_load_offset_bottom * 2,
                                    Parameters.button_save_and_load_width,
                                    Parameters.button_save_and_load_height),
                                   'Images/button_save.png', 'Images/press_button_save.png')

    variables.button_load = Button(Parameters.display_color, pygame, window,
                                   (Parameters.button_save_offset_left,
                                    display_height - Parameters.button_save_and_load_height - Parameters.button_save_and_load_offset_bottom,
                                    Parameters.button_save_and_load_width,
                                    Parameters.button_save_and_load_height),
                                   'Images/button_load.png', 'Images/press_button_load.png')

    variables.button_save_image = Button(Parameters.display_color, pygame, window,
                                         (Parameters.button_save_offset_left + 170,
                                          display_height - Parameters.button_save_and_load_height * 2 - Parameters.button_save_and_load_offset_bottom * 2,
                                          Parameters.button_save_and_load_width,
                                          Parameters.button_save_and_load_height),
                                         'Images/button_save_image.png', 'Images/press_button_save_image.png')

    variables.button_load_plan = Button(Parameters.display_color, pygame, window,
                                        (Parameters.button_save_offset_left + 170,
                                         display_height - Parameters.button_save_and_load_height - Parameters.button_save_and_load_offset_bottom,
                                         Parameters.button_save_and_load_width,
                                         Parameters.button_save_and_load_height),
                                        'Images/button_load_plan.png', 'Images/press_button_load_plan.png')

    variables.button_choice_ToF_method = Button(Parameters.display_color, pygame, window,
                                                (variables.button_GDOP.image_area.x + variables.button_GDOP.image_area.width + 10,
                                                 variables.button_GDOP.image_area.y + 1,
                                                 Parameters.buttons_choice_width,
                                                 Parameters.buttons_choice_height),
                                                'Images/button_choice.png', 'Images/press_button_choice.png')

    """По умолчанию сразу выбрат ToF метод"""
    variables.button_choice_ToF_method.Press(pygame, window)

    variables.button_choice_TDoA_method = Button(Parameters.display_color, pygame, window,
                                                 (variables.button_GDOP.image_area.x + variables.button_GDOP.image_area.width + 10,
                                                  variables.button_GDOP.image_area.y + Parameters.buttons_choice_width + 2,
                                                  Parameters.buttons_choice_width,
                                                  Parameters.buttons_choice_height),
                                                 'Images/button_choice.png', 'Images/press_button_choice.png')

def ButtonsTextCreate(window, variables):

    beacon_text = Parameters.buttons_font.render('BEACON', True, (0, 0, 0))
    variables.beacon_text_place = beacon_text.get_rect(center=(variables.button_beacon.image_area.x + variables.button_beacon.image_area.width / 2,
                                                               variables.button_beacon.image_area.y + variables.button_beacon.image_area.height + 10))
    window.blit(beacon_text, variables.beacon_text_place)

    barriers_text = Parameters.buttons_font.render('BARRIERS', True, (0, 0, 0))
    variables.barriers_text_place = barriers_text.get_rect(center=(variables.button_wall.image_area.x - Parameters.buttons_group_offset / 2,
                                                                   variables.button_wall.image_area.y + Parameters.buttons_width + 10))
    window.blit(barriers_text, variables.barriers_text_place)

    axes_text = Parameters.buttons_font.render('AXES', True, (0, 0, 0))
    variables.axes_text_place = axes_text.get_rect(center=(variables.button_axes.image_area.x + variables.button_axes.image_area.width / 2,
                                                           variables.button_axes.image_area.y + variables.button_axes.image_area.height + 10))
    window.blit(axes_text, variables.axes_text_place)

    ruler_text = Parameters.buttons_font.render('RULER', True, (0, 0, 0))
    variables.ruler_text_place = ruler_text.get_rect(center=(variables.button_ruler.image_area.x + variables.button_ruler.image_area.width / 2,
                                                             variables.button_ruler.image_area.y +variables.button_ruler.image_area.height + 10))
    window.blit(ruler_text, variables.ruler_text_place)

    connect_text = Parameters.buttons_font.render('CONNECT', True, (0, 0, 0))
    variables.connect_text_place = connect_text.get_rect(center=(variables.button_connect.image_area.x + variables.button_connect.image_area.width / 2,
                                                                 variables.button_connect.image_area.y + variables.button_connect.image_area.height + 10))
    window.blit(connect_text, variables.connect_text_place)

    coverage_text = Parameters.buttons_font.render('COVERAGE', True, (0, 0, 0))
    variables.coverage_text_place = coverage_text.get_rect(center=(variables.button_coverage.image_area.x + variables.button_coverage.image_area.width / 2,
                                                                   variables.button_coverage.image_area.y + variables.button_coverage.image_area.height + 10))
    window.blit(coverage_text, variables.coverage_text_place)

    GDOP_text = Parameters.buttons_font.render('GDOP', True, (0, 0, 0))
    variables.GDOP_text_place = GDOP_text.get_rect(center=(variables.button_GDOP.image_area.x + variables.button_GDOP.image_area.width / 2,
                                                           variables.button_GDOP.image_area.y + variables.button_GDOP.image_area.height + 10))
    window.blit(GDOP_text, variables.GDOP_text_place)

    ToF_text = Parameters.buttons_font.render('ToF', True, (0, 0, 0))
    variables.ToF_text_place = ToF_text.get_rect(center=(0, variables.button_choice_ToF_method.image_area.y + variables.button_choice_ToF_method.image_area.height / 2))
    variables.ToF_text_place.x = variables.button_choice_ToF_method.image_area.x + variables.button_choice_ToF_method.image_area.width + 5
    window.blit(ToF_text, variables.ToF_text_place)

    TDoA_text = Parameters.buttons_font.render('TDoA', True, (0, 0, 0))
    variables.TDoA_text_place = TDoA_text.get_rect(center=(0, variables.button_choice_TDoA_method.image_area.y + variables.button_choice_TDoA_method.image_area.height / 2))
    variables.TDoA_text_place.x = variables.button_choice_TDoA_method.image_area.x + variables.button_choice_TDoA_method.image_area.width + 5
    window.blit(TDoA_text, variables.TDoA_text_place)

    delete_text = Parameters.buttons_font.render('DELETE', True, (0, 0, 0))
    variables.delete_text_place = delete_text.get_rect(center=(variables.button_delete_rectangle.image_area.x + Parameters.buttons_width / 2,
                                                               variables.button_delete_rectangle.image_area.y + Parameters.buttons_width + 10))
    window.blit(delete_text, variables.delete_text_place)

    save_text = Parameters.buttons_font.render('SAVE CONFIGURATION', True, (0, 0, 0))
    variables.save_text_place = save_text.get_rect(center=(variables.button_save.image_area.x + Parameters.button_save_and_load_width + 5,
                                                           variables.button_save.image_area.y + variables.button_save.image_area.height / 2))
    variables.save_text_place.x = variables.button_save.image_area.x + Parameters.button_save_and_load_width + 5
    window.blit(save_text, variables.save_text_place)

    load_text = Parameters.buttons_font.render('LOAD CONFIGURATION', True, (0, 0, 0))
    variables.load_text_place = load_text.get_rect(center=(variables.button_load.image_area.x + Parameters.button_save_and_load_width + 5,
                                                           variables.button_load.image_area.y + variables.button_load.image_area.height / 2))
    variables.load_text_place.x = variables.button_load.image_area.x + Parameters.button_save_and_load_width + 5
    window.blit(load_text, variables.load_text_place)

    save_image_text = Parameters.buttons_font.render('SAVE IMAGE', True, (0, 0, 0))
    variables.save_image_text_place = save_image_text.get_rect(center=(variables.button_save_image.image_area.x + Parameters.button_save_and_load_width + 5,
                                                                       variables.button_save_image.image_area.y + variables.button_save_image.image_area.height / 2))
    variables.save_image_text_place.x = variables.button_save_image.image_area.x + Parameters.button_save_and_load_width + 5
    window.blit(save_image_text, variables.save_image_text_place)

    load_plan_text = Parameters.buttons_font.render('LOAD PLAN', True, (0, 0, 0))
    variables.load_plan_text_place = load_plan_text.get_rect(center=(variables.button_load_plan.image_area.x + Parameters.button_save_and_load_width + 5,
                                                                       variables.button_load_plan.image_area.y + variables.button_load_plan.image_area.height / 2))
    variables.load_plan_text_place.x = variables.button_load_plan.image_area.x + Parameters.button_save_and_load_width + 5
    window.blit(load_plan_text, variables.load_plan_text_place)

def CloseButtonFunctions(pygame):
    pygame.quit()
    sys.exit()

def BeaconButtonFunctions(variables, pygame, window):
    if not variables.beacon_placement_flag:
        variables.beacon_placement_flag = True
        variables.button_beacon.Press(pygame, window)
        variables.oval_placement_flag = False
        variables.rectangle_placement_flag = False
        variables.wall_placement_flag = False
        variables.button_oval.NoPress(pygame, window)
        variables.button_rectangle.NoPress(pygame, window)
        variables.button_wall.NoPress(pygame, window)
        variables.ruler_button_press_flag = False
        variables.button_ruler.NoPress(pygame, window)
    elif variables.beacon_placement_flag:
        variables.beacon_placement_flag = False
        variables.button_beacon.NoPress(pygame, window)

def OvalButtonFunctions(variables, pygame, window):
    if not variables.oval_placement_flag:
        variables.oval_placement_flag = True
        variables.button_oval.Press(pygame, window)
        variables.beacon_placement_flag = False
        variables.rectangle_placement_flag = False
        variables.wall_placement_flag = False
        variables.button_beacon.NoPress(pygame, window)
        variables.button_rectangle.NoPress(pygame, window)
        variables.button_wall.NoPress(pygame, window)
        variables.ruler_button_press_flag = False
        variables.button_ruler.NoPress(pygame, window)
    elif variables.oval_placement_flag:
        variables.oval_placement_flag = False
        variables.button_oval.NoPress(pygame, window)

def RectangleButtonFunctions(variables, pygame, window):
    if not variables.rectangle_placement_flag:
        variables.rectangle_placement_flag = True
        variables.button_rectangle.Press(pygame, window)
        variables.beacon_placement_flag = False
        variables.oval_placement_flag = False
        variables.wall_placement_flag = False
        variables.button_beacon.NoPress(pygame, window)
        variables.button_oval.NoPress(pygame, window)
        variables.button_wall.NoPress(pygame, window)
        variables.ruler_button_press_flag = False
        variables.button_ruler.NoPress(pygame, window)
    elif variables.rectangle_placement_flag:
        variables.rectangle_placement_flag = False
        variables.button_rectangle.NoPress(pygame, window)

def WallButtonFunctions(variables, pygame, window):
    if not variables.wall_placement_flag:
        variables.wall_placement_flag = True
        variables.button_wall.Press(pygame, window)
        variables.beacon_placement_flag = False
        variables.oval_placement_flag = False
        variables.rectangle_placement_flag = False
        variables.button_beacon.NoPress(pygame, window)
        variables.button_oval.NoPress(pygame, window)
        variables.button_rectangle.NoPress(pygame, window)
        variables.ruler_button_press_flag = False
        variables.button_ruler.NoPress(pygame, window)
    elif variables.wall_placement_flag:
        variables.wall_placement_flag = False
        variables.button_wall.NoPress(pygame, window)

def BeaconDeleteButton(variables, pygame, window, display_color, display_width,
                       canvas_offset_right, canvas_offset_top):
    variables.button_delete_beacon.Press(pygame, window)
    time.sleep(0.1)
    variables.button_delete_beacon.NoPress(pygame, window)
    variables.beacons_mas = []
    variables.beacons_count = 0
    variables.info_board_active_flag = False
    """Delete infoboard / Удаление информационного табло"""
    pygame.draw.rect(window, display_color,
                     (display_width - (canvas_offset_right - 30), canvas_offset_top - 10, canvas_offset_right, 400))


def OvalDeleteButton(variables, pygame, window):
    variables.button_delete_oval.Press(pygame, window)
    time.sleep(0.1)
    variables.button_delete_oval.NoPress(pygame, window)
    variables.ovals_mas = []
    variables.ovals_count = 0

def RectangleDeleteButton(variables, pygame, window):
    variables.button_delete_rectangle.Press(pygame, window)
    time.sleep(0.1)
    variables.button_delete_rectangle.NoPress(pygame, window)
    variables.rectangles_mas = []
    variables.rectangles_count = 0

def WallDeleteButton(variables, pygame, window):
    variables.button_delete_wall.Press(pygame, window)
    time.sleep(0.1)
    variables.button_delete_wall.NoPress(pygame, window)
    variables.walls_mas = []
    variables.walls_count = 0

def AllDelete(variables, pygame, window, display_color, display_width, canvas_offset_right, canvas_offset_top):
    variables.button_delete_all.Press(pygame, window)
    time.sleep(0.1)
    variables.button_delete_all.NoPress(pygame, window)
    variables.beacons_mas = []
    variables.beacons_count = 0
    variables.ovals_mas = []
    variables.ovals_count = 0
    variables.rectangles_mas = []
    variables.rectangles_count = 0
    variables.walls_mas = []
    variables.walls_count = 0
    variables.GDOP_enabled_flag = False
    variables.coverage_enabled_flag = False
    variables.connect_enabled_flag = False
    variables.info_board_active_flag = False
    variables.button_connect.NoPress(pygame, window)
    variables.button_coverage.NoPress(pygame, window)
    variables.button_GDOP.NoPress(pygame, window)
    """Delete infoboard / Удаление информационного табло"""
    pygame.draw.rect(window, display_color,
                     (display_width - (canvas_offset_right - 30), canvas_offset_top - 10, canvas_offset_right, 400))


def ConnectButtonFunctions(variables, pygame, window, canvas, canvas_place):
    if not variables.connect_enabled_flag:
        variables.button_connect.Press(pygame, window)
        Connect(variables, window, pygame, canvas, canvas_place,
                variables.beacons_mas, variables.ovals_mas, variables.rectangles_mas, variables.walls_mas)
    else:
        variables.connect_enabled_flag = False
        variables.button_connect.NoPress(pygame, window)

def CoverageButtonFunctions(variables, pygame, window, canvas_width, canvas_height):
    if not variables.coverage_enabled_flag:
        variables.GDOP_enabled_flag = False
        variables.button_GDOP.NoPress(pygame, window)
        variables.button_coverage.Press(pygame, window)
        Coverage(variables, canvas_width, canvas_height, pygame, window)
    else:
        variables.coverage_enabled_flag = False
        variables.button_coverage.NoPress(pygame, window)

def GDOPButtonFunctions(variables, pygame, window, canvas_width, canvas_height):
    if not variables.GDOP_enabled_flag:
        variables.coverage_enabled_flag = False
        variables.button_coverage.NoPress(pygame, window)
        variables.button_GDOP.Press(pygame, window)
        GDOP(variables, canvas_width, canvas_height, pygame, window)
    else:
        variables.GDOP_enabled_flag = False
        variables.button_GDOP.NoPress(pygame, window)

def AxesButton(variables, pygame, window):
    if variables.displaying_axes_flag:
        variables.displaying_axes_flag = False
        variables.button_axes.NoPress(pygame, window)
    else:
        variables.displaying_axes_flag = True
        variables.button_axes.Press(pygame, window)

def RulerButton(pygame, window, variables):
    if not variables.ruler_button_press_flag:
        variables.ruler_button_press_flag = True
        variables.button_ruler.Press(pygame, window)
        variables.beacon_placement_flag = False
        variables.oval_placement_flag = False
        variables.rectangle_placement_flag = False
        variables.wall_placement_flag = False
        variables.button_beacon.NoPress(pygame, window)
        variables.button_oval.NoPress(pygame, window)
        variables.button_rectangle.NoPress(pygame, window)
        variables.button_wall.NoPress(pygame, window)
    elif variables.ruler_button_press_flag:
        variables.ruler_button_press_flag = False
        variables.button_ruler.NoPress(pygame, window)

def ToFButton(pygame, window, variables):
        variables.choice_ToF_method_flag = True
        variables.button_choice_ToF_method.Press(pygame, window)
        variables.choice_TDoA_method_flag = False
        variables.button_choice_TDoA_method.NoPress(pygame, window)
        variables.GDOP_enabled_flag = False
        variables.button_GDOP.NoPress(pygame, window)

def TDoAButton(pygame, window, variables):
        variables.choice_TDoA_method_flag = True
        variables.button_choice_TDoA_method.Press(pygame, window)
        variables.choice_ToF_method_flag = False
        variables.button_choice_ToF_method.NoPress(pygame, window)
        variables.GDOP_enabled_flag = False
        variables.button_GDOP.NoPress(pygame, window)

def SaveButton(pygame, window, canvas, variables, canvas_width, canvas_height,):
    variables.button_save.Press(pygame, window)
    time.sleep(0.1)
    variables.button_save.NoPress(pygame, window)
    app = QApplication(sys.argv)
    saver = LOADER_SAVER.LoaderAndSaver(pygame, window, canvas, variables, canvas_width, canvas_height, 'SAVE')
    app.quit()

def LoadButton(pygame, window, canvas, variables, canvas_width, canvas_height):
    variables.button_load.Press(pygame, window)
    time.sleep(0.1)
    variables.button_load.NoPress(pygame, window)
    app = QApplication(sys.argv)
    loader = LOADER_SAVER.LoaderAndSaver(pygame, window, canvas, variables, canvas_width, canvas_height, 'LOAD')
    app.quit()

def SaveImageButton(pygame, window, canvas, variables, canvas_width, canvas_height):
    variables.button_save_image.Press(pygame, window)
    time.sleep(0.1)
    variables.button_save_image.NoPress(pygame, window)
    app = QApplication(sys.argv)
    saver_image = LOADER_SAVER.LoaderAndSaver(pygame, window, canvas, variables, canvas_width, canvas_height, 'SAVE_IMAGE')
    app.quit()

def LoadPlanButton(pygame, window, canvas, variables, canvas_width, canvas_height):
    variables.button_load_plan.Press(pygame, window)
    app = QApplication(sys.argv)
    loader_plan = LOADER_SAVER.LoaderAndSaver(pygame, window, canvas, variables, canvas_width, canvas_height, 'LOAD_PLAN')
    app.quit()
    if variables.load_plan_flag:
        variables.button_enabled_disabled_plan = Button(Parameters.display_color, pygame, window,
                                                        (variables.load_plan_text_place.x + variables.load_plan_text_place.width + 10,
                                                         variables.button_load_plan.image_area.y,
                                                         Parameters.button_save_and_load_width,
                                                         Parameters.button_save_and_load_height),
                                                        'Images/button_enabled_plan.png', 'Images/button_disabled_plan.png')

        enabled_plan_text = Parameters.buttons_font.render('ENABLED', True, (0, 0, 0))
        variables.enabled_plan_text_place = enabled_plan_text.get_rect(center = (variables.button_enabled_disabled_plan.image_area.x + Parameters.button_save_and_load_width + 5,
                                                                                 variables.button_enabled_disabled_plan.image_area.y + variables.button_enabled_disabled_plan.image_area.height))
        variables.enabled_plan_text_place.x = variables.button_enabled_disabled_plan.image_area.x + Parameters.button_save_and_load_width + 5
        variables.enabled_plan_text_place.y = variables.button_enabled_disabled_plan.image_area.y + variables.button_enabled_disabled_plan.image_area.height - \
                                              variables.enabled_plan_text_place.height
        window.blit(enabled_plan_text, variables.enabled_plan_text_place)

        disabled_plan_text = Parameters.buttons_font.render('DISABLED', True, (0, 0, 0))
        variables.disabled_plan_text_place = disabled_plan_text.get_rect(center=(variables.button_enabled_disabled_plan.image_area.x + Parameters.button_save_and_load_width + 5,
                                                                                 variables.button_enabled_disabled_plan.image_area.y + variables.button_enabled_disabled_plan.image_area.height))
        variables.disabled_plan_text_place.x = variables.button_enabled_disabled_plan.image_area.x + Parameters.button_save_and_load_width + 5
        variables.disabled_plan_text_place.y = variables.button_enabled_disabled_plan.image_area.y + variables.button_enabled_disabled_plan.image_area.height / 2 - \
                                               variables.disabled_plan_text_place.height
        window.blit(disabled_plan_text, variables.disabled_plan_text_place)

        variables.enabled_plan_flag = True

        variables.button_delete_plan = Button(Parameters.display_color, pygame, window,
                                              (variables.disabled_plan_text_place.x + variables.disabled_plan_text_place.width + 10,
                                               variables.button_load_plan.image_area.y,
                                               Parameters.button_save_and_load_width,
                                               Parameters.button_save_and_load_height),
                                              'Images/delete_plan.png', 'Images/press_delete_plan.png')

        delete_plan_text = Parameters.buttons_font.render('DELETE PLAN', True, (0, 0, 0))
        variables.delete_plan_text_place = delete_plan_text.get_rect(center=(variables.button_delete_plan.image_area.x + Parameters.button_save_and_load_width + 5,
                                                                             variables.button_delete_plan.image_area.y + variables.button_delete_plan.image_area.height / 2))
        variables.delete_plan_text_place.x = variables.button_delete_plan.image_area.x + Parameters.button_save_and_load_width + 5
        window.blit(delete_plan_text, variables.delete_plan_text_place)

    elif not variables.load_plan_flag:
        variables.load_plan_flag = False
        variables.enabled_plan_flag = False
        variables.button_load_plan.NoPress(pygame, window)

def EnabledDisabledPlanButton(pygame, window, variables):
    if variables.enabled_plan_flag:
        variables.button_enabled_disabled_plan.Press(pygame, window)
        variables.enabled_plan_flag = False
    elif not variables.enabled_plan_flag:
        variables.button_enabled_disabled_plan.NoPress(pygame, window)
        variables.enabled_plan_flag = True

def DeletePlanButton(pygame, window, variables):
    variables.button_delete_plan.Press(pygame, window)
    time.sleep(0.1)
    variables.button_delete_plan.NoPress(pygame, window)
    variables.load_plan_flag = False
    variables.enabled_plan_flag = False
    variables.button_load_plan.NoPress(pygame, window)
    pygame.draw.rect(window, Parameters.display_color, (variables.button_enabled_disabled_plan.image_area.x,
                                                        variables.button_enabled_disabled_plan.image_area.y,
                                                        variables.delete_plan_text_place.y + variables.delete_plan_text_place.width -
                                                        variables.button_enabled_disabled_plan.image_area.x,
                                                        variables.button_enabled_disabled_plan.image_area.height))
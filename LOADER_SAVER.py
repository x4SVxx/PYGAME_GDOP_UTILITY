from PyQt5.QtWidgets import QMainWindow, QFileDialog
from BEACON import  Beacon
from OVAL import Oval
from RECTANGLE import  Rectangle
from WALL import Wall
import PARAMETERS as Parameters
import time


class LoaderAndSaver(QMainWindow):

    def __init__(self, pygame, window, canvas, variables, canvas_width, canvas_height, job_flag):
        super().__init__()
        if job_flag == 'LOAD':
            self.ShowDialogLoad(pygame, window, variables, canvas_height)
        if job_flag == 'SAVE':
            self.ShowDialogSave(variables)
        if job_flag == 'SAVE_IMAGE':
            self.ShowDialogSaveImage(pygame, canvas)
        if job_flag == 'LOAD_PLAN':
            self.ShowDialogLoadPlan(pygame, window, variables, canvas_width, canvas_height)

    def ShowDialogLoad(self, pygame, window, variables, canvas_height):
        try:
            filename = QFileDialog.getOpenFileName(self, 'Load file', '', 'Text Files (*.txt)')[0]
            file = open(filename, 'r')
            incorrect_lines_flag = False
            add_beacon_flag = False
            add_oval_flag = False
            add_rectangle_flag = False
            add_wall_flag = False
            for line in file:
                try:
                    mas_string = line.split()
                    if mas_string[0] == 'beacon':
                        variables.beacons_count += 1
                        beacon_user_x = str(round(float(mas_string[4]), 2))
                        beacon_user_y = str(round(float(mas_string[5]), 2))
                        beacon_ID = str(mas_string[2])
                        variables.beacons_mas.append(Beacon(Parameters.beacon_radius, Parameters.beacon_color,
                                                            variables.beacons_count, beacon_ID, variables, canvas_height,
                                                            beacon_user_x, beacon_user_y))
                        add_beacon_flag = True

                    elif mas_string[0] == 'oval':
                        variables.ovals_count += 1
                        oval_user_x = float(mas_string[2])
                        oval_user_y = float(mas_string[3])
                        oval_user_width = float(mas_string[4])
                        oval_user_height = float(mas_string[5])
                        if oval_user_width <= 0 or oval_user_height <= 0:
                            incorrect_lines_flag = True
                        else:
                            variables.ovals_mas.append(Oval(Parameters.oval_outline_width, Parameters.oval_color, variables.ovals_count, variables,
                                                            canvas_height, oval_user_x, oval_user_y, oval_user_width, oval_user_height))
                            add_oval_flag = True

                    elif mas_string[0] == 'rectangle':
                        variables.rectangles_count += 1
                        rectangle_user_x = float(mas_string[2])
                        rectangle_user_y = float(mas_string[3])
                        rectangle_user_width = float(mas_string[4])
                        rectangle_user_height = float(mas_string[5])
                        if rectangle_user_width <= 0 or rectangle_user_height <= 0:
                            incorrect_lines_flag = True
                        else:
                            variables.rectangles_mas.append(Rectangle(Parameters.oval_outline_width, Parameters.oval_color, variables.ovals_count, variables,
                                                                      canvas_height, rectangle_user_x, rectangle_user_y, rectangle_user_width, rectangle_user_height))
                            add_rectangle_flag = True

                    elif mas_string[0] == 'wall':
                        variables.walls_count += 1
                        wall_side_1_user_x = float(mas_string[2])
                        wall_side_1_user_y = float(mas_string[3])
                        wall_side_2_user_x = float(mas_string[4])
                        wall_side_2_user_y = float(mas_string[5])
                        variables.walls_mas.append(Wall(Parameters.wall_width, Parameters.wall_color, variables.walls_count, variables, canvas_height,
                                                        wall_side_1_user_x, wall_side_1_user_y, wall_side_2_user_x, wall_side_2_user_y))
                        add_wall_flag = True

                    else:
                        incorrect_lines_flag = True

                except:
                    incorrect_lines_flag = True

            file.close()

            if incorrect_lines_flag:
                font = pygame.font.SysFont('ebrima', 16)
                warning_text = font.render('File contains incorrect lines', True, (255, 0, 0))
                warning_text_place = warning_text.get_rect(center=(variables.save_image_text_place.x + variables.save_image_text_place.width + 50,
                                                                   variables.save_image_text_place.y + variables.save_image_text_place.height))
                warning_text_place.x = variables.save_image_text_place.x + variables.save_image_text_place.width + 50
                warning_text_place.y = variables.save_image_text_place.y + variables.save_image_text_place.height - warning_text_place.height
                window.blit(warning_text, warning_text_place)
                pygame.display.update()
                time.sleep(1.5)
                pygame.draw.rect(window, Parameters.display_color, (variables.save_image_text_place.x + variables.save_image_text_place.width + 50,
                                                                    variables.save_image_text_place.y + variables.save_image_text_place.height - warning_text_place.height,
                                                                    warning_text_place.width, warning_text_place.height))

            if not add_beacon_flag and not add_oval_flag and not add_rectangle_flag and not add_wall_flag:
                font = pygame.font.SysFont('ebrima', 14)
                warning_text = font.render('File does not contain the necessary objects', True, (255, 0, 0))
                warning_text_place = warning_text.get_rect(center=(variables.save_image_text_place.x + variables.save_image_text_place.width + 50,
                                                                   variables.save_image_text_place.y + variables.save_image_text_place.height))
                warning_text_place.x = variables.save_image_text_place.x + variables.save_image_text_place.width + 50
                warning_text_place.y = variables.save_image_text_place.y + variables.save_image_text_place.height - warning_text_place.height
                window.blit(warning_text, warning_text_place)
                pygame.display.update()
                time.sleep(1.5)
                pygame.draw.rect(window, Parameters.display_color, (variables.save_image_text_place.x + variables.save_image_text_place.width + 50,
                                                                    variables.save_image_text_place.y + variables.save_image_text_place.height - warning_text_place.height,
                                                                    warning_text_place.width, warning_text_place.height))

            if add_wall_flag or add_oval_flag or add_rectangle_flag or add_wall_flag:
                variables.GDOP_enabled_flag = False
                variables.coverage_enabled_flag = False
                variables.button_coverage.NoPress(pygame, window)
                variables.button_GDOP.NoPress(pygame, window)

        except:
            font = pygame.font.SysFont('ebrima', 16)
            warning_text = font.render('File was not opened', True, (255, 0, 0))
            warning_text_place = warning_text.get_rect(center=(variables.save_image_text_place.x + variables.save_image_text_place.width + 50,
                                                               variables.save_image_text_place.y + variables.save_image_text_place.height))
            warning_text_place.x = variables.save_image_text_place.x + variables.save_image_text_place.width + 50
            warning_text_place.y = variables.save_image_text_place.y + variables.save_image_text_place.height - warning_text_place.height
            window.blit(warning_text, warning_text_place)
            pygame.display.update()
            time.sleep(1.5)
            pygame.draw.rect(window, Parameters.display_color, (variables.save_image_text_place.x + variables.save_image_text_place.width + 50,
                                                                variables.save_image_text_place.y + variables.save_image_text_place.height - warning_text_place.height,
                                                                warning_text_place.width, warning_text_place.height))

    def ShowDialogSave(self, variables):
        if len(variables.beacons_mas) == 0 and len(variables.ovals_mas) == 0:
            pass
        save_as = QFileDialog.getSaveFileName(self, "Save as...", '', 'Text Files (*.txt)')[0]
        if save_as != "":
            output_file = open(save_as, "w+")

            for beacon in variables.beacons_mas:
                output_file.write(''.join('beacon ID: ' + str(beacon.ID) + " " + 'Coordinates_center_x_y: ' +
                                          str(beacon.user_x) + ' ' + str(beacon.user_y) + "\n"))
            for oval in variables.ovals_mas:
                output_file.write(''.join('oval Coordinates_Left_Top_Corner_x_y_and_Width_Height: ' +
                                          str(round(float(oval.user_x), 2)) + ' ' +
                                          str(round(float(oval.user_y), 2)) + ' ' +
                                          str(round(float(oval.user_width), 2)) + ' ' +
                                          str(round(float(oval.user_height), 2)) + "\n"))
            for rectangle in variables.rectangles_mas:
                output_file.write(''.join('rectangle Coordinates_Left_Top_Corner_x_y_and_Width_Height: ' +
                                          str(round(float(rectangle.user_x), 2)) + ' ' +
                                          str(round(float(rectangle.user_y), 2)) + ' ' +
                                          str(round(float(rectangle.user_width), 2)) + ' ' +
                                          str(round(float(rectangle.user_height), 2)) + "\n"))
            for wall in variables.walls_mas:
                output_file.write(''.join('wall Coordinate_first_side_x_y_and_second_side_x_y: ' +
                                          str(round(float(wall.user_x1), 2)) + ' ' +
                                          str(round(float(wall.user_y1), 2)) + ' ' +
                                          str(round(float(wall.user_x2), 2)) + ' ' +
                                          str(round(float(wall.user_y2), 2)) + "\n"))
            output_file.close()

    def ShowDialogSaveImage(self, pygame, canvas):
        save_as = QFileDialog.getSaveFileName(self, "Save as...", '', 'Image Files (*.png)')[0]
        if save_as:
            pygame.image.save(canvas, save_as.title())

    def ShowDialogLoadPlan(self, pygame, window, variables, canvas_width, canvas_height):
        try:
            filename = QFileDialog.getOpenFileName(self, 'Load file', '', 'Image Files (*.png; *.jpeg; *.jpg; *.bmp)')[0]
            variables.plan_image = pygame.image.load(filename)
            variables.plan_image = pygame.transform.scale(variables.plan_image, (canvas_width, canvas_height))
            variables.plan_image.set_alpha(75)  # 0 is fully transparent and 255 fully opaque.

            if variables.load_plan_flag:
                pygame.draw.rect(window, Parameters.display_color, (variables.button_enabled_disabled_plan.image_area.x,
                                                                    variables.button_enabled_disabled_plan.image_area.y,
                                                                    variables.delete_plan_text_place.y + variables.delete_plan_text_place.width -
                                                                    variables.button_enabled_disabled_plan.image_area.x,
                                                                    variables.button_enabled_disabled_plan.image_area.height))

            variables.load_plan_flag = True
        except:
            font = pygame.font.SysFont('ebrima', 16)
            warning_text = font.render('Plan was not opened', True, (255, 0, 0))
            warning_text_place = warning_text.get_rect(center=(variables.save_image_text_place.x + variables.save_image_text_place.width + 50,
                                                               variables.save_image_text_place.y + variables.save_image_text_place.height))
            warning_text_place.x = variables.save_image_text_place.x + variables.save_image_text_place.width + 50
            warning_text_place.y = variables.save_image_text_place.y + variables.save_image_text_place.height - warning_text_place.height
            window.blit(warning_text, warning_text_place)
            pygame.display.update()
            time.sleep(1.5)
            pygame.draw.rect(window, Parameters.display_color, (variables.save_image_text_place.x + variables.save_image_text_place.width + 50,
                                                                variables.save_image_text_place.y + variables.save_image_text_place.height - warning_text_place.height,
                                                                warning_text_place.width, warning_text_place.height))


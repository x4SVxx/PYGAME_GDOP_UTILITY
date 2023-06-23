from BEACON import Beacon
from OVAL import Oval
from WALL import Wall
from RECTANGLE import Rectangle
import PARAMETERS as Parameters
import keyboard
import math
import INFO_BOARD


def MouseButtonDownLeft(x, y, variables, pygame, window, display_width, display_height,
                        canvas_width, canvas_height, canvas_offset_top, canvas_offset_right):
   if not variables.ruler_button_press_flag:
      inside_beacon_flag = False
      for beacon in variables.beacons_mas:
         if pow(x - beacon.x, 2) / pow(beacon.radius, 2) + \
                 pow(y - beacon.y, 2) / pow(beacon.radius, 2) <= 1:
            inside_beacon_flag = True
      if variables.beacon_placement_flag:
         if not inside_beacon_flag:
            variables.beacons_count += 1
            new_beacon = Beacon(Parameters.beacon_radius, Parameters.beacon_color, variables.beacons_count,
                                'Beacon_' + str(variables.beacons_count), variables, canvas_height,
                                x * variables.units_per_pixel_x,
                                canvas_height * variables.units_per_pixel_y - y * variables.units_per_pixel_y)
            variables.info_beacon = new_beacon
            variables.info_board_active_flag = True
            variables.beacons_mas.append(new_beacon)
            INFO_BOARD.BeaconsInfo(display_width, display_height, pygame, window, variables.info_beacon,
                                   Parameters.display_color, canvas_offset_top, canvas_offset_right, variables)
            variables.beacon_posed_flag = True

      elif variables.oval_placement_flag and not inside_beacon_flag:

         variables.ovals_count += 1
         variables.ovals_mas.append(Oval(Parameters.oval_outline_width, Parameters.oval_color, variables.ovals_count, variables, canvas_height,
                                         x * variables.units_per_pixel_x, canvas_height * variables.units_per_pixel_y - y * variables.units_per_pixel_y,
                                         1, 1))
         variables.oval_placement_motion_flag = True
         variables.start_oval_placement_position = (x, y)

      elif variables.rectangle_placement_flag and not inside_beacon_flag:

         variables.rectangles_count += 1
         variables.rectangles_mas.append(Rectangle(Parameters.rectangle_outline_width, Parameters.rectangle_color, variables.rectangles_count, variables, canvas_height,
                                                   x * variables.units_per_pixel_x, canvas_height * variables.units_per_pixel_y - y * variables.units_per_pixel_y,
                                                   1, 1))
         variables.rectangle_placement_motion_flag = True
         variables.start_rectangle_placement_position = (x, y)

      elif variables.wall_placement_flag and not inside_beacon_flag:
         if Parameters.wall_width < x < canvas_width - Parameters.wall_width and \
                 Parameters.wall_width < y < canvas_height - Parameters.wall_width:

            variables.walls_count += 1
            variables.walls_mas.append(Wall(Parameters.wall_width, Parameters.wall_color, variables.walls_count, variables, canvas_height,
                                            x * variables.units_per_pixel_x,
                                            canvas_height * variables.units_per_pixel_y - y * variables.units_per_pixel_y,
                                            (x + 1) * variables.units_per_pixel_x,
                                            canvas_height * variables.units_per_pixel_y - (y + 1) * variables.units_per_pixel_y))
            variables.wall_placement_motion_flag = True
            variables.start_wall_placement_position = (x, y)

      if variables.oval_placement_motion_flag == variables.rectangle_placement_motion_flag == \
              variables.wall_placement_motion_flag == variables.beacon_posed_flag == False:

         for beacon in variables.beacons_mas:
            if pow(x - beacon.x, 2) / pow(beacon.radius, 2) + \
                    pow(y - beacon.y, 2) / pow(beacon.radius, 2) <= 1:
               variables.replace_beacon_flag = True
               variables.delta_beacon_replace_width = x - beacon.x
               variables.delta_beacon_replace_height = y - beacon.y
               variables.replace_object = beacon
               variables.info_board_active_flag = True
               variables.info_beacon = beacon
               INFO_BOARD.BeaconsInfo(display_width, display_height, pygame, window, variables.info_beacon,
                                      Parameters.display_color, canvas_offset_top, canvas_offset_right, variables)

         if not variables.replace_beacon_flag:

            for wall in variables.walls_mas:
               if wall.x1 - wall.width <= x <= wall.x1 + wall.width and wall.y1 - wall.width <= y <= wall.y1 + wall.width:
                  variables.replace_wall_side_1_flag = True
                  variables.replace_object = wall

            if not variables.replace_wall_side_1_flag:

               for wall in variables.walls_mas:
                  if wall.x2 - wall.width <= x <= wall.x2 + wall.width and wall.y2 - wall.width <= y <= wall.y2 + wall.width:
                     variables.replace_wall_side_2_flag = True
                     variables.replace_object = wall

            if not variables.replace_wall_side_1_flag and not variables.replace_wall_side_2_flag:

               for oval in variables.ovals_mas:
                  if pow(x - (oval.x + oval.width / 2), 2) / pow(oval.width / 2, 2) + \
                          pow(y - (oval.y + oval.height / 2), 2) / pow(oval.height / 2, 2) <= 1:
                     if variables.replace_oval_flag:
                        if variables.replace_object.width > oval.width and variables.replace_object.height > oval.height:
                           variables.delta_oval_replace_width = x - oval.x
                           variables.delta_oval_replace_height = y - oval.y
                           variables.replace_object = oval
                     else:
                        variables.replace_oval_flag = True
                        variables.delta_oval_replace_width = x - oval.x
                        variables.delta_oval_replace_height = y - oval.y
                        variables.replace_object = oval

               for rectangle in variables.rectangles_mas:
                  if rectangle.x <= x <= rectangle.x + rectangle.width and rectangle.y <= y <= rectangle.y + rectangle.height:
                     if variables.replace_oval_flag:
                        if variables.replace_object.width > rectangle.width and variables.replace_object.height > rectangle.height:
                           variables.replace_oval_flag = False
                           variables.replace_rectangle_flag = True
                           variables.delta_rectangle_replace_width = x - rectangle.x
                           variables.delta_rectangle_replace_height = y - rectangle.y
                           variables.replace_object = rectangle
                     elif variables.replace_rectangle_flag:
                        if variables.replace_object.width > rectangle.width and variables.replace_object.height > rectangle.height:
                           variables.delta_rectangle_replace_width = x - rectangle.x
                           variables.delta_rectangle_replace_height = y - rectangle.y
                           variables.replace_object = rectangle
                     else:
                        variables.replace_rectangle_flag = True
                        variables.delta_rectangle_replace_width = x - rectangle.x
                        variables.delta_rectangle_replace_height = y - rectangle.y
                        variables.replace_object = rectangle

      variables.beacon_posed_flag = False

      if variables.beacon_placement_flag or variables.oval_placement_flag or variables.wall_placement_flag or \
              variables.rectangle_placement_flag or variables.replace_beacon_flag or variables.replace_oval_flag or \
              variables.replace_rectangle_flag or variables.replace_wall_side_1_flag or variables.replace_wall_side_2_flag:
         variables.GDOP_enabled_flag = False
         variables.coverage_enabled_flag = False
         variables.button_coverage.NoPress(pygame, window)
         variables.button_GDOP.NoPress(pygame, window)

   else:
      variables.ruler_enabled_flag = True
      if x >= canvas_width: x = canvas_width - 2
      if y >= canvas_height: y = canvas_height - 2
      variables.ruler_start_pos = (x, y)
      variables.ruler_finish_pos = (x, y)



def MouseMotion(x, y, canvas_width, canvas_height, variables, display_width, display_height,
                pygame, window, canvas_offset_top, canvas_offset_right):
   if x < 0: x = 0
   if y < 0: y = 0
   if x > canvas_width: x = canvas_width
   if y > canvas_height: y = canvas_height

   if variables.oval_placement_motion_flag:
      new_oval_width = abs(x - variables.start_oval_placement_position[0])
      new_oval_height = abs(y - variables.start_oval_placement_position[1])
      if x < variables.start_oval_placement_position[0]:
         variables.ovals_mas[len(variables.ovals_mas) - 1].user_x = x * variables.units_per_pixel_x
      elif x > variables.start_oval_placement_position[0]:
         variables.ovals_mas[len(variables.ovals_mas) - 1].user_x = variables.start_oval_placement_position[0] * variables.units_per_pixel_x
      variables.ovals_mas[len(variables.ovals_mas) - 1].x = int(variables.ovals_mas[len(variables.ovals_mas) - 1].user_x / variables.units_per_pixel_x)
      if y < variables.start_oval_placement_position[1]:
         variables.ovals_mas[len(variables.ovals_mas) - 1].user_y = canvas_height * variables.units_per_pixel_y - y * variables.units_per_pixel_y
      elif y > variables.start_oval_placement_position[1]:
         variables.ovals_mas[len(variables.ovals_mas) - 1].user_y = canvas_height * variables.units_per_pixel_y - variables.start_oval_placement_position[1] * variables.units_per_pixel_y
      variables.ovals_mas[len(variables.ovals_mas) - 1].y = int((canvas_height * variables.units_per_pixel_y - variables.ovals_mas[len(variables.ovals_mas) - 1].user_y) / variables.units_per_pixel_y)

      variables.ovals_mas[len(variables.ovals_mas) - 1].user_width = new_oval_width * variables.units_per_pixel_x
      variables.ovals_mas[len(variables.ovals_mas) - 1].user_height = new_oval_height * variables.units_per_pixel_y
      variables.ovals_mas[len(variables.ovals_mas) - 1].width = int(variables.ovals_mas[len(variables.ovals_mas) - 1].user_width / variables.units_per_pixel_x)
      variables.ovals_mas[len(variables.ovals_mas) - 1].height = int(variables.ovals_mas[len(variables.ovals_mas) - 1].user_height / variables.units_per_pixel_y)
      if variables.ovals_mas[len(variables.ovals_mas) - 1].x + variables.ovals_mas[len(variables.ovals_mas) - 1].width < variables.start_oval_placement_position[0]:
         variables.ovals_mas[len(variables.ovals_mas) - 1].user_width += variables.units_per_pixel_x
         variables.ovals_mas[len(variables.ovals_mas) - 1].width = int(variables.ovals_mas[len(variables.ovals_mas) - 1].user_width / variables.units_per_pixel_x)
      if variables.ovals_mas[len(variables.ovals_mas) - 1].y + variables.ovals_mas[len(variables.ovals_mas) - 1].height < variables.start_oval_placement_position[1]:
         variables.ovals_mas[len(variables.ovals_mas) - 1].user_height += variables.units_per_pixel_y
         variables.ovals_mas[len(variables.ovals_mas) - 1].height = int(variables.ovals_mas[len(variables.ovals_mas) - 1].user_height / variables.units_per_pixel_y)
      if variables.ovals_mas[len(variables.ovals_mas) - 1].x + variables.ovals_mas[len(variables.ovals_mas) - 1].width > variables.start_oval_placement_position[0]:
         variables.ovals_mas[len(variables.ovals_mas) - 1].user_width -= variables.units_per_pixel_x
         variables.ovals_mas[len(variables.ovals_mas) - 1].width = int(variables.ovals_mas[len(variables.ovals_mas) - 1].user_width / variables.units_per_pixel_x)
      if variables.ovals_mas[len(variables.ovals_mas) - 1].y + variables.ovals_mas[len(variables.ovals_mas) - 1].height > variables.start_oval_placement_position[1]:
         variables.ovals_mas[len(variables.ovals_mas) - 1].user_height -= variables.units_per_pixel_y
         variables.ovals_mas[len(variables.ovals_mas) - 1].height = int(variables.ovals_mas[len(variables.ovals_mas) - 1].user_height / variables.units_per_pixel_y)

   if variables.rectangle_placement_motion_flag:
      new_rectangle_width = abs(x - variables.start_rectangle_placement_position[0])
      new_rectangle_height = abs(y - variables.start_rectangle_placement_position[1])
      if x < variables.start_rectangle_placement_position[0]:
            variables.rectangles_mas[len(variables.rectangles_mas) - 1].user_x = x * variables.units_per_pixel_x
      elif x > variables.start_rectangle_placement_position[0]:
         variables.rectangles_mas[len(variables.rectangles_mas) - 1].user_x = variables.start_rectangle_placement_position[0] * variables.units_per_pixel_x
      variables.rectangles_mas[len(variables.rectangles_mas) - 1].x = int(variables.rectangles_mas[len(variables.rectangles_mas) - 1].user_x / variables.units_per_pixel_x)
      if y < variables.start_rectangle_placement_position[1]:
            variables.rectangles_mas[len(variables.rectangles_mas) - 1].user_y = canvas_height * variables.units_per_pixel_y - y * variables.units_per_pixel_y
      elif y > variables.start_rectangle_placement_position[1]:
         variables.rectangles_mas[len(variables.rectangles_mas) - 1].user_y = canvas_height * variables.units_per_pixel_y - variables.start_rectangle_placement_position[1] * variables.units_per_pixel_y
      variables.rectangles_mas[len(variables.rectangles_mas) - 1].y = int((canvas_height * variables.units_per_pixel_y - variables.rectangles_mas[len(variables.rectangles_mas) - 1].user_y) / variables.units_per_pixel_y)

      variables.rectangles_mas[len(variables.rectangles_mas) - 1].user_width = new_rectangle_width * variables.units_per_pixel_x
      variables.rectangles_mas[len(variables.rectangles_mas) - 1].user_height = new_rectangle_height * variables.units_per_pixel_y
      variables.rectangles_mas[len(variables.rectangles_mas) - 1].width = int(variables.rectangles_mas[len(variables.rectangles_mas) - 1].user_width / variables.units_per_pixel_x)
      variables.rectangles_mas[len(variables.rectangles_mas) - 1].height = int(variables.rectangles_mas[len(variables.rectangles_mas) - 1].user_height / variables.units_per_pixel_y)
      if variables.rectangles_mas[len(variables.rectangles_mas) - 1].x + variables.rectangles_mas[len(variables.rectangles_mas) - 1].width < variables.start_rectangle_placement_position[0]:
         variables.rectangles_mas[len(variables.rectangles_mas) - 1].user_width += variables.units_per_pixel_x
         variables.rectangles_mas[len(variables.rectangles_mas) - 1].width = int(variables.rectangles_mas[len(variables.rectangles_mas) - 1].user_width / variables.units_per_pixel_x)
      if variables.rectangles_mas[len(variables.rectangles_mas) - 1].y + variables.rectangles_mas[len(variables.rectangles_mas) - 1].height < variables.start_rectangle_placement_position[1]:
         variables.rectangles_mas[len(variables.rectangles_mas) - 1].user_height += variables.units_per_pixel_y
         variables.rectangles_mas[len(variables.rectangles_mas) - 1].height = int(variables.rectangles_mas[len(variables.rectangles_mas) - 1].user_height / variables.units_per_pixel_y)
      if variables.rectangles_mas[len(variables.rectangles_mas) - 1].x + variables.rectangles_mas[len(variables.rectangles_mas) - 1].width > variables.start_rectangle_placement_position[0]:
         variables.rectangles_mas[len(variables.rectangles_mas) - 1].user_width -= variables.units_per_pixel_x
         variables.rectangles_mas[len(variables.rectangles_mas) - 1].width = int(variables.rectangles_mas[len(variables.rectangles_mas) - 1].user_width / variables.units_per_pixel_x)
      if variables.rectangles_mas[len(variables.rectangles_mas) - 1].y + variables.rectangles_mas[len(variables.rectangles_mas) - 1].height > variables.start_rectangle_placement_position[1]:
         variables.rectangles_mas[len(variables.rectangles_mas) - 1].user_height -= variables.units_per_pixel_y
         variables.rectangles_mas[len(variables.rectangles_mas) - 1].height = int(variables.rectangles_mas[len(variables.rectangles_mas) - 1].user_height / variables.units_per_pixel_y)

   if variables.wall_placement_motion_flag:
      if keyboard.is_pressed('shift') == True and keyboard.is_pressed('alt') == False:
         y = variables.start_wall_placement_position[1]
      elif keyboard.is_pressed('shift') == False and keyboard.is_pressed('alt') == True:
         x = variables.start_wall_placement_position[0]
      if x == 0:
         x = Parameters.wall_width
      elif x == canvas_width:
         x = canvas_width - Parameters.wall_width
      if y == 0:
         y = Parameters.wall_width
      elif y == canvas_height:
         y = canvas_height - Parameters.wall_width
      variables.walls_mas[len(variables.walls_mas) - 1].user_x2 = x * variables.units_per_pixel_x
      variables.walls_mas[len(variables.walls_mas) - 1].user_y2 = canvas_height * variables.units_per_pixel_y - y * variables.units_per_pixel_y
      variables.walls_mas[len(variables.walls_mas) - 1].x2 = int(variables.walls_mas[len(variables.walls_mas) - 1].user_x2 / variables.units_per_pixel_x)
      variables.walls_mas[len(variables.walls_mas) - 1].y2 = int((canvas_height * variables.units_per_pixel_y - variables.walls_mas[len(variables.walls_mas) - 1].user_y2) / variables.units_per_pixel_y)

   if variables.replace_beacon_flag:
      if x == 0: variables.replace_object.user_x = str(0)
      elif x == canvas_width: variables.replace_object.user_x = str(variables.axes_max_x)
      else: variables.replace_object.user_x = str(round((x - variables.delta_beacon_replace_width) * variables.units_per_pixel_x, 2))
      if y == 0: variables.replace_object.user_y = str(variables.axes_max_y)
      elif y == canvas_height: variables.replace_object.user_y = str(0)
      else: variables.replace_object.user_y = str(round(canvas_height * variables.units_per_pixel_y - (y - variables.delta_beacon_replace_height) * variables.units_per_pixel_y, 2))
      variables.replace_object.x = int(float(variables.replace_object.user_x) / variables.units_per_pixel_x)
      variables.replace_object.y = int((canvas_height * variables.units_per_pixel_y - float(variables.replace_object.user_y)) / variables.units_per_pixel_y)
      INFO_BOARD.BeaconsInfo(display_width, display_height, pygame, window, variables.info_beacon,
                             Parameters.display_color, canvas_offset_top, canvas_offset_right, variables)

   if variables.replace_oval_flag:
      if x < variables.delta_oval_replace_width:
         variables.replace_object.user_x = 0
      elif x > canvas_width - (variables.replace_object.width - variables.delta_oval_replace_width):
         variables.replace_object.user_x = (canvas_width - variables.replace_object.width) * variables.units_per_pixel_x
      else:
         variables.replace_object.user_x = (x - variables.delta_oval_replace_width) * variables.units_per_pixel_x
      if y < variables.delta_oval_replace_height:
         variables.replace_object.user_y = variables.axes_max_y
      elif y > canvas_height - (variables.replace_object.height - variables.delta_oval_replace_height):
         variables.replace_object.user_y = canvas_height * variables.units_per_pixel_y - (canvas_height - variables.replace_object.height) * variables.units_per_pixel_y
      else:
         variables.replace_object.user_y = canvas_height * variables.units_per_pixel_y - (y - variables.delta_oval_replace_height) * variables.units_per_pixel_y
      variables.replace_object.x = int(variables.replace_object.user_x / variables.units_per_pixel_x)
      variables.replace_object.y = int((canvas_height * variables.units_per_pixel_y - variables.replace_object.user_y) / variables.units_per_pixel_y)

   if variables.replace_rectangle_flag:
      if x < variables.delta_rectangle_replace_width:
         variables.replace_object.user_x = 0
      elif x > canvas_width - (variables.replace_object.width - variables.delta_rectangle_replace_width):
         variables.replace_object.user_x = (canvas_width - variables.replace_object.width) * variables.units_per_pixel_x
      else:
         variables.replace_object.user_x = (x - variables.delta_rectangle_replace_width) * variables.units_per_pixel_x
      if y < variables.delta_rectangle_replace_height:
         variables.replace_object.user_y = variables.axes_max_y
      elif y > canvas_height - (variables.replace_object.height - variables.delta_rectangle_replace_height):
         variables.replace_object.user_y = canvas_height * variables.units_per_pixel_y - (canvas_height - variables.replace_object.height) * variables.units_per_pixel_y
      else:
         variables.replace_object.user_y = canvas_height * variables.units_per_pixel_y - (y - variables.delta_rectangle_replace_height) * variables.units_per_pixel_y
      variables.replace_object.x = int(variables.replace_object.user_x / variables.units_per_pixel_x)
      variables.replace_object.y = int((canvas_height * variables.units_per_pixel_y - variables.replace_object.user_y) / variables.units_per_pixel_y)

   if variables.replace_wall_side_1_flag:
      if x == 0:
         x = Parameters.wall_width
      elif x == canvas_width:
         x = canvas_width - Parameters.wall_width
      if y == 0:
         y = Parameters.wall_width
      elif y == canvas_height:
         y = canvas_height - Parameters.wall_width
      variables.replace_object.user_x1 = x * variables.units_per_pixel_x
      variables.replace_object.user_y1 = canvas_height * variables.units_per_pixel_y - y * variables.units_per_pixel_y
      variables.replace_object.x1 = int(variables.replace_object.user_x1 / variables.units_per_pixel_x)
      variables.replace_object.y1 = int((canvas_height * variables.units_per_pixel_y - variables.replace_object.user_y1) / variables.units_per_pixel_y)

   if variables.replace_wall_side_2_flag:
      if x == 0:
         x = Parameters.wall_width
      elif x == canvas_width:
         x = canvas_width - Parameters.wall_width
      if y == 0:
         y = Parameters.wall_width
      elif y == canvas_height:
         y = canvas_height - Parameters.wall_width
      variables.replace_object.user_x2 = x * variables.units_per_pixel_x
      variables.replace_object.user_y2 = canvas_height * variables.units_per_pixel_y - y * variables.units_per_pixel_y
      variables.replace_object.x2 = int(variables.replace_object.user_x2 / variables.units_per_pixel_x)
      variables.replace_object.y2 = int((canvas_height * variables.units_per_pixel_y - variables.replace_object.user_y2) / variables.units_per_pixel_y)

   if variables.ruler_enabled_flag:
      if x >= canvas_width: x = canvas_width - 2
      if y >= canvas_height: y = canvas_height - 2
      variables.ruler_finish_pos = (x, y)

def MouseButtonUpLeft(variables):
   if variables.oval_placement_motion_flag: variables.oval_placement_motion_flag = False
   elif variables.rectangle_placement_motion_flag: variables.rectangle_placement_motion_flag = False
   elif variables.wall_placement_motion_flag: variables.wall_placement_motion_flag = False
   elif variables.replace_beacon_flag: variables.replace_beacon_flag = False
   elif variables.replace_oval_flag: variables.replace_oval_flag = False
   elif variables.replace_rectangle_flag: variables.replace_rectangle_flag = False
   elif variables.replace_wall_side_1_flag: variables.replace_wall_side_1_flag = False
   elif variables.replace_wall_side_2_flag: variables.replace_wall_side_2_flag = False
   elif variables.ruler_enabled_flag: variables.ruler_enabled_flag = False

def MouseButtonDownRight(x, y, variables, pygame, window, display_color, display_width, canvas_offset_right, canvas_offset_top):
   delete_beacon_flag = False
   delete_oval_flag = False
   delete_rectangle_flag = False
   delete_wall_flag = False

   for beacon in variables.beacons_mas:
      if pow(x - beacon.x, 2) / pow(beacon.radius, 2) + \
              pow(y - beacon.y, 2) / pow(beacon.radius, 2) <= 1:
         variables.beacons_mas.remove(beacon)
         """Delete info board if beacon has been delete / Удаление иформационного табло иесли маяк был удален"""
         if beacon == variables.info_beacon:
            pygame.draw.rect(window, display_color,
                             (display_width - (canvas_offset_right - 30), canvas_offset_top - 10, canvas_offset_right, 400))
            variables.info_board_active_flag = False
         delete_beacon_flag = True

   if not delete_beacon_flag:

      for wall in variables.walls_mas:
         if (wall.x1 - wall.width <= x <= wall.x1 + wall.width and wall.y1 - wall.width <= y <= wall.y1 + wall.width) or \
                 (wall.x2 - wall.width <= x <= wall.x2 + wall.width and wall.y2 - wall.width <= y <= wall.y2 + wall.width):
            variables.walls_mas.remove(wall)
            delete_wall_flag = True

      if not delete_wall_flag:

         for oval in variables.ovals_mas:
            if pow(x - (oval.x + oval.width / 2), 2) / pow(oval.width / 2, 2) + \
                    pow(y - (oval.y + oval.height / 2), 2) / pow(oval.height / 2, 2) <= 1:
               if delete_oval_flag:
                  if variables.delete_object.width > oval.width and variables.delete_object.height > oval.height:
                     variables.delete_object = oval
               else:
                  variables.delete_object = oval
                  delete_oval_flag = True

         for rectangle in variables.rectangles_mas:
            if rectangle.x <= x <= rectangle.x + rectangle.width and rectangle.y <= y <= rectangle.y + rectangle.height:
               if delete_oval_flag:
                  if variables.delete_object.width > rectangle.width and variables.delete_object.height > rectangle.height:
                     variables.delete_object = rectangle
                     delete_oval_flag = False
                     delete_rectangle_flag = True
               elif delete_rectangle_flag:
                  if variables.delete_object.width > rectangle.width and variables.delete_object.height > rectangle.height:
                     variables.delete_object = rectangle
               else:
                  variables.delete_object = rectangle
                  delete_rectangle_flag = True

         if variables.delete_object is not None:
            if delete_oval_flag:
               variables.ovals_mas.remove(variables.delete_object)
            if delete_rectangle_flag:
               variables.rectangles_mas.remove(variables.delete_object)

   if delete_beacon_flag or delete_oval_flag or delete_rectangle_flag or delete_wall_flag:
      variables.GDOP_enabled_flag = False
      variables.coverage_enabled_flag = False
      variables.button_coverage.NoPress(pygame, window)
      variables.button_GDOP.NoPress(pygame, window)

def MouseWheel(x, y, delta, canvas_height, variables, pygame, window):
   for oval in variables.ovals_mas:
         if pow(x - (oval.x + oval.width / 2), 2) / pow(oval.width / 2, 2) + \
                 pow(y - (oval.y + oval.height / 2), 2) / pow(oval.height / 2, 2) <= 1:

            if keyboard.is_pressed('shift') == True and keyboard.is_pressed('alt') == False:
               if delta == 1:
                  if oval.user_x > 0 and oval.user_x + oval.user_width < variables.axes_max_x:
                     oval.user_x = oval.user_x - variables.units_per_pixel_x
                     oval.user_width = oval.user_width + variables.units_per_pixel_x * 2
                  elif oval.user_x <= 0 and oval.user_x + oval.user_width < variables.axes_max_x:
                     oval.user_width = oval.user_width + variables.units_per_pixel_x * 2
                  elif oval.user_x + oval.user_width >= variables.axes_max_x and oval.user_x > 0:
                     oval.user_x = oval.user_x - variables.units_per_pixel_x * 2
                     oval.user_width = oval.user_width + variables.units_per_pixel_x * 2
               if delta == -1:
                  if oval.width > Parameters.oval_minimum_width:
                     oval.user_x = oval.user_x + variables.units_per_pixel_x
                     oval.user_width = oval.user_width - variables.units_per_pixel_x * 2

            elif keyboard.is_pressed('alt') == True and keyboard.is_pressed('shift') == False:
               if delta == 1:
                  if oval.user_y - oval.user_height > 0 and oval.user_y < variables.axes_max_y:
                     oval.user_y = oval.user_y + variables.units_per_pixel_y
                     oval.user_height = oval.user_height + variables.units_per_pixel_y * 2
                  elif oval.user_y - oval.user_height > 0 and oval.user_y <= variables.axes_max_y:
                     oval.user_height = oval.user_height + variables.units_per_pixel_y * 2
                  elif oval.user_y < variables.axes_max_y and oval.user_y - oval.user_height <= 0:
                     oval.user_y = oval.user_y + variables.units_per_pixel_y * 2
                     oval.user_height = oval.user_height + variables.units_per_pixel_y * 2
               if delta == -1:
                  if oval.height > Parameters.oval_minimum_height:
                     oval.user_y = oval.user_y + variables.units_per_pixel_y
                     oval.user_height = oval.user_height - variables.units_per_pixel_y * 2

            elif keyboard.is_pressed('alt') == False and keyboard.is_pressed('shift') == False or \
                    keyboard.is_pressed('alt') == True and keyboard.is_pressed('shift') == True:
               if delta == 1:
                  if oval.user_x > 0 and oval.user_x + oval.user_width < variables.axes_max_x and \
                          oval.user_y < variables.axes_max_y and oval.user_y - oval.user_height > 0:
                     oval.user_x = oval.user_x - variables.units_per_pixel_x
                     oval.user_y = oval.user_y + variables.units_per_pixel_y
                     oval.user_width = oval.user_width + variables.units_per_pixel_x * 2
                     oval.user_height = oval.user_height + variables.units_per_pixel_y * 2
                  else:
                     if oval.user_x <= 0 and oval.user_y >= variables.axes_max_y and \
                             oval.user_x + oval.user_width <= variables.axes_max_x and oval.user_y - oval.user_height >= 0:
                        oval.user_width = oval.user_width + variables.units_per_pixel_x * 2
                        oval.user_height = oval.user_height + variables.units_per_pixel_y * 2
                     elif oval.user_x <= 0 and oval.user_y - oval.user_height <= 0 and \
                             oval.user_x + oval.user_width <= variables.axes_max_x and oval.user_y <= variables.axes_max_y:
                        oval.user_y = oval.user_y + variables.units_per_pixel_y * 2
                        oval.user_width = oval.user_width + variables.units_per_pixel_x * 2
                        oval.user_height = oval.user_height + variables.units_per_pixel_y * 2
                     elif oval.user_x + oval.user_width >= variables.axes_max_x and oval.user_y >= variables.axes_max_y and \
                             oval.user_x >= 0 and oval.user_y - oval.user_height >= 0:
                        oval.user_x = oval.user_x - variables.units_per_pixel_x * 2
                        oval.user_width = oval.user_width + variables.units_per_pixel_x * 2
                        oval.user_height = oval.user_height + variables.units_per_pixel_y * 2
                     elif oval.user_x + oval.user_width >= variables.axes_max_x and oval.user_y - oval.user_height >= 0 and \
                             oval.user_x >= 0 and oval.y <= variables.axes_max_y:
                        oval.user_x = oval.user_x - variables.units_per_pixel_x * 2
                        oval.user_y = oval.user_y + variables.units_per_pixel_y * 2
                        oval.user_width = oval.user_width + variables.units_per_pixel_x * 2
                        oval.user_height = oval.user_height + variables.units_per_pixel_y * 2
                     elif oval.user_x <= 0 and oval.user_y <= variables.axes_max_y and \
                             oval.user_x + oval.user_width <= variables.axes_max_x and oval.user_y - oval.user_height >= 0:
                        oval.user_y = oval.user_y + variables.units_per_pixel_y
                        oval.user_width = oval.user_width + variables.units_per_pixel_x * 2
                        oval.user_height = oval.user_height + variables.units_per_pixel_y * 2
                     elif oval.user_x + oval.user_width >= variables.axes_max_x and oval.user_x >= 0 and \
                             oval.user_y <= variables.axes_max_y and oval.user_y - oval.user_height >= 0:
                        oval.user_x = oval.user_x - variables.units_per_pixel_x * 2
                        oval.user_y = oval.user_y + variables.units_per_pixel_y
                        oval.user_width = oval.user_width + variables.units_per_pixel_x * 2
                        oval.user_height = oval.user_height + variables.units_per_pixel_y * 2
                     elif oval.user_y >= variables.axes_max_y and oval.user_x >= 0 and \
                             oval.user_x + oval.user_width <= variables.axes_max_x and oval.user_y - oval.user_height >= 0:
                        oval.user_x = oval.user_x - variables.units_per_pixel_x
                        oval.user_width = oval.user_width + variables.units_per_pixel_x * 2
                        oval.user_height = oval.user_height + variables.units_per_pixel_y * 2
                     elif oval.user_y - oval.user_height <= 0 and oval.user_y >= 0 and \
                             oval.user_x >= 0 and oval.user_x + oval.user_width <= variables.axes_max_x:
                        oval.user_x = oval.user_x - variables.units_per_pixel_x
                        oval.user_y = oval.user_y + variables.units_per_pixel_y * 2
                        oval.user_width = oval.user_width + variables.units_per_pixel_x * 2
                        oval.user_height = oval.user_height + variables.units_per_pixel_y * 2
               if delta == -1:
                  if oval.width > Parameters.oval_minimum_width:
                     oval.user_x = oval.user_x + variables.units_per_pixel_x
                     oval.user_width = oval.user_width - variables.units_per_pixel_x * 2
                  if oval.height > Parameters.oval_minimum_height:
                     oval.user_y = oval.user_y - variables.units_per_pixel_y
                     oval.user_height = oval.user_height - variables.units_per_pixel_y * 2

         variables.GDOP_enabled_flag = False
         variables.coverage_enabled_flag = False
         variables.button_coverage.NoPress(pygame, window)
         variables.button_GDOP.NoPress(pygame, window)

   for rectangle in variables.rectangles_mas:
         if rectangle.x <= x <= rectangle.x + rectangle.width and rectangle.y <= y <= rectangle.y + rectangle.height:

            if keyboard.is_pressed('shift') == True and keyboard.is_pressed('alt') == False:
               if delta == 1:
                  if rectangle.user_x > 0 and rectangle.user_x + rectangle.user_width < variables.axes_max_x:
                     rectangle.user_x = rectangle.user_x - variables.units_per_pixel_x
                     rectangle.user_width = rectangle.user_width + variables.units_per_pixel_x * 2
                  elif rectangle.user_x <= 0 and rectangle.user_x + rectangle.user_width < variables.axes_max_x:
                     rectangle.user_width = rectangle.user_width + variables.units_per_pixel_x * 2
                  elif rectangle.user_x + rectangle.user_width >= variables.axes_max_x and rectangle.user_x > 0:
                     rectangle.user_x = rectangle.user_x - variables.units_per_pixel_x * 2
                     rectangle.user_width = rectangle.user_width + variables.units_per_pixel_x * 2
               if delta == -1:
                  if rectangle.width > Parameters.oval_minimum_width:
                     rectangle.user_x = rectangle.user_x + variables.units_per_pixel_x
                     rectangle.user_width = rectangle.user_width - variables.units_per_pixel_x * 2

            elif keyboard.is_pressed('alt') == True and keyboard.is_pressed('shift') == False:
               if delta == 1:
                  if rectangle.user_y - rectangle.user_height > 0 and rectangle.user_y < variables.axes_max_y:
                     rectangle.user_y = rectangle.user_y + variables.units_per_pixel_y
                     rectangle.user_height = rectangle.user_height + variables.units_per_pixel_y * 2
                  elif rectangle.user_y - rectangle.user_height > 0 and rectangle.user_y <= variables.axes_max_y:
                     rectangle.user_height = rectangle.user_height + variables.units_per_pixel_y * 2
                  elif rectangle.user_y < variables.axes_max_y and rectangle.user_y - rectangle.user_height <= 0:
                     rectangle.user_y = rectangle.user_y + variables.units_per_pixel_y * 2
                     rectangle.user_height = rectangle.user_height + variables.units_per_pixel_y * 2
               if delta == -1:
                  if rectangle.height > Parameters.oval_minimum_height:
                     rectangle.user_y = rectangle.user_y + variables.units_per_pixel_y
                     rectangle.user_height = rectangle.user_height - variables.units_per_pixel_y * 2

            elif keyboard.is_pressed('alt') == False and keyboard.is_pressed('shift') == False or \
                    keyboard.is_pressed('alt') == True and keyboard.is_pressed('shift') == True:
               if delta == 1:
                  if rectangle.user_x > 0 and rectangle.user_x + rectangle.user_width < variables.axes_max_x and \
                          rectangle.user_y < variables.axes_max_y and rectangle.user_y - rectangle.user_height > 0:
                     rectangle.user_x = rectangle.user_x - variables.units_per_pixel_x
                     rectangle.user_y = rectangle.user_y + variables.units_per_pixel_y
                     rectangle.user_width = rectangle.user_width + variables.units_per_pixel_x * 2
                     rectangle.user_height = rectangle.user_height + variables.units_per_pixel_y * 2
                  else:
                     if rectangle.user_x <= 0 and rectangle.user_y >= variables.axes_max_y and \
                             rectangle.user_x + rectangle.user_width <= variables.axes_max_x and rectangle.user_y - rectangle.user_height >= 0:
                        rectangle.user_width = rectangle.user_width + variables.units_per_pixel_x * 2
                        rectangle.user_height = rectangle.user_height + variables.units_per_pixel_y * 2
                     elif rectangle.user_x <= 0 and rectangle.user_y - rectangle.user_height <= 0 and \
                             rectangle.user_x + rectangle.user_width <= variables.axes_max_x and rectangle.user_y <= variables.axes_max_y:
                        rectangle.user_y = rectangle.user_y + variables.units_per_pixel_y * 2
                        rectangle.user_width = rectangle.user_width + variables.units_per_pixel_x * 2
                        rectangle.user_height = rectangle.user_height + variables.units_per_pixel_y * 2
                     elif rectangle.user_x + rectangle.user_width >= variables.axes_max_x and rectangle.user_y >= variables.axes_max_y and \
                             rectangle.user_x >= 0 and rectangle.user_y - rectangle.user_height >= 0:
                        rectangle.user_x = rectangle.user_x - variables.units_per_pixel_x * 2
                        rectangle.user_width = rectangle.user_width + variables.units_per_pixel_x * 2
                        rectangle.user_height = rectangle.user_height + variables.units_per_pixel_y * 2
                     elif rectangle.user_x + rectangle.user_width >= variables.axes_max_x and rectangle.user_y - rectangle.user_height >= 0 and \
                             rectangle.user_x >= 0 and rectangle.y <= variables.axes_max_y:
                        rectangle.user_x = rectangle.user_x - variables.units_per_pixel_x * 2
                        rectangle.user_y = rectangle.user_y + variables.units_per_pixel_y * 2
                        rectangle.user_width = rectangle.user_width + variables.units_per_pixel_x * 2
                        rectangle.user_height = rectangle.user_height + variables.units_per_pixel_y * 2
                     elif rectangle.user_x <= 0 and rectangle.user_y <= variables.axes_max_y and \
                             rectangle.user_x + rectangle.user_width <= variables.axes_max_x and rectangle.user_y - rectangle.user_height >= 0:
                        rectangle.user_y = rectangle.user_y + variables.units_per_pixel_y
                        rectangle.user_width = rectangle.user_width + variables.units_per_pixel_x * 2
                        rectangle.user_height = rectangle.user_height + variables.units_per_pixel_y * 2
                     elif rectangle.user_x + rectangle.user_width >= variables.axes_max_x and rectangle.user_x >= 0 and \
                             rectangle.user_y <= variables.axes_max_y and rectangle.user_y - rectangle.user_height >= 0:
                        rectangle.user_x = rectangle.user_x - variables.units_per_pixel_x * 2
                        rectangle.user_y = rectangle.user_y + variables.units_per_pixel_y
                        rectangle.user_width = rectangle.user_width + variables.units_per_pixel_x * 2
                        rectangle.user_height = rectangle.user_height + variables.units_per_pixel_y * 2
                     elif rectangle.user_y >= variables.axes_max_y and rectangle.user_x >= 0 and \
                             rectangle.user_x + rectangle.user_width <= variables.axes_max_x and rectangle.user_y - rectangle.user_height >= 0:
                        rectangle.user_x = rectangle.user_x - variables.units_per_pixel_x
                        rectangle.user_width = rectangle.user_width + variables.units_per_pixel_x * 2
                        rectangle.user_height = rectangle.user_height + variables.units_per_pixel_y * 2
                     elif rectangle.user_y - rectangle.user_height <= 0 and rectangle.user_y >= 0 and \
                             rectangle.user_x >= 0 and rectangle.user_x + rectangle.user_width <= variables.axes_max_x:
                        rectangle.user_x = rectangle.user_x - variables.units_per_pixel_x
                        rectangle.user_y = rectangle.user_y + variables.units_per_pixel_y * 2
                        rectangle.user_width = rectangle.user_width + variables.units_per_pixel_x * 2
                        rectangle.user_height = rectangle.user_height + variables.units_per_pixel_y * 2
               if delta == -1:
                  if rectangle.width > Parameters.oval_minimum_width:
                     rectangle.user_x = rectangle.user_x + variables.units_per_pixel_x
                     rectangle.user_width = rectangle.user_width - variables.units_per_pixel_x * 2
                  if rectangle.height > Parameters.oval_minimum_height:
                     rectangle.user_y = rectangle.user_y - variables.units_per_pixel_y
                     rectangle.user_height = rectangle.user_height - variables.units_per_pixel_y * 2

         variables.GDOP_enabled_flag = False
         variables.coverage_enabled_flag = False
         variables.button_coverage.NoPress(pygame, window)
         variables.button_GDOP.NoPress(pygame, window)

   for oval in variables.ovals_mas:
      if oval.user_width > variables.axes_max_x: oval.user_width = variables.axes_max_x
      if oval.user_height > variables.axes_max_y: oval.user_height = variables.axes_max_y
      if oval.user_x < 0: oval.user_x = 0
      if oval.user_y > variables.axes_max_y: oval.user_y = variables.axes_max_y
      if oval.user_x + oval.user_width > variables.axes_max_x: oval.user_x = variables.axes_max_x - oval.user_width
      if oval.user_y - oval.user_height < 0: oval.user_y = oval.user_height
      oval.x = int(oval.user_x / variables.units_per_pixel_x)
      oval.y = int((canvas_height * variables.units_per_pixel_y - oval.user_y) / variables.units_per_pixel_y)
      oval.width = math.ceil(oval.user_width / variables.units_per_pixel_x)
      oval.height = math.ceil(oval.user_height / variables.units_per_pixel_y)
   for rectangle in variables.rectangles_mas:
      if rectangle.user_width > variables.axes_max_x: rectangle.user_width = variables.axes_max_x
      if rectangle.user_height > variables.axes_max_y: rectangle.user_height = variables.axes_max_y
      if rectangle.user_x < 0: rectangle.user_x = 0
      if rectangle.user_y > variables.axes_max_y: rectangle.user_y = variables.axes_max_y
      if rectangle.user_x + rectangle.user_width > variables.axes_max_x: rectangle.user_x = variables.axes_max_x - rectangle.user_width
      if rectangle.user_y - rectangle.user_height < 0: rectangle.user_y = rectangle.user_height
      rectangle.x = int(rectangle.user_x / variables.units_per_pixel_x)
      rectangle.y = int((canvas_height * variables.units_per_pixel_y - rectangle.user_y) / variables.units_per_pixel_y)
      rectangle.width = math.ceil(rectangle.user_width / variables.units_per_pixel_x)
      rectangle.height = math.ceil(rectangle.user_height / variables.units_per_pixel_y)
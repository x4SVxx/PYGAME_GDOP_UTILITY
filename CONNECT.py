import PARAMETERS as Parameters
from CROSS import CrossDotWithAllElements
import time


def Connect(variables, window, pygame, canvas, canvas_place, beacon_mas, oval_mas, rectangle_mas, wall_mas):
    visible_beacons = []
    no_visible_beacons = []
    for i in range(len(beacon_mas)):
        for j in range(len(beacon_mas)):
            if j > i:
                if CrossDotWithAllElements(beacon_mas[j].x, beacon_mas[j].y, beacon_mas[i], oval_mas, rectangle_mas, wall_mas):
                    no_visible_beacons.append(beacon_mas[j])
                else:
                    visible_beacons.append(beacon_mas[j])
        DrawConnect(i, canvas, canvas_place, window, pygame, variables, beacon_mas, visible_beacons, no_visible_beacons)
        visible_beacons.clear()
        no_visible_beacons.clear()
    variables.connect_enabled_flag = True

def DrawConnect(i, canvas, canvas_place, window, pygame, variables, beacon_mas, visible_beacons, no_visible_beacons):
    for j in range(len(no_visible_beacons)):
        if not variables.connect_enabled_flag:
            pygame.draw.line(canvas, (0, 200, 0),
                             (no_visible_beacons[j].x, no_visible_beacons[j].y), (beacon_mas[i].x, beacon_mas[i].y),
                             Parameters.flash_connect_line_width)
            window.blit(canvas, canvas_place)
            pygame.display.update()
            time.sleep(Parameters.connect_pause)

            pygame.draw.line(canvas, (255, 255, 0),
                             (no_visible_beacons[j].x, no_visible_beacons[j].y), (beacon_mas[i].x, beacon_mas[i].y),
                             Parameters.flash_connect_line_width)
            window.blit(canvas, canvas_place)
            pygame.display.update()
            time.sleep(Parameters.connect_pause)

            pygame.draw.line(canvas, (250, 150, 0),
                             (no_visible_beacons[j].x, no_visible_beacons[j].y), (beacon_mas[i].x, beacon_mas[i].y),
                             Parameters.flash_connect_line_width)
            window.blit(canvas, canvas_place)
            pygame.display.update()
            time.sleep(Parameters.connect_pause)

        pygame.draw.line(canvas, (255, 0, 0),
                         (no_visible_beacons[j].x, no_visible_beacons[j].y), (beacon_mas[i].x, beacon_mas[i].y),
                         Parameters.no_connect_line_width)
        if not variables.connect_enabled_flag:
            window.blit(canvas, canvas_place)
            pygame.display.update()
            time.sleep(Parameters.connect_pause)

    for j in range(len(visible_beacons)):
        pygame.draw.line(canvas, (0, 200, 0),
                         (visible_beacons[j].x, visible_beacons[j].y), (beacon_mas[i].x, beacon_mas[i].y),
                         Parameters.connect_line_width)
        if not variables.connect_enabled_flag:
            window.blit(canvas, canvas_place)
            pygame.display.update()
            time.sleep(Parameters.connect_pause)

import math
from numba import njit, prange

@njit(fastmath=True, cache=True)
def LineCross(line_1_x1, line_1_x2, line_1_y1, line_1_y2, line_2_x1, line_2_x2, line_2_y1, line_2_y2):
        return ((line_2_x2 - line_2_x1) * (line_1_y1 - line_2_y1) - (line_2_y2 - line_2_y1) * (line_1_x1 - line_2_x1)) * \
               ((line_2_x2 - line_2_x1) * (line_1_y2 - line_2_y1) - (line_2_y2 - line_2_y1) * (line_1_x2 - line_2_x1)) <= 0 and \
               ((line_1_x2 - line_1_x1) * (line_2_y1 - line_1_y1) - (line_1_y2 - line_1_y1) * (line_2_x1 - line_1_x1)) * \
               ((line_1_x2 - line_1_x1) * (line_2_y2 - line_1_y1) - (line_1_y2 - line_1_y1) * (line_2_x2 - line_1_x1)) <= 0

@njit(fastmath=True, cache=True)
def OvalCross(line_x1, line_x2, line_y1, line_y2, oval_x1, oval_x2, oval_y1, oval_y2):
    if pow((oval_x2 - oval_x1) / 2, 2) == 0 and pow((oval_y2 - oval_y1) / 2, 2) == 0:
        return False
    else:
        A = pow(line_x2 - line_x1, 2) / pow((oval_x2 - oval_x1) / 2, 2) + \
            pow(line_y2 - line_y1, 2) / pow((oval_y2 - oval_y1) / 2, 2)
        B = (2 * (line_x1 - (oval_x2 + oval_x1) / 2) * (line_x2 - line_x1)) / pow((oval_x2 - oval_x1) / 2, 2) + \
            (2 * (line_y1 - (oval_y2 + oval_y1) / 2) * (line_y2 - line_y1)) / pow((oval_y2 - oval_y1) / 2, 2)
        C = pow(line_x1 - (oval_x2 + oval_x1) / 2, 2) / pow((oval_x2 - oval_x1) / 2, 2) + \
            pow(line_y1 - (oval_y2 + oval_y1) / 2, 2) / pow((oval_y2 - oval_y1) / 2, 2) - 1
        try:
            D = pow(B, 2) - 4 * A * C
            if D > 0:
                k1 = (-B + math.sqrt(D)) / (2 * A)
                k2 = (-B - math.sqrt(D)) / (2 * A)
                return k1 >= 0 and k1 <= 1 or k2 >= 0 and k2 <= 1
            elif D == 0:
                k = -B / (2 * A)
                return  k >= 0 and k <= 1
            else:
                return False
        except:
            return  True

def CrossDotWithAllElements(connect_x, connect_y, beacon, oval_mas, rectangle_mas, wall_mas):
    cross_flag = False
    for k in prange(len(wall_mas)):
        if LineCross(connect_x, beacon.x, connect_y, beacon.y, wall_mas[k].x1, wall_mas[k].x2, wall_mas[k].y1, wall_mas[k].y2):
            cross_flag = True
            break
    if not cross_flag:
        for k in prange(len(rectangle_mas)):
            if LineCross(connect_x, beacon.x, connect_y, beacon.y,
                         rectangle_mas[k].x, rectangle_mas[k].x + rectangle_mas[k].width,
                         rectangle_mas[k].y,rectangle_mas[k].y) or \
               LineCross(connect_x, beacon.x, connect_y, beacon.y,
                         rectangle_mas[k].x + rectangle_mas[k].width, rectangle_mas[k].x + rectangle_mas[k].width,
                         rectangle_mas[k].y, rectangle_mas[k].y + rectangle_mas[k].height) or \
               LineCross(connect_x, beacon.x, connect_y, beacon.y,
                         rectangle_mas[k].x + rectangle_mas[k].width, rectangle_mas[k].x,
                         rectangle_mas[k].y + rectangle_mas[k].height, rectangle_mas[k].y + rectangle_mas[k].height) or \
               LineCross(connect_x, beacon.x, connect_y, beacon.y,
                         rectangle_mas[k].x, rectangle_mas[k].x,
                         rectangle_mas[k].y + rectangle_mas[k].height, rectangle_mas[k].y):
                cross_flag = True
                break
    if not cross_flag:
        for k in prange(len(oval_mas)):
            if OvalCross(connect_x, beacon.x, connect_y, beacon.y,
                         oval_mas[k].x, oval_mas[k].x + oval_mas[k].width, oval_mas[k].y, oval_mas[k].y + oval_mas[k].height):
                cross_flag = True
                break
    return  cross_flag
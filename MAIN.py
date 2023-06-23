import pygame
from tkinter import Tk
import PARAMETERS as Parameters
from VARIABLES import Variables
import BUTTONS_FUNCTIONS as ButtonFunctions
from CONNECT import Connect
from COVERAGE import  DrawCoverage
from GDOP import DrawGDOP
from AXES import Axes, DrawAxes
from RULER import DrawRuler
from EVENTS import  EventsHandler


pygame.init()

WIDTHSCREEN = Tk().winfo_screenwidth()
HEIGHTSCREEN = Tk().winfo_screenheight()
if WIDTHSCREEN > 1920: WIDTHSCREEN = 1920
if HEIGHTSCREEN > 1080: HEIGHTSCREEN = 1080

display_width, display_height = int(WIDTHSCREEN / 4 * 3), int(HEIGHTSCREEN / 5 * 4 + 30)

window = pygame.display.set_mode((display_width, display_height), pygame.NOFRAME)
window.fill(pygame.Color(Parameters.display_color))

canvas_place = (Parameters.canvas_offset_left, Parameters.canvas_offset_top)
canvas_width = display_width - (Parameters.canvas_offset_left + Parameters.canvas_offset_right)
canvas_height = display_height - (Parameters.canvas_offset_top + Parameters.canvas_offset_bottom)
canvas = pygame.Surface((canvas_width, canvas_height))

clock = pygame.time.Clock()
variables = Variables(canvas_width, canvas_height)
ButtonFunctions.ButtonsCreate(pygame, window, variables, display_width, display_height)
ButtonFunctions.ButtonsTextCreate(window, variables)
Axes(pygame, window, variables, display_width, display_height, canvas_width, canvas_height, False, False)

while True:
    for event in pygame.event.get():
        EventsHandler(event, pygame, window, variables, display_width, display_height,
                      canvas, canvas_place, canvas_width, canvas_height)

    """Draw / Отрисовка"""
    if not variables.coverage_enabled_flag and not variables.GDOP_enabled_flag:
        """Delete helpbar / Удаление подсказки"""
        canvas.fill(Parameters.canvas_color)
        pygame.draw.rect(window, Parameters.display_color, (Parameters.canvas_offset_left + canvas_width + 5, Parameters.canvas_offset_top, 20, canvas_height))
    if variables.coverage_enabled_flag:
        DrawCoverage(variables, pygame, canvas, canvas_width, canvas_height)
    if variables.GDOP_enabled_flag:
        DrawGDOP(canvas, canvas_width, canvas_height, pygame, variables)
    [beacon.Draw(canvas, pygame, canvas_width, canvas_height) for beacon in variables.beacons_mas]
    [oval.Draw(canvas, pygame) for oval in variables.ovals_mas]
    [rectangle.Draw(canvas, pygame) for rectangle in variables.rectangles_mas]
    [wall.Draw(canvas, pygame) for wall in variables.walls_mas]
    if variables.connect_enabled_flag:
        Connect(variables, window, pygame, canvas, canvas_place,
                variables.beacons_mas, variables.ovals_mas, variables.rectangles_mas, variables.walls_mas)
    if variables.ruler_enabled_flag:
        DrawRuler(pygame, canvas, canvas_width, canvas_height, variables)
    DrawAxes(pygame, variables, canvas, canvas_width, canvas_height)
    if variables.enabled_plan_flag:
        canvas.blit(variables.plan_image, (0, 0))

    window.blit(canvas, canvas_place)
    pygame.display.update()
    clock.tick(Parameters.FPS)
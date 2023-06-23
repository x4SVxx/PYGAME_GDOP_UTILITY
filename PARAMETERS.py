import pygame
pygame.init()

FPS = 60

display_color = (200, 200, 200)
canvas_color = (230, 230, 230)

canvas_offset_left = 65
canvas_offset_top = 80
canvas_offset_right = 300
canvas_offset_bottom = 100

buttons_width = 40
buttons_height = 40
button_close_width = 25
button_close_height = 25
button_close_right_offset = 5
button_save_and_load_width = 25
button_save_and_load_height = 25
button_save_offset_left = 65
button_save_and_load_offset_bottom = 5
buttons_top_offset = 5
button_beacon_left_offset = 70
button_beacon_and_buttons_barriers_offset = 20
buttons_group_offset = 5
buttons_barriers_and_buttons_options_offset = 30
buttons_options_group_offset = 30
buttons_options_and_buttons_delete_offset = 70
buttons_choice_width = 18
buttons_choice_height = 18

axes_color = (150, 150, 150)
axes_count = 10

beacon_radius = 8
beacon_color = (0, 0, 255)
oval_outline_width = 3
oval_color = (0, 0, 0)
rectangle_outline_width = 3
rectangle_color = (0, 0, 0)
wall_width = 3
wall_color = (0, 0, 0)

oval_minimum_width = 10
oval_minimum_height = 10
rectangle_minimum_width = 10
rectangle_minimum_height = 10

connect_pause = 0.05
connect_line_width = 2
no_connect_line_width = 1
flash_connect_line_width = 1

coverage_colors = [(255, 0, 0), (255, 100, 5), (255, 165, 0), (255, 255, 0), (0, 255, 0)]

buttons_font = pygame.font.SysFont('ebrima', 12)
axes_font  = pygame.font.SysFont('ebrima', 12)
ruler_font = pygame.font.SysFont('ebrima', 12)
information_font = pygame.font.SysFont('ebrima', 14)
board_font = pygame.font.SysFont('ebrima', 12)
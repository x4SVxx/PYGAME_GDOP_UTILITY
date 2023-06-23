class Variables:

    def __init__(self, canvas_width, canvas_height):

        self.coverage_colors_mas = [[(0, 0, 0) for y in range(canvas_height + 1)] for x in range(canvas_width + 1)]
        self.GDOP_colors_mas = [[(0, 0, 0) for y in range(canvas_height + 1)] for x in range(canvas_width + 1)]

        self.beacon_placement_flag = False
        self.oval_placement_flag = False
        self.wall_placement_flag = False
        self.rectangle_placement_flag = False

        """Checking the beacon was installed / Проверка - был ли утсановлен маяк"""
        self.beacon_posed_flag = False

        self.oval_placement_motion_flag = False
        self.rectangle_placement_motion_flag = False
        self.wall_placement_motion_flag = False

        self.beacons_mas = []
        self.ovals_mas = []
        self.rectangles_mas = []
        self.walls_mas = []

        self.beacons_count = 0
        self.ovals_count = 0
        self.rectangles_count = 0
        self.walls_count = 0

        self.start_oval_placement_position = []
        self.motion_oval_placement = []
        self.start_rectangle_placement_position = []
        self.motion_rectangle_placement = []
        self.start_wall_placement_position = []
        self.motion_wall_placement = []

        self.replace_beacon_flag = False
        self.replace_oval_flag = False
        self.replace_rectangle_flag = False
        self.replace_wall_side_1_flag = False
        self.replace_wall_side_2_flag = False
        self.replace_object = None
        self.delete_object = None

        self.delta_beacon_replace_width = 0
        self.delta_beacon_replace_height = 0
        self.delta_oval_replace_width = 0
        self.delta_oval_replace_height = 0
        self.delta_rectangle_replace_width = 0
        self.delta_rectangle_replace_height = 0

        self.connect_enabled_flag = False
        self.coverage_enabled_flag = False
        self.GDOP_enabled_flag = False

        self.input_axes_x_flag = False
        self.input_axes_y_flag = False

        self.displaying_axes_flag = True

        self.axes_max_x = 100
        self.axes_max_y = 100
        """Для ввода максимального значения осей удобно использовать 2 переменных int и str, так как str может быть пустой, а int нет"""
        self.text_axes_max_x = str(self.axes_max_x)
        self.text_axes_max_y = str(self.axes_max_y)
        self.units_per_pixel_x = None
        self.units_per_pixel_y = None

        self.info_board_active_flag = False
        self.info_beacon = None

        self.progressbar_width = 0

        self.input_beacon_ID_flag = False
        self.input_beacon_x_flag = False
        self.input_beacon_y_flag = False
        self.refactor_beacon = None

        self.ruler_button_press_flag = False
        self.ruler_enabled_flag = False
        self.ruler_start_pos = []
        self.ruler_finish_pos = []

        self.choice_ToF_method_flag = True
        self.choice_TDoA_method_flag = False

        self.load_plan_flag = False
        self.plan_image = None
        self.enabled_plan_flag = False

        self.button_close = None
        self.button_beacon = None
        self.button_oval = None
        self.button_rectangle = None
        self.button_wall = None
        self.button_axes = None
        self.button_ruler = None
        self.button_connect = None
        self.button_coverage = None
        self.button_GDOP = None
        self.button_delete_beacon = None
        self.button_delete_oval = None
        self.button_delete_rectangle = None
        self.button_delete_wall = None
        self.button_delete_all = None
        self.button_save = None
        self.button_load = None
        self.button_choice_ToF_method = None
        self.button_choice_TDoA_metho = None
        self.button_save_image = None
        self.button_load_plan = None
        self.button_enabled_disabled_plan = None
        self.button_delete_plan = None

        self.beacon_text_place = None
        self.barriers_text_place = None
        self.axes_text_place = None
        self.ruler_text_place = None
        self.connect_text_place = None
        self.coverage_text_place = None
        self.GDOP_text_place = None
        self.ToF_text_place = None
        self.TDoA_text_place = None
        self.delete_text_place = None
        self.save_text_place = None
        self.load_text_place = None
        self.save_image_text_place = None
        self.load_plan_text_place = None
        self.enabled_plan_text_place = None
        self.disabled_plan_text_place = None
        self.delete_plan_text_place = None
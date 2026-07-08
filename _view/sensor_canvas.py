from tkinter import Canvas, W, N, S


class SensorCanvas(Canvas):
    """
    Sensor canvas
    :var int INDICATOR_SQUARE: indicator square size
    :var int INDICATOR_LINE_LENGTH: active line length
    :var int INDICATOR_TEXT_LENGTH: sensor name text length
    """
    SENSOR_SQUARE = 20
    SENSOR_LINE_LENGTH = 10
    SENSOR_TEXT_LENGTH = 80
    SENSOR_FONT_SIZE = 10

    def create_sensor(self, x_position, y_position, name, color, line_length=0) -> None:
        """
        Create discrete sensor
        :param int x_position: sensor x position
        :param int y_position: sensor y position
        :param str name: sensor name
        :param str  color: sensor color name string
        :param int line_length: sensor line length (0 - no line)
        """
        self.create_line(x_position,
                         y_position,
                         x_position + line_length,
                         y_position,
                         fill=color)
        self.create_rectangle(x_position + line_length + 2,
                              y_position - self.SENSOR_SQUARE // 2,
                              x_position + line_length + self.SENSOR_SQUARE + 2,
                              y_position + self.SENSOR_SQUARE // 2,
                              fill=color)
        self.create_text(x_position + line_length + self.SENSOR_SQUARE + 4,
                         y_position,
                         font=("Arial", self.SENSOR_FONT_SIZE),
                         anchor=W, text=name)


class AnalogCanvas(Canvas):
    """
    Analog sensor canvas
    :var int ANALOG_INDICATOR_WIDTH: analog indicator bar size
    """
    ANALOG_SENSOR_WIDTH = 20
    ANALOG_SENSOR_FONT_SIZE = 10

    def create_analog(self, x_position, y_position, height, name, active_color, active_level=0, activ_level_print=False,
                      background_color='gray', line_length=0, name_position='right', marks_position=None) -> int:
        """
        Create analog sensor
        :param int x_position: analog indicator x position
        :param int y_position: analog indicator y position
        :param int height: indicator bar height
        :param str name: indicator name
        :param str active_color: active color name string
        :param int active_level: activ level [%]
        :param bool activ_level_print: activ level printing after sensor name
        :param str background_color: indicator bar background color name string
        :param int line_length: indicator line length (0 - no line)
        :param str name_position: name position (left or right)
        :param tuple marks_position: indicator bar marks position [%]
        :return: name text canvas id (to delete)
        """

        text_id = None

        if active_level > 100:
            active_level = 100
        if active_level < 0:
            active_level = 0

        if activ_level_print:
            name = '%s (%s%%)' % (name, active_level)

        self.create_line(x_position,
                         y_position,
                         x_position + line_length,
                         y_position,
                         fill=background_color)
        self.create_rectangle(x_position + line_length,
                              y_position,
                              x_position + line_length + self.ANALOG_SENSOR_WIDTH,
                              y_position + height,
                              fill=background_color)
        self.create_rectangle(x_position + line_length,
                              y_position + height - int(height / 100 * active_level),
                              x_position + line_length + self.ANALOG_SENSOR_WIDTH,
                              y_position + height,
                              fill=active_color)
        self.create_line(x_position,
                         y_position + height,
                         x_position + line_length,
                         y_position + height,
                         fill=background_color)
        if marks_position is not None:
            for item in marks_position:
                self.create_line(x_position + line_length,
                                 y_position + height - int(height / 100 * item),
                                 x_position + line_length + self.ANALOG_SENSOR_WIDTH,
                                 y_position + height - int(height / 100 * item),
                                 dash=(1, 1))
        if name_position == 'right':
            # noinspection PyArgumentList
            text_id = self.create_text(x_position + line_length + self.ANALOG_SENSOR_WIDTH,
                                       y_position + height // 2,
                                       font=("Arial", self.ANALOG_SENSOR_FONT_SIZE),
                                       angle=90, anchor=N, text=name)
        elif name_position == 'left':
            # noinspection PyArgumentList
            text_id = self.create_text(x_position,
                                       y_position + height // 2,
                                       font=("Arial", self.ANALOG_SENSOR_FONT_SIZE),
                                       angle=90, anchor=S, text=name)

        return text_id

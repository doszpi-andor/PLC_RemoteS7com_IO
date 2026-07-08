from tkinter import Frame, IntVar, Checkbutton, Tk

from _view.conveyor_canvas import ConveyorCanvas
from _view.indicator_canvas import IndicatorCanvas
from _view.sensor_canvas import SensorCanvas
from _view.silo_camvas import SiloCanvas


class ErrorCheckBox(Frame):

    # noinspection PyDefaultArgument
    def __init__(self,
                 master=None,
                 silo_process=None,
                 error1_process=None,
                 error2_process=None,
                 error3_process=None,
                 cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        self.silo_var = IntVar()
        # noinspection SpellCheckingInspection
        self.silo = Checkbutton(self, variable=self.silo_var, command=silo_process, text='Siló kifogyott')

        self.error1_var = IntVar()
        # noinspection SpellCheckingInspection
        self.error1 = Checkbutton(self, variable=self.error1_var, command=error1_process, text='Szalag 1 hiba')
        self.error2_var = IntVar()
        # noinspection SpellCheckingInspection
        self.error2 = Checkbutton(self, variable=self.error2_var, command=error2_process, text='Szalag 2 hiba')
        self.error3_var = IntVar()
        # noinspection SpellCheckingInspection
        self.error3 = Checkbutton(self, variable=self.error3_var, command=error3_process, text='Szalag 3 hiba')

        self.silo.grid(row=1, column=1, columnspan=3)

        self.error1.grid(row=2, column=1)
        self.error2.grid(row=2, column=2)
        self.error3.grid(row=2, column=3)


class Conveyors(SiloCanvas, ConveyorCanvas, SensorCanvas, IndicatorCanvas):
    SILO_WIDTH = 100
    SILO_HEIGHT = 150

    INDICATOR_WIDTH = 25

    CONVEYOR_WIDTH = 45

    CONVEYOR1_LENGTH = 300
    CONVEYOR2_LENGTH = 300
    CONVEYOR3_LENGTH = 300

    CONVEYOR2_X_POSITION = 5
    CONVEYOR1_X_POSITION = CONVEYOR2_X_POSITION + CONVEYOR2_LENGTH * 2 // 3
    CONVEYOR3_X_POSITION = CONVEYOR1_X_POSITION + CONVEYOR1_LENGTH * 2 // 3

    DIRECTION1_INDICATOR_X_POSITION = CONVEYOR1_X_POSITION - 60
    DIRECTION2_INDICATOR_X_POSITION = CONVEYOR1_X_POSITION + CONVEYOR1_LENGTH - 30

    SILO_X_POSITION = CONVEYOR1_X_POSITION + CONVEYOR1_LENGTH // 2 - SILO_WIDTH // 2
    SILO_SENSOR_X_POSITION = SILO_X_POSITION + 5

    SILO_Y_POSITION = 5
    SILO_SENSOR_Y_POSITION = SILO_Y_POSITION + SILO_HEIGHT * 7 // 8

    CONVEYOR1_Y_POSITION = SILO_Y_POSITION + SILO_HEIGHT + 40
    CONVEYOR2_Y_POSITION = CONVEYOR1_Y_POSITION + CONVEYOR_WIDTH + 20
    CONVEYOR3_Y_POSITION = CONVEYOR2_Y_POSITION

    DIRECTION1_INDICATOR_Y_POSITION = CONVEYOR1_Y_POSITION - INDICATOR_WIDTH - 10
    DIRECTION2_INDICATOR_Y_POSITION = DIRECTION1_INDICATOR_Y_POSITION

    FULL_WIDTH = CONVEYOR3_X_POSITION + CONVEYOR3_LENGTH
    FULL_HEIGHT = CONVEYOR3_Y_POSITION + CONVEYOR_WIDTH

    # noinspection PyDefaultArgument
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, width=self.FULL_WIDTH, height=self.FULL_HEIGHT, **kw)

        self.__silo_motor_color = 'gray'
        self.__silo_sensor_color = 'blue'

        self.__conveyor1_motor_color = 'gray'
        self.__conveyor1_left_color = 'gray'
        self.__conveyor1_right_color = 'gray'
        self.__conveyor1_sensor_color = 'gray'
        self.__conveyor2_motor_color = 'gray'
        self.__conveyor2_sensor_color = 'gray'
        self.__conveyor3_motor_color = 'gray'
        self.__conveyor3_sensor_color = 'gray'

        self.__silo_drawing()
        self.__conveyor1_drawing()
        self.__conveyor2_drawing()
        self.__conveyor3_drawing()
        self.__direction_left_drawing()
        self.__direction_right_drawing()

    def silo_change_motor_color(self, motor_color):
        if self.__silo_motor_color != motor_color:
            self.__silo_motor_color = motor_color
            self.__silo_drawing()

    def silo_change_sensor_color(self, sensor_color):
        if self.__silo_sensor_color != sensor_color:
            self.__silo_sensor_color = sensor_color
            self.__silo_drawing()

    def conveyor1_change_motor_color(self, motor_color, left_color, right_color):
        if self.__conveyor1_motor_color != motor_color:
            self.__conveyor1_motor_color = motor_color
            self.__conveyor1_drawing()
        if self.__conveyor1_left_color != left_color:
            self.__conveyor1_left_color = left_color
            self.__direction_left_drawing()
        if self.__conveyor1_right_color != right_color:
            self.__conveyor1_right_color = right_color
            self.__direction_right_drawing()

    def conveyor1_change_sensor_color(self, sensor_color):
        if self.__conveyor1_sensor_color != sensor_color:
            self.__conveyor1_sensor_color = sensor_color
            self.__conveyor1_drawing()

    def conveyor2_change_motor_color(self, motor_color):
        if self.__conveyor2_motor_color != motor_color:
            self.__conveyor2_motor_color = motor_color
            self.__conveyor2_drawing()

    def conveyor2_change_sensor_color(self, sensor_color):
        if self.__conveyor2_sensor_color != sensor_color:
            self.__conveyor2_sensor_color = sensor_color
            self.__conveyor2_drawing()

    def conveyor3_change_motor_color(self, motor_color):
        if self.__conveyor3_motor_color != motor_color:
            self.__conveyor3_motor_color = motor_color
            self.__conveyor3_drawing()

    def conveyor3_change_sensor_color(self, sensor_color):
        if self.__conveyor3_sensor_color != sensor_color:
            self.__conveyor3_sensor_color = sensor_color
            self.__conveyor3_drawing()

    def __silo_drawing(self):
        # noinspection SpellCheckingInspection
        self.create_silo(self.SILO_X_POSITION,
                         self.SILO_Y_POSITION,
                         silo_name='Siló',
                         motor_name='M1', motor_color=self.__silo_motor_color)
        self.create_sensor(self.SILO_SENSOR_X_POSITION,
                           self.SILO_SENSOR_Y_POSITION,
                           line_length=self.SILO_WIDTH,
                           name='S1', color=self.__silo_sensor_color)

    def __direction_left_drawing(self):
        self.create_delta_indicator(self.DIRECTION1_INDICATOR_X_POSITION,
                                    self.DIRECTION1_INDICATOR_Y_POSITION,
                                    name='M2_BAL',
                                    direction='left',
                                    color=self.__conveyor1_left_color)

    def __direction_right_drawing(self):
        # noinspection SpellCheckingInspection
        self.create_delta_indicator(self.DIRECTION2_INDICATOR_X_POSITION,
                                    self.DIRECTION2_INDICATOR_Y_POSITION,
                                    name='M2_JOBB',
                                    direction='right',
                                    color=self.__conveyor1_right_color)

    def __conveyor1_drawing(self):
        # noinspection SpellCheckingInspection
        self.create_conveyor(self.CONVEYOR1_X_POSITION,
                             self.CONVEYOR1_Y_POSITION,
                             length=self.CONVEYOR1_LENGTH, name='Szalag 1',
                             circle1_name='M2',
                             circle1_color=self.__conveyor1_motor_color,
                             circle2_name='S2',
                             circle2_color=self.__conveyor1_sensor_color)

    def __conveyor2_drawing(self):
        # noinspection SpellCheckingInspection
        self.create_conveyor(self.CONVEYOR2_X_POSITION,
                             self.CONVEYOR2_Y_POSITION,
                             length=self.CONVEYOR2_LENGTH, name='Szalag 2',
                             circle1_name='S3',
                             circle1_color=self.__conveyor2_sensor_color,
                             circle2_name='M3',
                             circle2_color=self.__conveyor2_motor_color)

    def __conveyor3_drawing(self):
        # noinspection SpellCheckingInspection
        self.create_conveyor(self.CONVEYOR3_X_POSITION,
                             self.CONVEYOR3_Y_POSITION,
                             length=self.CONVEYOR2_LENGTH, name='Szalag 3',
                             circle1_name='M4',
                             circle1_color=self.__conveyor3_motor_color,
                             circle2_name='S4',
                             circle2_color=self.__conveyor3_sensor_color)

if __name__ == '__main__':
    app = Tk()

    conveyors_frame = Conveyors(app)
    error_frame = ErrorCheckBox(app)
    conveyors_frame.pack()
    error_frame.pack()

    app.mainloop()
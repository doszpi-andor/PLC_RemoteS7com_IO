from tkinter import Frame, Checkbutton, IntVar, Tk

from _view.conveyor_canvas import ConveyorCanvas
from _view.sensor_canvas import SensorCanvas
from _view.silo_camvas import SiloCanvas

class ErrorCheckBox(Frame):

    # noinspection PyDefaultArgument
    def __init__(self,
                 master=None,
                 silo1_process=None,
                 silo2_process=None,
                 error1_process=None,
                 error2_process=None,
                 cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        self.silo1_var = IntVar()
        # noinspection SpellCheckingInspection
        self.silo1 = Checkbutton(self, variable=self.silo1_var, command=silo1_process, text='Siló 1 kifogyott')
        self.silo2_var = IntVar()
        # noinspection SpellCheckingInspection
        self.silo2 = Checkbutton(self, variable=self.silo2_var, command=silo2_process, text='Siló 2 kifogyott')

        self.error1_var = IntVar()
        # noinspection SpellCheckingInspection
        self.error1 = Checkbutton(self, variable=self.error1_var, command=error1_process, text='Szalag 1 hiba')
        self.error2_var = IntVar()
        # noinspection SpellCheckingInspection
        self.error2 = Checkbutton(self, variable=self.error2_var, command=error2_process, text='Szalag 2 hiba')

        self.silo1.grid(row=1, column=1)
        self.silo2.grid(row=1, column=2)

        self.error1.grid(row=2, column=1)
        self.error2.grid(row=2, column=2)


class Conveyors(ConveyorCanvas, SiloCanvas, SensorCanvas):
    SILO_WIDTH = 100
    SILO_HEIGHT = 150

    CONVEYOR_WIDTH = 45

    CONVEYOR1_LENGTH = 400
    CONVEYOR2_LENGTH = 400

    SILO1_X_POSITION = 5
    SILO2_X_POSITION = SILO1_X_POSITION + SILO_WIDTH + 80
    SILO1_SENSOR_X_POSITION = SILO1_X_POSITION + 5
    SILO2_SENSOR_X_POSITION = SILO2_X_POSITION + 5
    CONVEYOR1_X_POSITION = SILO1_X_POSITION
    CONVEYOR2_X_POSITION = CONVEYOR1_X_POSITION + CONVEYOR1_LENGTH * 2 // 3

    SILO_Y_POSITION = 5
    SILO_SENSOR_Y_POSITION = SILO_Y_POSITION + SILO_HEIGHT * 7 // 8
    CONVEYOR1_Y_POSITION = SILO_Y_POSITION + SILO_HEIGHT + 20
    CONVEYOR2_Y_POSITION = CONVEYOR1_Y_POSITION + CONVEYOR_WIDTH + 20

    FULL_WIDTH = CONVEYOR2_X_POSITION + CONVEYOR2_LENGTH
    FULL_HEIGHT = CONVEYOR2_Y_POSITION + CONVEYOR_WIDTH

    # noinspection PyDefaultArgument
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, width=self.FULL_WIDTH, height=self.FULL_HEIGHT, **kw)

        self.silo1_motor_color = 'gray'
        self.silo2_motor_color = 'gray'
        self.silo1_sensor_color = 'blue'
        self.silo2_sensor_color = 'blue'
        self.conveyor1_motor_color = 'gray'
        self.conveyor1_sensor_color = 'gray'
        self.conveyor2_motor_color = 'gray'
        self.conveyor2_sensor_color = 'gray'

        self.__silo1_drawing()
        self.__silo2_drawing()
        self.__conveyor1_drawing()
        self.__conveyor2_drawing()

    def silo1_change_motor_color(self, motor_color):
        if self.silo1_motor_color != motor_color:
            self.silo1_motor_color = motor_color
            self.__silo1_drawing()

    def silo1_change_sensor_color(self, sensor_color):
        if self.silo1_sensor_color != sensor_color:
            self.silo1_sensor_color = sensor_color
            self.__silo1_drawing()

    def silo2_change_motor_color(self, motor_color):
        if self.silo2_motor_color != motor_color:
            self.silo2_motor_color = motor_color
            self.__silo2_drawing()

    def silo2_change_sensor_color(self, sensor_color):
        if self.silo2_sensor_color != sensor_color:
            self.silo2_sensor_color = sensor_color
            self.__silo2_drawing()

    def conveyor1_change_motor_color(self, motor_color):
        if self.conveyor1_motor_color != motor_color:
            self.conveyor1_motor_color = motor_color
            self.__conveyor1_drawing()

    def conveyor1_change_sensor_color(self, sensor_color):
        if self.conveyor1_sensor_color != sensor_color:
            self.conveyor1_sensor_color = sensor_color
            self.__conveyor1_drawing()

    def conveyor2_change_motor_color(self, motor_color):
        if self.conveyor2_motor_color != motor_color:
            self.conveyor2_motor_color = motor_color
            self.__conveyor2_drawing()

    def conveyor2_change_sensor_color(self, sensor_color):
        if self.conveyor2_sensor_color != sensor_color:
            self.conveyor2_sensor_color = sensor_color
            self.__conveyor2_drawing()

    def __silo1_drawing(self):
        # noinspection SpellCheckingInspection
        self.create_silo(self.SILO1_X_POSITION,
                         self.SILO_Y_POSITION,
                         silo_name='Siló 1',
                         motor_name='M1', motor_color=self.silo1_motor_color)
        self.create_sensor(self.SILO1_SENSOR_X_POSITION,
                           self.SILO_SENSOR_Y_POSITION,
                           line_length=self.SILO_WIDTH,
                           name='S1', color=self.silo1_sensor_color)

    def __silo2_drawing(self):
        # noinspection SpellCheckingInspection
        self.create_silo(self.SILO2_X_POSITION,
                         self.SILO_Y_POSITION,
                         silo_name='Siló 2',
                         motor_name='M2', motor_color=self.silo2_motor_color)
        self.create_sensor(self.SILO2_SENSOR_X_POSITION,
                           self.SILO_SENSOR_Y_POSITION,
                           line_length=self.SILO_WIDTH,
                           name='S2', color=self.silo2_sensor_color)

    def __conveyor1_drawing(self):
        # noinspection SpellCheckingInspection
        self.create_conveyor(self.CONVEYOR1_X_POSITION,
                             self.CONVEYOR1_Y_POSITION,
                             length=self.CONVEYOR1_LENGTH, name='Szalag 1',
                             circle1_name='M3', circle1_color=self.conveyor1_motor_color,
                             circle2_name='S3', circle2_color=self.conveyor1_sensor_color)

    def __conveyor2_drawing(self):
        # noinspection SpellCheckingInspection
        self.create_conveyor(self.CONVEYOR2_X_POSITION,
                             self.CONVEYOR2_Y_POSITION,
                             length=self.CONVEYOR2_LENGTH, name='Szalag 2',
                             circle1_name='M4', circle1_color=self.conveyor2_motor_color,
                             circle2_name='S4', circle2_color=self.conveyor2_sensor_color)


if __name__ == '__main__':
    app = Tk()

    conveyors_frame = Conveyors(app)
    error_frame = ErrorCheckBox(app)
    conveyors_frame.pack()
    error_frame.pack()

    app.mainloop()
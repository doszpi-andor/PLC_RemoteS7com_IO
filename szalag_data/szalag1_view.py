from tkinter import Frame, IntVar, Checkbutton, Tk

from _view.conveyor_canvas import ConveyorCanvas

class ErrorCheckBox(Frame):

    # noinspection PyDefaultArgument
    def __init__(self,
                 master=None,
                 error1_process=None,
                 error2_process=None,
                 error3_process=None,
                 cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        self.error1_var = IntVar()
        # noinspection SpellCheckingInspection
        self.error1 = Checkbutton(self, variable=self.error1_var, command=error1_process, text='Szalag 1 hiba')
        self.error2_var = IntVar()
        # noinspection SpellCheckingInspection
        self.error2 = Checkbutton(self, variable=self.error2_var, command=error2_process, text='Szalag 2 hiba')
        self.error3_var = IntVar()
        # noinspection SpellCheckingInspection
        self.error3 = Checkbutton(self, variable=self.error3_var, command=error3_process, text='Szalag 3 hiba')

        self.error1.grid(row=1, column=1)
        self.error2.grid(row=1, column=2)
        self.error3.grid(row=1, column=3)


class Conveyors(ConveyorCanvas):
    CONVEYOR_WIDTH = 45

    CONVEYOR1_LENGTH = 300
    CONVEYOR2_LENGTH = 300
    CONVEYOR3_LENGTH = 400

    CONVEYOR1_X_POSITION = 5
    CONVEYOR2_X_POSITION = CONVEYOR1_X_POSITION + CONVEYOR1_LENGTH + 50
    CONVEYOR3_X_POSITION = CONVEYOR1_X_POSITION + CONVEYOR1_LENGTH * 2 // 3

    CONVEYOR1_Y_POSITION = 5
    CONVEYOR2_Y_POSITION = CONVEYOR1_Y_POSITION
    CONVEYOR3_Y_POSITION = CONVEYOR1_Y_POSITION + CONVEYOR_WIDTH + 20

    FULL_WIDTH = CONVEYOR2_X_POSITION + CONVEYOR2_LENGTH
    FULL_HEIGHT = CONVEYOR3_Y_POSITION + CONVEYOR_WIDTH

    # noinspection PyDefaultArgument
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, width=self.FULL_WIDTH, height=self.FULL_HEIGHT, **kw)

        self.__conveyor1_motor_color = 'gray'
        self.__conveyor1_sensor_color = 'gray'
        self.__conveyor2_motor_color = 'gray'
        self.__conveyor2_sensor_color = 'gray'
        self.__conveyor3_motor_color = 'gray'
        self.__conveyor3_sensor_color = 'gray'

        self.__conveyor1_drawing()
        self.__conveyor2_drawing()
        self.__conveyor3_drawing()

    def conveyor1_change_motor_color(self, motor_color):
        if self.__conveyor1_motor_color != motor_color:
            self.__conveyor1_motor_color = motor_color
            self.__conveyor1_drawing()

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

    def __conveyor1_drawing(self):
        # noinspection SpellCheckingInspection
        self.create_conveyor(self.CONVEYOR1_X_POSITION,
                             self.CONVEYOR1_Y_POSITION,
                             length=self.CONVEYOR1_LENGTH, name='Szalag 1',
                             circle1_name='M1', circle1_color=self.__conveyor1_motor_color,
                             circle2_name='S1', circle2_color=self.__conveyor1_sensor_color)

    def __conveyor2_drawing(self):
        # noinspection SpellCheckingInspection
        self.create_conveyor(self.CONVEYOR2_X_POSITION,
                             self.CONVEYOR2_Y_POSITION,
                             length=self.CONVEYOR2_LENGTH, name='Szalag 2',
                             circle1_name='S2', circle1_color=self.__conveyor2_sensor_color,
                             circle2_name='M2', circle2_color=self.__conveyor2_motor_color)

    def __conveyor3_drawing(self):
        # noinspection SpellCheckingInspection
        self.create_conveyor(self.CONVEYOR3_X_POSITION,
                             self.CONVEYOR3_Y_POSITION,
                             length=self.CONVEYOR3_LENGTH, name='Szalag 3',
                             circle1_name='M3', circle1_color=self.__conveyor3_motor_color,
                             circle2_name='S3', circle2_color=self.__conveyor3_sensor_color)


if __name__ == '__main__':
    app = Tk()

    conveyors_frame = Conveyors(app)
    error_frame = ErrorCheckBox(app)
    conveyors_frame.pack()
    error_frame.pack()

    app.mainloop()
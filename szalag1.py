from threading import Timer

from _snap7.snap7_server import S7Server
from _view.remote_io_view import RemoteIOView
from szalag_data.szalag1_data import Szalag1Data, Szalag1Address
from szalag_data.szalag1_view import Conveyors, ErrorCheckBox

class App(RemoteIOView):

    def __init__(self):
        super().__init__()

        # noinspection SpellCheckingInspection
        self.name.configure(text='Szalag 1 Remote IO')

        self.conveyors = Conveyors(self.process_frame)
        self.error_check = ErrorCheckBox(self.process_frame,
                                         error1_process=self.s1_changed,
                                         error2_process=self.s2_changed,
                                         error3_process=self.s3_changed)

        self.conveyors.pack()
        self.error_check.pack()

        self.s7_server = S7Server(ip_address=self.ip_select.ip_address, port=self.ip_select.port, s7_address=Szalag1Address())
        self.s7_server.start()

        self.data = Szalag1Data(self.s7_server)

    def s1_changed(self):
        if self.error_check.error1_var.get():
            self.conveyors.conveyor1_change_sensor_color(sensor_color='red')
            self.data.s1 = False
        else:
            if self.data.m1:
                self.conveyors.conveyor1_change_sensor_color(sensor_color='green')
                self.data.s1 = True
            else:
                self.conveyors.conveyor1_change_sensor_color(sensor_color='gray')
                self.data.s1 = False

    # noinspection DuplicatedCode
    def s2_changed(self):
        if self.error_check.error2_var.get():
            self.conveyors.conveyor2_change_sensor_color(sensor_color='red')
            self.data.s2 = False
        else:
            if self.data.m2:
                self.conveyors.conveyor2_change_sensor_color(sensor_color='green')
                self.data.s2 = True
            else:
                self.conveyors.conveyor2_change_sensor_color(sensor_color='gray')
                self.data.s2 = False

    # noinspection DuplicatedCode
    def s3_changed(self):
        if self.error_check.error3_var.get():
            self.conveyors.conveyor3_change_sensor_color(sensor_color='red')
            self.data.s3 = False
        else:
            if self.data.m3:
                self.conveyors.conveyor3_change_sensor_color(sensor_color='green')
                self.data.s3 = True
            else:
                self.conveyors.conveyor3_change_sensor_color(sensor_color='gray')
                self.data.s3 = False

    def loop(self, n):

        if self.data.m1_is_changed():
            if self.data.m1:
                self.conveyors.conveyor1_change_motor_color('green')
                s1_delay = Timer(1.5, self.s1_changed)
                s1_delay.start()
            else:
                self.conveyors.conveyor1_change_motor_color('gray')
                self.s1_changed()

        if self.data.m2_is_changed():
            if self.data.m2:
                self.conveyors.conveyor2_change_motor_color('green')
                s2_delay = Timer(1.5, self.s2_changed)
                s2_delay.start()
            else:
                self.conveyors.conveyor2_change_motor_color('gray')
                self.s2_changed()

        if self.data.m3_is_changed():
            if self.data.m3:
                self.conveyors.conveyor3_change_motor_color('green')
                s3_delay = Timer(1.5, self.s3_changed)
                s3_delay.start()
            else:
                self.conveyors.conveyor3_change_motor_color('gray')
                self.s3_changed()

        self.data.control_bit_set()

        super().loop(n)


if __name__ == "__main__":
    app = App()

    app.after(100, app.loop, 0)

    app.mainloop()

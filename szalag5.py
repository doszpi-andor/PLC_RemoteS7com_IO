from threading import Timer

from _snap7.snap7_server import S7Server
from _view.remote_io_view import RemoteIOView
from szalag_data.szalag5_data import Szalag5Data, Szalag5Address
from szalag_data.szalag5_view import Conveyors, ErrorCheckBox

class App(RemoteIOView):

    def __init__(self):
        super().__init__()

        # noinspection SpellCheckingInspection
        self.name.configure(text='Szalag 5 Remote IO')

        self.error_check = ErrorCheckBox(self.process_frame,
                                         silo1_process=self.s1_changed,
                                         silo2_process=self.s2_changed,
                                         error1_process=self.s3_changed,
                                         error2_process=self.s4_changed)
        self.conveyors = Conveyors(self.process_frame)

        self.conveyors.pack()
        self.error_check.pack()

        self.s7_server = S7Server(ip_address=self.ip_select.ip_address, port=self.ip_select.port,
                                  s7_address=Szalag5Address(), reconnect_handler=self.reconnect)
        self.s7_server.start()

        self.data = Szalag5Data(self.s7_server)

    def reconnect(self):
        self.s1_changed()
        self.s2_changed()

    def s1_changed(self):
        if self.error_check.silo1_var.get():
            self.conveyors.silo1_change_sensor_color(sensor_color='gray')
            self.data.s1 = False
        else:
            self.conveyors.silo1_change_sensor_color(sensor_color='blue')
            self.data.s1 = True

    def s2_changed(self):
        if self.error_check.silo2_var.get():
            self.conveyors.silo2_change_sensor_color(sensor_color='gray')
            self.data.s2 = False
        else:
            self.conveyors.silo2_change_sensor_color(sensor_color='blue')
            self.data.s2 = True

    # noinspection DuplicatedCode
    def s3_changed(self):
        if self.error_check.error1_var.get():
            self.conveyors.conveyor1_change_sensor_color(sensor_color='red')
            self.data.s3 = False
        else:
            if self.data.m3:
                self.conveyors.conveyor1_change_sensor_color(sensor_color='green')
                self.data.s3 = True
            else:
                self.conveyors.conveyor1_change_sensor_color(sensor_color='gray')
                self.data.s3 = False

    # noinspection DuplicatedCode
    def s4_changed(self):
        if self.error_check.error2_var.get():
            self.conveyors.conveyor2_change_sensor_color(sensor_color='red')
            self.data.s4 = False
        else:
            if self.data.m4:
                self.conveyors.conveyor2_change_sensor_color(sensor_color='green')
                self.data.s4 = True
            else:
                self.conveyors.conveyor2_change_sensor_color(sensor_color='gray')
                self.data.s4 = False

    def loop(self, n):

        if self.data.m1_is_changed():
            if self.data.m1:
                self.conveyors.silo1_change_motor_color(motor_color='green')
            else:
                self.conveyors.silo1_change_motor_color(motor_color='gray')

        if self.data.m2_is_changed():
            if self.data.m2:
                self.conveyors.silo2_change_motor_color(motor_color='green')
            else:
                self.conveyors.silo2_change_motor_color(motor_color='gray')

        if self.data.m3_is_changed():
            if self.data.m3:
                self.conveyors.conveyor1_change_motor_color(motor_color='green')
                s3_delay = Timer(1.5, self.s3_changed)
                s3_delay.start()
            else:
                self.conveyors.conveyor1_change_motor_color(motor_color='gray')
                self.s3_changed()

        if self.data.m4_is_changed():
            if self.data.m4:
                self.conveyors.conveyor2_change_motor_color(motor_color='green')
                s4_delay = Timer(1.5, self.s4_changed)
                s4_delay.start()
            else:
                self.conveyors.conveyor2_change_motor_color(motor_color='gray')
                self.s4_changed()

        self.data.control_bit_set()

        super().loop(n)


if __name__ == "__main__":
    app = App()

    app.after(100, app.loop, 0)

    app.mainloop()

from tkinter import Frame, Label, Tk

from _snap7.snap7_server import S7Server

from _view.ip_select import ToplevelIpSelect


# noinspection PyTypeChecker
class RemoteIOView(Tk):

    def __init__(self):
        super().__init__()
        self.title("Remote IO")
        self.resizable(False, False)

        self.name_frame = Frame(self)
        self.process_frame = Frame(self)
        self.connect_frame = Frame(self)

        self.name = Label(self.name_frame, text="Remote S7Connect IO", font=("Arial", 16))
        self.name.pack()

        self.server_label = Label(self.connect_frame, text='--')
        self.client_label = Label(self.connect_frame, text='--')

        self.server_label.pack()
        self.client_label.pack()

        self.name_frame.pack()
        self.process_frame.pack()
        self.connect_frame.pack()

        self.ip_select = ToplevelIpSelect(self)
        # self.ip_select.grab_set()
        self.ip_select.wait_window()


        self.s7_server: S7Server = None

    def destroy(self):
        if self.s7_server is not None:
            self.s7_server.stop()
        super().destroy()

    def loop(self, n):
        if self.s7_server is not None:
            self.server_label.configure(text=f"Server: {self.s7_server.ip_address}:{str(self.s7_server.port)}")

            if self.s7_server.connect:
                self.client_label.configure(text='PLC connected', fg='black')
            else:
                self.client_label.configure(text='PLC not connected', fg='red')
        
        self.after(100, self.loop, n)

if __name__ == "__main__":
    app = RemoteIOView()

    app.after(100, app.loop, 0)

    app.mainloop()

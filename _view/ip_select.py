from tkinter import Toplevel, StringVar, OptionMenu, Button, Label

from psutil import net_if_addrs


class ToplevelIpSelect(Toplevel):

    __port_list = ['102', '1102']

    def __init__(self, master):
        Toplevel.__init__(self, master)
        self.title("Select IP")
        self.attributes('-topmost', 'true')
        self.geometry('200x130')

        self.__ip_list = []

        self.__read_ip_list()

        self.__label = Label(self, text='Select IP')

        self.__ip_address = StringVar()
        self.__ip_address.set(self.__ip_list[0] if self.__ip_list else '')
        self.__ip_option_menu = OptionMenu(self, self.__ip_address, *self.__ip_list)

        self.__port = StringVar()
        self.__port.set(self.__port_list[0] if self.__port_list else '102')
        self.__port_option_menu = OptionMenu(self, self.__port, *self.__port_list)

        self.__button = Button(self, text='Select', command=self.__select_ip)

        self.__label.pack()
        self.__ip_option_menu.pack()
        self.__port_option_menu.pack()
        self.__button.pack()

    @property
    def ip_address(self):
        return self.__ip_address.get()

    @property
    def port(self):
        return int(self.__port.get())

    def __select_ip(self):
        self.destroy()

    def __read_ip_list(self):
        # noinspection SpellCheckingInspection
        for interface, addrs in net_if_addrs().items():
            if interface != "lo":  # Exclude loopback interface
                for addr in addrs:
                    if addr.family == 2 and addr.address != '127.0.0.1':
                        self.__ip_list.append(addr.address)

    def __str__(self):
        return self.__ip_address.get()

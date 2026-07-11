from threading import Timer
from time import sleep

from snap7 import Server, SrvArea

class S7Address:
    RECEIVE_ADDRESS = {'address': '', 'size': None}
    TRANSMIT_ADDRESS = {'address': '', 'size': None}

    RECEIVE_BIT_ADDRESS = {}
    TRANSMIT_DATA_ADDRESS = {}

    @staticmethod
    def area(address: str):
        if address.startswith('Q'):
            return SrvArea.PA
        elif address.startswith('I'):
            return SrvArea.PE
        else:
            raise ValueError(f"Invalid address: {address}")
        
    @staticmethod
    def index(address: str):
        try:
            if address.startswith('Q') or address.startswith('I'):
                return int(address[2:])
            else:
                raise ValueError
        except ValueError:
            raise ValueError(f"Invalid address: {address}")

    @staticmethod
    def bit_address(address: str | int):
        try:
            if isinstance(address, str):
                bit_address, bit_index = int(address.split('.')[0]), int(address.split('.')[1])
            elif isinstance(address, int):
                bit_address, bit_index = S7Address.calc_bit_address(address)
            else:
                raise ValueError

            return bit_address, bit_index
        except (IndexError, ValueError):
            raise ValueError(f"Invalid address: {address}")

    @staticmethod
    def calc_bit_address(address: int):
        if address < 0:
            raise ValueError(f"Invalid address: {address}")

        bit_index = address
        bit_address = 0
        while bit_index >= 8:
            bit_index -= 8
            bit_address += 1

        return bit_address, bit_index

class S7Data:
    def __init__(self, server: S7Server):
        self.__s7_server = server

    def read_receive_bit(self, bit_address: int | str):
        return self.__s7_server.read_receive_bit(bit_address)

    def set_transmit_bit(self, bit_address: int, value: bool):
        self.__s7_server.set_transmit_bit(bit_address, value)

class S7Server:

    TIMEOUT = 1

    __transmit_data: bytearray
    __receive_data: bytearray

    def __init__(self, ip_address: str, port: int = 102, s7_address: S7Address = S7Address(), reconnect_handler = None):
        self.__ip_address = ip_address
        self.__port = port

        self.__connect = False
        self.__reconnect_handler = reconnect_handler

        self.__server = Server()
        self.__server.host = self.__ip_address

        self.__server.set_read_events_callback(self.__read_event)

        self.__timer = Timer(self.TIMEOUT, self.__timer_handler)
        self.__timer.start()

        self.__control_bit = False

        if s7_address.RECEIVE_ADDRESS['size'] is not None:
            # noinspection PyTypeChecker
            self.__receive_data = bytearray(s7_address.RECEIVE_ADDRESS['size'])

            self.__clear_buffer(self.__receive_data)

            # noinspection PyTypeChecker
            self.__server.register_area(s7_address.area(s7_address.RECEIVE_ADDRESS['address']), s7_address.index(s7_address.RECEIVE_ADDRESS['address']), self.__receive_data)

        if s7_address.TRANSMIT_ADDRESS['size'] is not None:
            # noinspection PyTypeChecker
            self.__transmit_data = bytearray(s7_address.TRANSMIT_ADDRESS['size'])

            self.__clear_buffer(self.__transmit_data)

            # noinspection PyTypeChecker
            self.__server.register_area(s7_address.area(s7_address.TRANSMIT_ADDRESS['address']), s7_address.index(s7_address.TRANSMIT_ADDRESS['address']), self.__transmit_data)

    @property
    def ip_address(self):
        return self.__ip_address
    
    @property
    def port(self):
        return self.__port

    @property
    def connect(self):
        return self.__connect

    def start(self):
        self.__server.start(self.__port)

    def stop(self):
        self.__server.stop()
        self.__timer.cancel()

    def register_area(self, area: SrvArea, index: int, data: bytearray):
        self.__server.register_area(area, index, data)

    def read_receive_bit(self, bit_address: int | str):
        address, index = S7Address.bit_address(bit_address)
        return bool(self.__receive_data[address] & (0x01 << index))

    def set_transmit_bit(self, bit_address: int, value: bool):
        address, index = S7Address.bit_address(bit_address)
        if value:
            self.__transmit_data[address] |= (0x01 << index)
        else:
            self.__transmit_data[address] &= ~(0x01 << index)

    # noinspection PyUnusedLocal
    def __read_event(self, event):
        if not self.__connect and self.__reconnect_handler:
            self.__reconnect_handler()
        self.__connect = True
        self.__control_bit = True

    def __timer_handler(self):
        if not self.__control_bit:
            self.__clear_buffer(self.__receive_data)
            self.__clear_buffer(self.__transmit_data)
            self.__connect = False

        self.__control_bit = False

        self.__timer = Timer(self.TIMEOUT, self.__timer_handler)
        self.__timer.start()

    @staticmethod
    def __clear_buffer(buffer: bytearray):
        for index in range(len(buffer)):
            buffer[index] = 0x00
    
if __name__ == "__main__":
    class TestS7Server(S7Address):
        RECEIVE_ADDRESS = {'address': 'QB0', 'size': 1}
        TRANSMIT_ADDRESS = {'address': 'IB0', 'size': 1}


    s7_server = S7Server(ip_address="192.168.90.190", port=102, s7_address=TestS7Server())
    s7_server.start()

    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        s7_server.stop()
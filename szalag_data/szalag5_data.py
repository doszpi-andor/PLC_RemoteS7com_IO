from _snap7.snap7_server import S7Address, S7Data, S7Server


# noinspection SpellCheckingInspection
class Szalag5Address(S7Address):
    RECEIVE_ADDRESS = {'address': 'QB0', 'size': 1}
    TRANSMIT_ADDRESS = {'address': 'IB0', 'size': 1}

    RECEIVE_BIT_ADDRESS = {'M1': 0, 'M2': 1, 'M3': 2, 'M4': 3}
    TRANSMIT_DATA_ADDRESS = {'S1': 0, 'S2': 1, 'S3': 2, 'S4': 3, 'control_bit': 7}


# noinspection SpellCheckingInspection
class Szalag5Data(S7Data):

    __m1_old = False
    __m2_old = False
    __m3_old = False
    __m4_old = False

    def __init__(self, server: S7Server):
        super().__init__(server)

        self.__s1 = False
        self.__s2 = False
        self.__s3 = False
        self.__s4 = False

        self.__m1 = False
        self.__m2 = False
        self.__m3 = False
        self.__m4 = False

    @property
    def s1(self):
        return self.__s1

    @s1.setter
    def s1(self, value):
        if value not in [True, False]:
            raise ValueError('S1 must be True or False')
        self.__s1 = value
        self.set_transmit_bit(Szalag5Address.TRANSMIT_DATA_ADDRESS['S1'], self.__s1)

    @property
    def s2(self):
        return self.__s2

    @s2.setter
    def s2(self, value):
        if value not in [True, False]:
            raise ValueError('S2 must be True or False')
        self.__s2 = value
        self.set_transmit_bit(Szalag5Address.TRANSMIT_DATA_ADDRESS['S2'], self.__s2)

    @property
    def s3(self):
        return self.__s3

    @s3.setter
    def s3(self, value):
        if value not in [True, False]:
            raise ValueError('S3 must be True or False')
        self.__s3 = value
        self.set_transmit_bit(Szalag5Address.TRANSMIT_DATA_ADDRESS['S3'], self.__s3)

    @property
    def s4(self):
        return self.__s4

    @s4.setter
    def s4(self, value):
        if value not in [True, False]:
            raise ValueError('S4 must be True or False')
        self.__s4 = value
        self.set_transmit_bit(Szalag5Address.TRANSMIT_DATA_ADDRESS['S4'], self.__s4)

    @property
    def m1(self):
        self.__m1 = self.__get_m1()
        return self.__m1

    def m1_is_changed(self) -> bool:
        self.__m1 = self.__get_m1()
        if self.__m1 != self.__m1_old:
            self.__m1_old = self.__m1
            return True
        else:
            return False

    @property
    def m2(self):
        self.__m2 = self.__get_m2()
        return self.__m2

    def m2_is_changed(self) -> bool:
        self.__m2 = self.__get_m2()
        if self.__m2 != self.__m2_old:
            self.__m2_old = self.__m2
            return True
        else:
            return False

    @property
    def m3(self):
        self.__m3 = self.__get_m3()
        return self.__m3

    def m3_is_changed(self) -> bool:
        self.__m3 = self.__get_m3()
        if self.__m3 != self.__m3_old:
            self.__m3_old = self.__m3
            return True
        else:
            return False

    @property
    def m4(self):
        self.__m4 = self.__get_m4()
        return self.__m4

    def m4_is_changed(self) -> bool:
        self.__m4 = self.__get_m4()
        if self.__m4 != self.__m4_old:
            self.__m4_old = self.__m4
            return True
        else:
            return False

    def control_bit_set(self):
        self.set_transmit_bit(Szalag5Address.TRANSMIT_DATA_ADDRESS['control_bit'], True)

    def __get_m1(self):
        return self.read_receive_bit(Szalag5Address.RECEIVE_BIT_ADDRESS['M1'])

    def __get_m2(self):
        return self.read_receive_bit(Szalag5Address.RECEIVE_BIT_ADDRESS['M2'])

    def __get_m3(self):
        return self.read_receive_bit(Szalag5Address.RECEIVE_BIT_ADDRESS['M3'])

    def __get_m4(self):
        return self.read_receive_bit(Szalag5Address.RECEIVE_BIT_ADDRESS['M4'])

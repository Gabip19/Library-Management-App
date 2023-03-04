class DataTransfer:
    """
    Clasa responsabila cu transferul datelor
    """
    def __init__(self, value1, value2, value3):
        self.__field1 = value1
        self.__field2 = value2
        self.__field3 = value3

    """GETTERS"""
    def get_field1(self):
        return self.__field1

    def get_field2(self):
        return self.__field2

    def get_field3(self):
        return self.__field3


    """SETTERS"""
    def set_field1(self, value):
        self.__field1 = value

    def set_field2(self, value):
        self.__field2 = value

    def set_field3(self, value):
        self.__field3 = value

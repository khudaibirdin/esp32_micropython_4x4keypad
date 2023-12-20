class ClassKeypad:
    def __init__(self, pcf8574):
        self.pcf8574 = pcf8574
        self.keypad = [['1', '2', '3', 'A', 'None'],
                       ['4', '5', '6', 'B', 'None'],
                       ['7', '8', '9', 'C', 'None'],
                       ['*', '0', '#', 'D', 'None'],
                       ['None', 'None', 'None', 'None', 'None']]
        self.decoded = [4,4,4,4,4,4,4,0,4,4,4,1,4,2,3,4,4]
        self.result = (4, 4)
        self.previous_result = 'None'
        self.previous = 'None'
        self.is_pressed = False

    def __toggle_and_check(self):
        self.pcf8574.port = 0xF0
        row = self.decoded[self.pcf8574.port >> 4]
        self.pcf8574.port = 0x0F
        column = self.decoded[self.pcf8574.port]
        self.result = (row, column)

    def __transform_to_keys(self):
        result = self.keypad[int(self.result[0])][int(self.result[1])]
        return result
        
    def process(self):
        self.__toggle_and_check()
        result = self.__transform_to_keys()
        if result != 'None':
            self.is_pressed = True
        else:
            self.is_pressed = False
        if self.previous != result and result != 'None':
            self.previous = result
        if not self.is_pressed and self.previous_result != self.previous:
            self.previous_result = self.previous
        return result
            
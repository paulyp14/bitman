

class HammingBit:
    def __init__(self, place, value, is_redundant):
        self.place = place
        self.value = value
        self.is_redundant = is_redundant

    def __str__(self):
        return f'HammingBit(value = {self.value}, is_redundant = {self.is_redundant})'

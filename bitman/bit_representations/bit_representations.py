from bitstring import Bits
from enum import Enum
from bit_representations import bit_manipulation as bm

class BitTypes(Enum):
    Unsigned = 1
    SignedMagnitude = 2
    OnesComplement = 3
    TwosComplement = 4
    FloatingPoint = 5


class BitString():

    def __init__(self, bits, bit_type, bit_limit=None):
        self.bits = bits
        self.sign = None
        self.value = None
        self.magnitude = None
        self._divisions = None
        self.bit_limit = bit_limit
        self._mag_pad = ''
        self.ensure_length()
        self._set_type(bit_type)

    def set_type(self, type_):
        if type_ == BitTypes.Unsigned:
            # it is the literal value of the string
            self.magnitude = self.bits
            self._set_value()
            self._divisions = (len(self.bits))
        elif type_ == BitTypes.SignedMagnitude:
            self._mag_pad = ' '
            # it is signed, so it is the literal value of all bits following the sign bit
            self.magnitude = self.bits[1::]
            self._set_value()
            # if the sign bit is one, it's negative
            self.set_negative_value()
            self._divisions = (1, len(self.bits[1::]))
        elif type_ == BitTypes.OnesComplement:
            self._mag_pad = ' '
            if self.check_negative():
                self.flip()
                self.magnitude = self.magnitude[1::]
            else:
                self.magnitude = self.bits[1::]
            self._set_value()
            self.set_negative_value()
            self._divisions = (1, len(self.bits[1::]))
        elif type_ == BitTypes.TwosComplement:
            self._mag_pad = ' '
            if self.check_negative():
                self.flip()
                self.magnitude = self.magnitude[1::]
            else:
                self.magnitude = self.bits[1::]
            self.add('1')
            self._set_value()
            self.set_negative_value()
            self._divisions = (1, len(self.bits[1::]))

        else:
            raise KeyError('No valid BitType given')
        self.type_ = bit_type

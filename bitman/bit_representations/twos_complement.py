from bitman.bit_representations.ones_complement import OnesComplement
from bitman.bit_representations.bit_manipulation import *


class TwosComplement(OnesComplement):
    def __init__(self, bits, fixed_len: bool=False, max_len: int=None):
        OnesComplement.__init__(self, bits, fixed_len=fixed_len, max_len=max_len)

    def check_negative(self):
        if self.bits[0] == '1':
            self.set_magnitude(bin_add(flip_bits(self.bits), '1'))
            self.magnitude *= -1
            self.is_negative = True

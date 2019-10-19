from bitman.bit_representations.bit_repr import BitRepr
from bitman.bit_representations.bit_manipulation import *


class OnesComplement(BitRepr):

    def __init__(self, bits, fixed_len: bool=False, max_len: int=None):
        BitRepr.__init__(self, _preserve_sign(bits, fixed_len, max_len), fixed_len=fixed_len, max_len=max_len)
        self.is_negative = False

        self.check_negative()

    def check_negative(self):
        if self.bits[0] == '1':
            self.set_magnitude(flip_bits(self.bits))
            self.magnitude *= -1
            self.is_negative = True

    def _validate_string(self):
        return (BitRepr._validate_string(self) +
                f"""  is_negative : {self.is_negative}
                """
                )


def _preserve_sign(bits, fixed_len: bool=False, max_len: int=None):
    if fixed_len and max_len is not None:
        sign = bits[0]
        pad = '1' if sign == '1' else '0'
        return bits[0] + pad * (max_len - len(bits)) + bits[1::]
    else:
        return bits

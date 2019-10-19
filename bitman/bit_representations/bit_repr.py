from bitman.bit_representations.bit_manipulation import *


class BitRepr:

    def __init__(self, bits: str, base: int=2, fixed_len: bool=False, max_len: int=None):
        self.bits = None
        self.base = None
        self.length = None
        self.magnitude = None
        self.fixed_len = None
        self.max_len = None
        self.update(bits, base, fixed_len, max_len)

    def update(self, bits: str, base: int=2, fixed_len: bool=False, max_len: int=None):
        self.bits = bits
        self.base = base
        self.length = len(bits)
        self.magnitude = convert_from_base_to_base10(self.bits, self.base)
        self.fix_length(fixed_len, max_len)

    def fix_length(self, fixed_len, max_len):
        self.fixed_len = False
        if fixed_len:
            self.fixed_len = True
            if max_len is None:
                self.max_len = self.length
            else:
                self.max_len = max_len
        self.populate_fixed()

    def populate_fixed(self):
        if self.fixed_len:
            if self.length < self.max_len:
                self.pad_bits('0' * (self.max_len - self.length) + self.bits)

    def pad_bits(self, bits):
        self.bits = bits
        self.length = len(bits)

    def set_magnitude(self, bits=None):
        if bits is None:
            self.magnitude = convert_from_base_to_base10(self.bits, self.base)
        else:
            self.magnitude = convert_from_base_to_base10(bits, self.base)

    def __repr__(self):
        return f'BitRepr(\'{self.bits}\', {self.base}, {self.fixed_len}, {self.max_len})'

    def _validate_string(self):
        return f"""
        Class {self.__class__.__name__}:
          bits      : {self.bits}
          base      : {self.base}
          length    : {self.length}
          magnitude : {self.magnitude}
          fixed_len : {self.fixed_len}
          max_len   : {self.max_len}
        """

    def _print_validate(self):
        print(self._validate_string())

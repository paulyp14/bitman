from bitman.hamming.hamming_exception import HammingException
from bitman.hamming.hamming_bit import HammingBit
from bitman.utilities.utilities import *


class HammingEncoder:
    def __init__(self, data=None, data_bits=None, parity='even'):

        if data is not None:
            data_bits = len(data)
        elif data_bits is None:
            raise HammingException(3)

        self.data_bits = data_bits
        self.redundant_bits = HammingEncoder.calculate_redundant_bits(self.data_bits)
        self.length = self.redundant_bits + self.data_bits
        self._redundant_positions = [2 ** i for i in range(self.redundant_bits)]
        self.parity = None
        self.parity_ranges = None
        self.encoding = {
            i + 1: HammingBit(
                i + 1,
                ' ',
                (True if i + 1 in self._redundant_positions else False)
            )
            for i in range(self.data_bits + self.redundant_bits)
        }
        if data is not None:
            self.fill(data)
        self.set_parity(parity)

    def fill_parity_bits(self):
        self.generate_parity_range()
        parity_matches = self.check_parity_bit_value()
        self.reset_parity_bits(parity_matches)

    def check_parity_bit_value(self):
        def get_bitval(idx):
            bitval = self.encoding[idx].value
            if bitval == ' ':
                bitval = 0
            return int(bitval)

        def parity_match(idx):
            bits_involved = self.parity_ranges[idx]
            bits_sum = sum([get_bitval(j) for j in bits_involved if j != idx])
            if self.parity == 'even':
                return bits_sum % 2 == 0
            else:
                return bits_sum % 2 == 1

        return {i: parity_match(i) for i in self._redundant_positions}

    def reset_parity_bits(self, matches=None):
        if matches is None:
            pass
        for k, v in matches.items():
            if v:
                self.encoding[k].value = '0'
            else:
                self.encoding[k].value = '1'

    def generate_parity_range(self):
        self.parity_ranges = {}
        for i in self._redundant_positions:
            step = 2 * i
            num_groups = int(self.length / step) + 1
            self.parity_ranges[i] = []
            for j in range(num_groups):
                start = (j * step) + i
                full_end = start + i
                if full_end > self.length:
                    full_end = self.length + 1
                for idx in range(start, full_end):
                    self.parity_ranges[i].append(idx)

    def fill(self, data):
        data_range = [i for i in self.encoding.keys() if self.encoding[i].is_redundant == False]
        for i, j in enumerate(data_range):
            self.encoding[j].value = data[i]

    def validate_parity(self, parity=None):
        valid_parities = ['even', 'odd']
        if parity is None:
            return self.parity in valid_parities
        else:
            return parity in valid_parities

    def set_parity(self, parity=None):
        if self.validate_parity(parity):
            self.parity = parity
        else:
            raise HammingException(4)

    def render_string(self, html=False):
        breaker = '\n' if not html else '<br>'
        max_length = max([len(str(i)) for i in self.encoding.keys()])
        chars = [HammingEncoder.rendered_char(bit, max_length) for bit in list(self.encoding.values())[::-1]]
        return breaker.join(["".join([c[i] for c in chars]) for i in range(5)])

    def get_as_html(self):
        return render_html(self.render_string(html=True))

    def __print__(self):
        print(self.render_string())

    def rendered_char(bit: HammingBit, max_length=3):

        val_dif = max_length - len(str(bit.value))
        pdif = max_length - len(str(bit.place))

        if bit.is_redundant:
            return [
                f'-{"-" * max_length}-',
                f'|{" " * val_dif}{bit.value}|',
                f'|{"-" * max_length}|',
                f'|{" " * pdif}{bit.place}|',
                f'-{"-" * max_length}-',
            ]
        else:
            return [
                f' {" " * max_length} ',
                f' {" " * val_dif}{bit.value} ',
                f' {"-" * max_length} ',
                f' {" " * pdif}{bit.place} ',
                f' {" " * max_length} ',
            ]

    @staticmethod
    def calculate_redundant_bits(data_bits: int):
        m = data_bits + 1
        for r in range(1000):
            if m + r <= 2 ** r:
                return r
        raise HammingException(2)

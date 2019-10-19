from bitman.hamming.hamming_exception import HammingException
from bitman.hamming.hamming_bit import HammingBit
from bitman.utilities.utilities import *


class HammingEncoder:
    def __init__(self, data=None, data_bits=None):

        if data is not None:
            data_bits = len(data)
        elif data_bits is None:
            raise HammingException(3)

        self.data_bits = data_bits
        self.redundant_bits = HammingEncoder.calculate_redundant_bits(self.data_bits)
        self._redundant_positions = [2 ** i for i in range(self.redundant_bits)]
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

    def fill(self, data):
        data_range = [i for i in self.encoding.keys() if self.encoding[i].is_redundant == False]
        for i, j in enumerate(data_range):
            self.encoding[j].value = data[i]

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

    def calculate_redundant_bits(data_bits: int):
        m = data_bits + 1
        for r in range(1000):
            if m + r <= 2 ** r:
                return r
        raise HammingException(2)

from bit_representations import *
from functools import reduce

_DIGIT_DICT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'a': 10,
    'b': 11,
    'c': 12,
    'd': 13,
    'e': 14,
    'f': 15,
    'g': 16,
    'h': 17,
    'i': 18,
    'j': 19,
    'k': 20,
    'l': 21,
    'm': 22,
    'n': 23,
    'o': 24,
    'p': 25,
    'q': 26,
    'r': 27,
    's': 28,
    't': 29,
    'u': 30,
    'v': 31,
    'w': 32,
    'x': 33,
    'y': 34,
    'z': 35,
}

_BASE_DICT = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    '11': 11,
    '12': 12,
    '13': 13,
    '14': 14,
    '15': 15,
    '16': 16,
    '17': 17,
    '18': 18,
    '19': 19,
    '20': 20,
    '21': 21,
    '22': 22,
    '23': 23,
    '24': 24,
    '25': 25,
    '26': 26,
    '27': 27,
    '28': 28,
    '29': 29,
    '30': 30,
    '31': 31,
    '32': 32,
    '33': 33,
    '34': 34,
    '35': 35,
    '36': 36,
    'binary': 2,
    'bin': 2,
    'decimal': 10,
    'dec': 10,
    'hexadecimal': 16,
    'hex': 16,
}


def flip_bits(bits):
    '''
    Function to flip all bits in a bitstring

    :param bits: a string of bits to be flipped

    :returns: a string of bits of the same length, where every 1-bit in the bits input string is now a 0
              and every 0-bit in the bits input string is now a 1
    '''
    return ''.join(map(lambda x: '0' if x == '1' else '1', bits))


def negative_if_applicable(bits, value):
    '''
    Function to check if the magnitude of a bitstring needs to be negative

    :param bits: a bitstring
    :param value: the integer value of that bitstring

    :returns: the value, negative if required
    '''
    if bits[0] == '1':
        return value * -1
    else:
        return value


def bin_add(x, y, verbose=False):
    '''
    Method to do binary addition of two bitstrings
    This method does not take into account the sign bit

    :param x: a string of bits
    :param y: a string of bits
    :param verbose: a boolean indicating whether to print as the operation is happening

    :returns: the result of adding the two strings together
              if there is carryout from the most significant bit, then the result will be longer than the initial inputs
    '''

    # pad the shorter bitstring with zeros
    if len(x) > len(y):
        y = '0' * (len(x) - len(y)) + y
    elif len(y) > len(x):
        x = '0' * (len(y) - len(x)) + x
    # do some printing if needed
    if verbose:
        print(f'  {x}')
        print(f'+ {y}')
        print('-'*(len(x) + 2))
    # decls
    carry = 0
    bits = []
    pad = ' '
    # for each bit in the two strings
    for i, j in zip(x[::-1], y[::-1]):
        # add the bits and any carry from the last operation
        res = int(i) + int(j) + carry
        # set the carry for the next
        carry = 1 if res > 1 else 0
        # set the individual bit result
        res = 1 if res == 3 else (0 if res == 2 else res)
        # store the result
        bits.append(str(res))
    # change the padding for printing , add any carry from MSB
    if carry != 0:
        pad = ''
        bits.append(str(carry))
    # flip the result
    result = ''.join(bits[::-1])
    # print the result if required
    if verbose:
        print(f' {pad}{result}')
        print(f' {pad}{int(result, 2)} -> base 10')
    # return the resu;t
    return result


def digit_values(digit, base):
    '''
    Function that returns the value in base10 of a digit in a specific base

    :param digit: the original digit
    :param base: the base

    :returns: the value of the digit
    '''
    # get the digit value
    dval = _DIGIT_DICT[digit]
    # if value is larger than base, there's a problem
    if dval >= base:
        raise KeyError('Values larger than base detected')
    return dval


def convert_from_base_to_base10(value, base):
    '''
    Function that converts a value string from the specified base to base10

    :param value: the value to convert
    :param base: the base to convert from

    :returns: the converted value string in base10
    '''
    base = _BASE_DICT[base]
    # for each individual digit in value (from right to left)
    # mutliply the value of the digit by base ^ position
    # sum all the values of the digits
    return reduce(lambda x, y: x + y, [digit_values(v, base) * (base**i) for i, v in enumerate(value[::-1])])


def convert_from_base10_to_base(value, base):
    '''
    Function that converts a value string from base10 to the specified base

    :param value: a base10 number
    :param base: the desired base to convert to

    :returns: the base10 number as a string of the specified base
    '''
    dig_conv = {v: k for k, v in _DIGIT_DICT.items()}
    value = int(value)
    digits = []
    while value != 0:
        digits.append(dig_conv[value % base])
        value = int(value / base)
    return ''.join(digits[::-1])


def converter(value, base, targetbase, basetype=None):
    '''
    Function that converts 
    '''
    base_10 = None
    base = str(base).lower()
    targetbase = str(targetbase)
    # make sure base is supported
    if base not in _BASE_DICT.keys():
        print('Base not supported')
        return None
    # make sure target is supported
    if targetbase not in _BASE_DICT.keys():
        print('Base not supported')
    # convert value to base 10
    base_10 = convert_from_base_to_base10(value, base)
    print(f'value in base 10 is {base_10}')
    # convert value to targetbase
    value = convert_from_base10_to_base(base_10, _BASE_DICT[targetbase])
    print(f'value in base {targetbase} is {value}')
    return value

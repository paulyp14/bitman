from bitman.bit_representations.config_dicts import DIGIT_DICT, BASE_DICT
from functools import reduce


def flip_bits(bits):
    """
    Function to flip all bits in a bitstring

    :param bits: a string of bits to be flipped

    :returns: a string of bits of the same length, where every 1-bit in the bits input string is now a 0
              and every 0-bit in the bits input string is now a 1
    """
    return ''.join(map(lambda x: '0' if x == '1' else '1', bits))


def negative_if_applicable(bits, value):
    """
    Function to check if the magnitude of a bitstring needs to be negative

    :param bits: a bitstring
    :param value: the integer value of that bitstring

    :returns: the value, negative if required
    """
    if bits[0] == '1':
        return value * -1
    else:
        return value


def bin_add(x, y, verbose=False):
    """
    Method to do binary addition of two bitstrings
    This method does not take into account the sign bit

    :param x: a string of bits
    :param y: a string of bits
    :param verbose: a boolean indicating whether to print as the operation is happening

    :returns: the result of adding the two strings together
              if there is carryout from the most significant bit, then the result will be longer than the initial inputs
    """

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
    """
    Function that returns the value in base10 of a digit in a specific base

    :param digit: the original digit
    :param base: the base

    :returns: the value of the digit
    """
    # get the digit value
    dval = DIGIT_DICT[digit]
    # if value is larger than base, there's a problem
    if dval >= base:
        raise KeyError('Values larger than base detected')
    return dval


def convert_from_base_to_base10(value, base):
    """
    Function that converts a value string from the specified base to base10

    :param value: the value to convert
    :param base: the base to convert from

    :returns: the converted value string in base10
    """
    base = BASE_DICT[str(base)]
    # for each individual digit in value (from right to left)
    # mutliply the value of the digit by base ^ position
    # sum all the values of the digits
    return reduce(lambda x, y: x + y, [digit_values(v, int(base)) * (int(base)**i) for i, v in enumerate(value[::-1])])


def convert_from_base10_to_base(value, base):
    """
    Function that converts a value string from base10 to the specified base

    :param value: a base10 number
    :param base: the desired base to convert to

    :returns: the base10 number as a string of the specified base
    """
    dig_conv = {v: k for k, v in DIGIT_DICT.items()}
    value = int(value)
    digits = []
    while value != 0:
        digits.append(dig_conv[value % base])
        value = int(value / base)
    return ''.join(digits[::-1])


def converter(value, base, targetbase):
    """
    Function that converts 
    """
    base = str(base).lower()
    targetbase = str(targetbase)
    # make sure base is supported
    if base not in BASE_DICT.keys():
        print('Base not supported')
        return None
    # make sure target is supported
    if targetbase not in BASE_DICT.keys():
        print('Base not supported')
    # convert value to base 10
    base_10 = convert_from_base_to_base10(value, base)
    print(f'value in base 10 is {base_10}')
    # convert value to targetbase
    value = convert_from_base10_to_base(base_10, BASE_DICT[targetbase])
    print(f'value in base {targetbase} is {value}')
    return value

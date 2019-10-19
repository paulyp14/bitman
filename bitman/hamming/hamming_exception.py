class HammingException(Exception):

    def __init__(self, selector):
        Exception.__init__(self, MESSAGES[selector])

MESSAGES = {
        1: 'Not all codes of the same length',
        2: 'Invalid number of bits requested',
        3: 'Can\'t encode an empty bitstring',
        4: 'Invalide parity',
    }
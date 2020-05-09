# Generate random data for writing into DBs

import random

from common.consts import SAMPLE_IMAGE


def data_generator(count):
    with open(SAMPLE_IMAGE, 'rb') as f:
        picture = f.read()

    for index in range(count):
        name = ''.join([chr(random.randint(65, 90)) for _ in range(8)])
        is_male = bool(random.randint(0, 1))

        data = {'index': index,
                'name': name,
                'is_male': is_male,
                'picture': picture}

        yield data

# -*- coding: utf-8 -*-
import string

INPUT_FILENAME = 'input'
INPUT_PATH = f'./{INPUT_FILENAME}'


LOWER_ALPHABET = list(string.ascii_lowercase)
LOWER_PRIORITY = list(map(lambda x: x, range(1, 27)))
UPPER_ALPHABET = list(string.ascii_uppercase)
UPPER_PRIORITY = list(map(lambda x: x, range(27, 53)))

PRIORITIES = {
    **dict(zip(LOWER_ALPHABET, LOWER_PRIORITY)),
    **dict(zip(UPPER_ALPHABET, UPPER_PRIORITY))
}

if __name__ == '__main__':
    with open(INPUT_PATH) as f:
        lines = map(lambda x: x.replace('\n', ''), f.readlines())
        priorities = 0
        for line in lines:
            half = len(line) // 2
            first_compartment = line[:half]
            second_compartment = line[half:]
            common = set(first_compartment) & set(second_compartment)
            priorities += PRIORITIES[common.pop()]
        print(f'Sum of priorities is: {priorities}')

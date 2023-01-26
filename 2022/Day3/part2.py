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
        rucksacks = ['', '', '']
        for index, line in enumerate(lines):
            work_index = index % 3
            if work_index == 0:
                rucksacks = ['', '', '']
            rucksacks[work_index] = line
            if work_index == 2:
                common = set(rucksacks[0]) & set(rucksacks[1]) & set(rucksacks[2])
                priorities += PRIORITIES[common.pop()]
        print(f'Sum of priorities is: {priorities}')

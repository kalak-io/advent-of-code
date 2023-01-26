# -*- coding: utf-8 -*-
import re

INPUT_FILENAME = 'input'
INPUT_PATH = f'./{INPUT_FILENAME}'
START_LINE = 10

STACKS = {
    "1": ["B", "V", "S", "N", "T", "C", "H", "Q"],
    "2": ["W", "D", "B", "G"],
    "3": ["F", "W", "R", "T", "S", "Q", "B"],
    "4": ["L", "G", "W", "S", "Z", "J", "D", "N"],
    "5": ["M", "P", "D", "V", "F"],
    "6": ["F", "W", "J"],
    "7": ["L", "N", "Q", "B", "J", "V"],
    "8": ["G", "T", "R", "C", "J", "Q", "S", "N"],
    "9": ["J", "S", "Q", "C", "W", "D", "M"]
}


if __name__ == '__main__':
    with open(INPUT_PATH) as f:
        lines = map(lambda x: x.replace('\n', ''), f.readlines()[START_LINE:])
        result = ''
        pattern = r"\b\d+\b" # Extract list of digits in commands
        for line in lines:
            n_crates_to_move, origin, dest = re.findall(pattern, line)
            moving_crates = STACKS[origin][-int(n_crates_to_move):]
            STACKS[dest] = [*STACKS[dest], *moving_crates]
            STACKS[origin] = STACKS[origin][:-int(n_crates_to_move)]
        for value in STACKS.values():
            result += value[-1]
        print(f'The crates ends up on top of each stack are {result}')

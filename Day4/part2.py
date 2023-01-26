# -*- coding: utf-8 -*-

INPUT_FILENAME = 'input'
INPUT_PATH = f'./{INPUT_FILENAME}'

if __name__ == '__main__':
    with open(INPUT_PATH) as f:
        lines = map(lambda x: x.replace('\n', ''), f.readlines())
        count_overlap = 0
        for line in lines:
            pairs = line.split(',')
            range_first_elf = pairs[0].split('-')
            sections_first_elf = list(map(lambda x: x, range(int(range_first_elf[0]), int(range_first_elf[1]) + 1)))
            range_second_elf = pairs[1].split('-')
            sections_second_elf = list(map(lambda x: x, range(int(range_second_elf[0]), int(range_second_elf[1]) + 1)))
            if set(sections_first_elf) & set(sections_second_elf):
                count_overlap += 1
        print(f'There are {count_overlap} overlaps.')

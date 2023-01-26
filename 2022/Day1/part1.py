# -*- coding: utf-8 -*-

INPUT_FILENAME = 'input'
INPUT_PATH = f'./{INPUT_FILENAME}'

if __name__ == '__main__':
    with open(INPUT_PATH) as f:
        lines = f.readlines()
        highTotalCalories = 0
        currentTotalCalories = 0
        for line in lines:
            line = line.replace('\n', '')
            if not line:
                highTotalCalories = currentTotalCalories if currentTotalCalories > highTotalCalories else highTotalCalories;
                currentTotalCalories = 0
            else:
                currentTotalCalories = currentTotalCalories + int(line)
        print(f'The elf with the most calories has {highTotalCalories} calories.')

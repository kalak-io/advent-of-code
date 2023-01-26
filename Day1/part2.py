# -*- coding: utf-8 -*-

INPUT_FILENAME = 'input'
INPUT_PATH = f'./{INPUT_FILENAME}'

if __name__ == '__main__':
    with open(INPUT_PATH) as f:
        lines = map(lambda x: x.replace('\n', ''), f.readlines())
        topElfes = [0, 0, 0]
        currentTotalCalories = 0
        for line in lines:
            if not line:
                minElfe = min(topElfes)
                maxElfe = max(topElfes)
                if minElfe <= currentTotalCalories:
                    index = topElfes.index(minElfe)
                    topElfes[index] = currentTotalCalories
                currentTotalCalories = 0
            else:
                currentTotalCalories = currentTotalCalories + int(line)
        print(f'The top three elves with the most calories have {sum(topElfes)} calories.')

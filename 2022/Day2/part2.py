# -*- coding: utf-8 -*-

INPUT_FILENAME = 'input'
INPUT_PATH = f'./{INPUT_FILENAME}'

ROCK = {
    "left": 'A',
    "right": 'X',
}

PAPER = {
    "left": 'B',
    "right": 'Y',
}

SCISSORS = {
    "left": 'C',
    "right": 'Z',
}

WIN = 'win'
LOST = 'lost'
DRAW = 'draw'

POINTS = {
    ROCK["right"]: 1,
    PAPER["right"]: 2,
    SCISSORS["right"]: 3,
    WIN: 6,
    LOST: 0,
    DRAW: 3
}

RESULTS = {
    "X": LOST,
    "Y": DRAW,
    "Z": WIN
}

RULES = {
    ROCK["left"]: {
        LOST: SCISSORS["right"],
        DRAW: ROCK["right"],
        WIN: PAPER["right"]
    },
    PAPER["left"]: {
        LOST: ROCK["right"],
        DRAW: PAPER["right"],
        WIN: SCISSORS["right"]
    },
    SCISSORS["left"]: {
        LOST: PAPER["right"],
        DRAW: SCISSORS["right"],
        WIN: ROCK["right"]
    }
}
print(RULES)

if __name__ == '__main__':
    with open(INPUT_PATH) as f:
        lines = map(lambda x: x.replace('\n', ''), f.readlines())
        scores = []
        for line in lines:
            game_result = RESULTS[line[-1]]
            selected_shape = RULES[line[0]][game_result]
            round_score = POINTS[game_result] + POINTS[selected_shape]
            scores.append(round_score)
        print(f'Total: {sum(scores)} points')

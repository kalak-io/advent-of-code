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

WIN_CASES = [f'{ROCK["left"]} {PAPER["right"]}', f'{PAPER["left"]} {SCISSORS["right"]}', f'{SCISSORS["left"]} {ROCK["right"]}']
LOST_CASES = [f'{ROCK["left"]} {SCISSORS["right"]}', f'{PAPER["left"]} {ROCK["right"]}', f'{SCISSORS["left"]} {PAPER["right"]}']

if __name__ == '__main__':
    with open(INPUT_PATH) as f:
        lines = map(lambda x: x.replace('\n', ''), f.readlines())
        scores = []
        for line in lines:
            game_result = DRAW
            if line in WIN_CASES:
                game_result = WIN
            if line in LOST_CASES:
                game_result = LOST
            round_score = POINTS[line[-1]] + POINTS[game_result]
            scores.append(round_score)
        print(f'Total: {sum(scores)} points')

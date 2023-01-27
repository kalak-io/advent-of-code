# -*- coding: utf-8 -*-
import heapq
from itertools import groupby


INPUT_FILENAME = 'input'
INPUT_PATH = f'./{INPUT_FILENAME}'
        
def elves_iterator(line_iterator):
    annotated_lines = packet_by_elf_iterator(line_iterator)
    grouped_by_elf = groupby(annotated_lines, key=lambda item: item[0])
    return (
        map(lambda calories_item: calories_item[1], calories_list)
        for _, calories_list in grouped_by_elf
    )

def get_calories_per_elf(line_iterator):
    elves_list = elves_iterator(line_iterator)
    return (
        sum(calories_list)
        for calories_list in elves_list
    )


with open("/home/christophe/Downloads/elves.txt", "r") as f:
     calories_per_elves = get_calories_per_elf(f)
     print(sum(heapq.nlargest(3, calories_per_elves)))


import functools
import re

from util import LineParser

def getData():
    return LineParser.parseLines('day_1/data.txt')

def getAllDigits(data):
    return list(map(lambda entry: re.findall('[0-9]', entry), data))

def getAllDigitsIncludingWords(data):
    keyMap = [
        ["one",     "1"],
        ["two",     "2"],
        ["three",   "3"],
        ["four",    "4"],
        ["five",    "5"],
        ["six",     "6"],
        ["seven",   "7"],
        ["eight",   "8"],
        ["ight",    "8"],
        ["nine",    "9"],
        ["ine",     "9"],
        ["ne",      "1"],
        ["hree",    "3"],
        ["wo",      "2"],
    ]

    matchString = "[0-9]|zero|one|two|three|four|five|six|seven|eight|nine|(?<=o)ne|(?<=e)ight|(?<=n)ine|(?<=t)hree|(?<=t)wo"

    return functools.reduce(
        lambda acc, key: list(map( # for each key in the keymap
            lambda words: list(map( # for each word in a line
                lambda word: re.sub(key[0], key[1], word), words) # replace each matched word matching the key corresponding number
            ), acc)),
        keyMap,
        list(map( lambda entry: re.findall(matchString, entry), data)))

def getAllNumbersToAdd(digits):
    return list( map( lambda numbers: int(numbers[0])*10 + int(numbers[-1]), digits ) )

def part_one():
    return sum( getAllNumbersToAdd( getAllDigits( getData() ) ) )

def part_two():
    return sum ( getAllNumbersToAdd ( getAllDigitsIncludingWords ( getData() ) ) ) 

print("part one: ", part_one())
print("part two: ", part_two())
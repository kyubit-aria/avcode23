import functools
import re

from util import LineParser
from util import TextSplit

def getData():
    return LineParser.parseLines('day_2/data.txt')

# for a specific color return the amount of it within an episode of a play
def getValueOfColor(episode, color): 
    for move in episode:
        if color in move:
            return int(move.split(' ')[0])
    return 0

def parseGame(line):
    gameId, play = line.split(':')
    return {
        'game': int(gameId.split(' ')[1]), # extract game id number
        'play': list(map(lambda episode: { # get cube counts for each draw in a game
            'red'   :   getValueOfColor(episode, 'red'),
            'green' :   getValueOfColor(episode, 'green'),
            'blue'  :   getValueOfColor(episode, 'blue')
            }, TextSplit.subsplit(play.split(';'), ', ')))
        }

def filterValid(game): # Returns true if a game is valid
    return all(list(map(lambda episode: episode['red'] <= 12\
            and episode['green'] <= 13\
            and episode['blue'] <= 14, game['play'])))

# for the set of plays in a game, calculate what the minimum combination of cubes is
def reduceToMax(game): 
    return functools.reduce(
        lambda acc, val: {
            'red'   : max(acc['red'], val['red']),
            'green' : max(acc['green'], val['green']),
            'blue'  : max(acc['blue'], val['blue'])
        }, game, game[0])

def part_one(): # Filter all invalid games out of the list and then sum the id's
    return sum(list(map(lambda game: game['game'],
        list(filter(filterValid, list(map(lambda game: parseGame(game), getData()))))
    )))

def part_two(): # For each game calculate the cube combinations, multiply and then sum the result
    return sum(list(map( lambda values: values['red']  * values['green']  * values['blue'], 
        list(map(lambda parsedGame: reduceToMax(parsedGame['play']), 
            list(map(lambda game: parseGame(game), getData()))
        ))
    )))

print(part_one())
print(part_two())
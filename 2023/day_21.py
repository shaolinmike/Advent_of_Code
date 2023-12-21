#! python3.11
"""
--- Day 21: Step Counter ---
You manage to catch the airship right as it's dropping someone else off on
their all-expenses-paid trip to Desert Island! It even helpfully drops you
off near the gardener and his massive farm.

"You got the sand flowing again! Great work! Now we just need to wait until
we have enough sand to filter the water for Snow Island and we'll have snow
again in no time."

While you wait, one of the Elves that works with the gardener heard how
good you are at solving problems and would like your help. He needs to get
his steps in for the day, and so he'd like to know which garden plots he
can reach with exactly his remaining 64 steps.

He gives you an up-to-date map (your puzzle input) of his starting position
(S), garden plots (.), and rocks (#). For example:

...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........

The Elf starts at the starting position (S) which also counts as a garden
plot. Then, he can take one step north, south, east, or west, but only onto
tiles that are garden plots. This would allow him to reach any of the tiles
marked O:

...........
.....###.#.
.###.##..#.
..#.#...#..
....#O#....
.##.OS####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........

Then, he takes a second step. Since at this point he could be at either
tile marked O, his second step would allow him to reach any garden plot
that is one step north, south, east, or west of any tile that he could have
reached after the first step:

...........
.....###.#.
.###.##..#.
..#.#O..#..
....#.#....
.##O.O####.
.##.O#...#.
.......##..
.##.#.####.
.##..##.##.
...........

After two steps, he could be at any of the tiles marked O above, including
the starting position (either by going north-then-south or by going west-
then-east).

A single third step leads to even more possibilities:

...........
.....###.#.
.###.##..#.
..#.#.O.#..
...O#O#....
.##.OS####.
.##O.#...#.
....O..##..
.##.#.####.
.##..##.##.
...........

He will continue like this until his steps for the day have been exhausted.
After a total of 6 steps, he could reach any of the garden plots marked O:

...........
.....###.#.
.###.##.O#.
.O#O#O.O#..
O.O.#.#.O..
.##O.O####.
.##.O#O..#.
.O.O.O.##..
.##.#.####.
.##O.##.##.
...........

In this example, if the Elf's goal was to get exactly 6 more steps today,
he could use them to reach any of 16 garden plots.

However, the Elf actually needs to get 64 steps today, and the map he's
handed you is much larger than the example map.

Starting from the garden plot marked S on your map, how many garden plots
could the Elf reach in exactly 64 steps?

Your puzzle answer was 3814.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
The Elf seems confused by your answer until he realizes his mistake: he was
reading from a list of his favorite numbers that are both perfect squares
and perfect cubes, not his step counter.

The actual number of steps he needs to get today is exactly 26501365.

He also points out that the garden plots and rocks are set up so that the
map repeats infinitely in every direction.

So, if you were to look one additional map-width or map-height out from the
edge of the example map above, you would find that it keeps repeating:

.................................
.....###.#......###.#......###.#.
.###.##..#..###.##..#..###.##..#.
..#.#...#....#.#...#....#.#...#..
....#.#........#.#........#.#....
.##...####..##...####..##...####.
.##..#...#..##..#...#..##..#...#.
.......##.........##.........##..
.##.#.####..##.#.####..##.#.####.
.##..##.##..##..##.##..##..##.##.
.................................
.................................
.....###.#......###.#......###.#.
.###.##..#..###.##..#..###.##..#.
..#.#...#....#.#...#....#.#...#..
....#.#........#.#........#.#....
.##...####..##..S####..##...####.
.##..#...#..##..#...#..##..#...#.
.......##.........##.........##..
.##.#.####..##.#.####..##.#.####.
.##..##.##..##..##.##..##..##.##.
.................................
.................................
.....###.#......###.#......###.#.
.###.##..#..###.##..#..###.##..#.
..#.#...#....#.#...#....#.#...#..
....#.#........#.#........#.#....
.##...####..##...####..##...####.
.##..#...#..##..#...#..##..#...#.
.......##.........##.........##..
.##.#.####..##.#.####..##.#.####.
.##..##.##..##..##.##..##..##.##.
.................................

This is just a tiny three-map-by-three-map slice of the inexplicably-
infinite farm layout; garden plots and rocks repeat as far as you can see.
The Elf still starts on the one middle tile marked S, though - every other
repeated S is replaced with a normal garden plot (.).

Here are the number of reachable garden plots in this new infinite version
of the example map for different numbers of steps:

In exactly 6 steps, he can still reach 16 garden plots.
In exactly 10 steps, he can reach any of 50 garden plots.
In exactly 50 steps, he can reach 1594 garden plots.
In exactly 100 steps, he can reach 6536 garden plots.
In exactly 500 steps, he can reach 167004 garden plots.
In exactly 1000 steps, he can reach 668697 garden plots.
In exactly 5000 steps, he can reach 16733044 garden plots.

However, the step count the Elf needs is much larger! Starting from the
garden plot marked S on your infinite map, how many garden plots could the
Elf reach in exactly 26501365 steps?


"""

import copy
import heapq

from collections import deque

TEST_DATA = [ '...........',
              '.....###.#.',
              '.###.##..#.',
              '..#.#...#..',
              '....#.#....',
              '.##..S####.',
              '.##..#...#.',
              '.......##..',
              '.##.#.####.',
              '.##..##.##.',
              '...........'
            ]

DEBUG = True


class Plot_Object():

    def __init__(self, id, x, y, is_valid=False):
        self.id = id
        self.x = x
        self.y = y
        self.steps = 0
        self.is_valid = is_valid

    def __repr__(self):
        return f"<{self.__class__.__name__}({self.x}, {self.y}) {self.id}>"

    def __str__(self):
        return f'{str(self.id)}'



def _print(obj, render_mode = False):
    if render_mode:
        results = []

        for datum in obj:
            if datum.is_valid:
                results.append('O')
            else:
                results.append(datum.id)

        print(''.join(results))

    else:
        print(''.join(map(str, obj)))


def get_neighbors(data, x, y):
    all_neighbors = deque([])

    row_height = len(data[0])
    col_length = len(data)

    # Up
    if 0 <= x < col_length and 0 <= y - 1 < row_height:
        all_neighbors.append(data[y - 1][x])

    # Right
    if 0 <= x + 1 < col_length and 0 <= y< row_height:
        all_neighbors.append(data[y][x + 1])

    # Down
    if 0 <= x < col_length and 0 <= y + 1< row_height:
        all_neighbors.append(data[y + 1][x])

    # Left
    if 0 <= x - 1< col_length and 0 <= y < row_height:
        all_neighbors.append(data[y][x - 1])

    # Return only valid neighbors that haven't already been identified as valid
    return [x for x in all_neighbors if x.id != '#']

def _calculate_path(data, current_node, steps, total_steps):
    current_steps = steps
    results = []

    if current_steps == total_steps:
        current_node.is_valid = True
        return [current_node]

    else:
        current_steps += 1

        all_neighbors = get_neighbors(data, current_node.x, current_node.y)
        neighbors = []
        for neighbor in all_neighbors:
            if neighbor.steps == 0 or neighbor.steps > current_steps:
                neighbor.steps == current_steps
                neighbors.append(neighbor)
            else:
                if neighbor.is_valid == False:
                    neighbors.append(neighbor)

        for neighbor in neighbors:
            neighbor.steps = current_steps
            sub_results = _calculate_path(data, neighbor, current_steps, total_steps)
            results.extend(sub_results)

    return results


def calculate_path(data, unknown_node_list, total_steps, x=0, y=0):
    results = []

    current_node = data[y][x]
    results = _calculate_path(data, current_node, 0, total_steps)

    return results


def parse_data(raw_data):
    data = []
    nodes = []
    origin = None

    for row_idx, row in enumerate(raw_data):
        datum = []
        for col_idx, item in enumerate(row):
            map_obj = Plot_Object(item, col_idx, row_idx)
            datum.append(map_obj)
            nodes.append(map_obj)
        data.append(datum)

    origin = [x for datum in data for x in datum if x.id == 'S'][0]

    return data, nodes, (origin.x, origin.y)


def main(raw_data, total_steps, part_two = False):
    data, nodes, origin = parse_data(raw_data)
    total_paths = calculate_path(data, nodes, total_steps, origin[0], origin[1])

    if not part_two:
        print(f'\n{len(list(set(total_paths)))} garden plots can be reached in exactly {total_steps} steps')
    else:
        print(f'\n{len(list(set(total_paths)))} garden plots can be reached in exactly {total_steps} steps')



if __name__ == "__main__":
    input = r"D:\Projects\Advent_of_Code\2023\day_21_input.txt"
    raw_data = []

    with open(input, "r") as input_file:
        raw_data = [line.rstrip() for line in input_file.readlines( )]

    # main(TEST_DATA, 6)
    main(raw_data, 64)
    # main(TEST_DATA, 6, part_two = True)
    # main(raw_data,  part_two = True)
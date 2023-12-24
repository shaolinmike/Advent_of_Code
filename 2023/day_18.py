#! python3.11
"""
--- Day 18: Lavaduct Lagoon ---
Thanks to your efforts, the machine parts factory is one of the first
factories up and running since the lavafall came back. However, to catch up
with the large backlog of parts requests, the factory will also need a
large supply of lava for a while; the Elves have already started creating a
large lagoon nearby for this purpose.

However, they aren't sure the lagoon will be big enough; they've asked you
to take a look at the dig plan (your puzzle input). For example:

R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)

The digger starts in a 1 meter cube hole in the ground. They then dig the
specified number of meters up (U), down (D), left (L), or right (R),
clearing full 1 meter cubes as they go. The directions are given as seen
from above, so if "up" were north, then "right" would be east, and so on.
Each trench is also listed with the color that the edge of the trench
should be painted as an RGB hexadecimal color code.

When viewed from above, the above example dig plan would result in the
following loop of trench (#) having been dug out from otherwise ground-
level terrain (.):

#######
#.....#
###...#
..#...#
..#...#
###.###
#...#..
##..###
.#....#
.######

At this point, the trench could contain 38 cubic meters of lava. However,
this is just the edge of the lagoon; the next step is to dig out the
interior so that it is one meter deep as well:

#######
#######
#######
..#####
..#####
#######
#####..
#######
.######
.######

Now, the lagoon can contain a much more respectable 62 cubic meters of
lava. While the interior is dug out, the edges are also painted according
to the color codes in the dig plan.

The Elves are concerned the lagoon won't be large enough; if they follow
their dig plan, how many cubic meters of lava could it hold?

Your puzzle answer was 72821.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
The Elves were right to be concerned; the planned lagoon would be much too
small.

After a few minutes, someone realizes what happened; someone swapped the
color and instruction parameters when producing the dig plan. They don't
have time to fix the bug; one of them asks if you can extract the correct
instructions from the hexadecimal codes.

Each hexadecimal code is six hexadecimal digits long. The first five
hexadecimal digits encode the distance in meters as a five-digit
hexadecimal number. The last hexadecimal digit encodes the direction to
dig: 0 means R, 1 means D, 2 means L, and 3 means U.

So, in the above example, the hexadecimal codes can be converted into the
true instructions:

#70c710 = R 461937
#0dc571 = D 56407
#5713f0 = R 356671
#d2c081 = D 863240
#59c680 = R 367720
#411b91 = D 266681
#8ceee2 = L 577262
#caa173 = U 829975
#1b58a2 = L 112010
#caa171 = D 829975
#7807d2 = L 491645
#a77fa3 = U 686074
#015232 = L 5411
#7a21e3 = U 500254

Digging out this loop and its interior produces a lagoon that can hold an
impressive 952408144115 cubic meters of lava.

Convert the hexadecimal color codes into the correct instructions; if the
Elves follow this new dig plan, how many cubic meters of lava could the
lagoon hold?

Your puzzle answer was 127844509405501.

Both parts of this puzzle are complete! They provide two gold stars: **


"""

import itertools
import numpy

TEST_DATA = [ 'R 6 (#70c710)',
              'D 5 (#0dc571)',
              'L 2 (#5713f0)',
              'D 2 (#d2c081)',
              'R 2 (#59c680)',
              'D 2 (#411b91)',
              'L 5 (#8ceee2)',
              'U 2 (#caa173)',
              'L 1 (#1b58a2)',
              'U 2 (#caa171)',
              'R 2 (#7807d2)',
              'U 3 (#a77fa3)',
              'L 2 (#015232)',
              'U 2 (#7a21e3)'
              ]

DEBUG = True

class Point():

    def __init__(self, id , x = -1, y = -1, color='0'):
        self.id = id
        self.x = x
        self.y = y
        self.color = color

    def __repr__(self):
        return f"<{self.__class__.__name__}_{self.x}_{self.y} ({self.color})>"

    @property
    def get_rgb(self):
        return int(self.color, 16)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)

    def __gt__(self, other):
        return (self.x, self.y) > (other.x, other.y)


def _print(obj, render_mode = False):
    if render_mode:
        results = []

        for datum in obj:
            results.append(datum.id)

        print(''.join(results))

    else:
        print(''.join(map(str, obj)))


def _initialize_ground(grid_size):
    ground = []
    x = 0
    y = 0

    for y in range(0, grid_size[1]):
        row = []
        for x in range(0, grid_size[0]):
            new_point = Point('.', x, y)
            row.append(new_point)
        ground.append(row)

    return ground


def calculate_area(ground, boundary_coords, part_two = False):
    outer_points = 0
    result = 0
    x_positions = numpy.array(boundary_coords[0], dtype=numpy.int64)
    y_positions = numpy.array(boundary_coords[1], dtype=numpy.int64)

    if part_two:
        outer_points = ground
    else:
        outer_points = len([x for row in ground for x in row if x.id == '#'])

    interior_area = 0.5*numpy.abs(numpy.dot(x_positions,numpy.roll(y_positions,1))-numpy.dot(y_positions,numpy.roll(x_positions,1)))
    result = int((interior_area - outer_points/2 + 1) + outer_points)

    return result


def process_instructions(data, grid_size, offset_pos, part_two = False):
    boundary_x = []
    boundary_y = []
    ground = None

    x = offset_pos[0]
    y = offset_pos[1]

    if not part_two:
        ground = _initialize_ground(grid_size)
        for instruction in data:
            if instruction[0]== 'U':
                for i in range(y - 1, y - int(instruction[1]) - 1, -1):
                    ground[i][x].id = '#'
                    ground[i][x].color = instruction[2]
                    boundary_x.append(x)
                    boundary_y.append(i)
                    y = i
                # if DEBUG: [_print(x, render_mode = True) for x in ground]

            elif instruction[0]== 'R':
                for i in range(x + 1, x + int(instruction[1]) + 1):
                    ground[y][i].id = '#'
                    ground[y][i].color = instruction[2]
                    boundary_x.append(i)
                    boundary_y.append(y)
                    x = i
                # if DEBUG: [_print(x, render_mode = True) for x in ground]

            elif instruction[0]== 'D':
                for i in range(y + 1, y + int(instruction[1]) + 1):
                    ground[i][x].id = '#'
                    ground[i][x].color = instruction[2]
                    boundary_x.append(x)
                    boundary_y.append(i)
                    y = i
                # if DEBUG: [_print(x, render_mode = True) for x in ground]

            else: # 'L' by process of elimination
                for i in range(x - 1, x - int(instruction[1]) - 1, -1):
                    ground[y][i].id = '#'
                    ground[y][i].color = instruction[2]
                    boundary_x.append(i)
                    boundary_y.append(y)
                    x = i
                # if DEBUG: [_print(x, render_mode = True) for x in ground]
    else:
        dig_verts= 0
        for instruction in data:
            dig_verts += int(instruction[1])
            if instruction[0]== 'U':
                y -= int(instruction[1])
                boundary_x.append(x)
                boundary_y.append(y)

            elif instruction[0]== 'R':
                x += int(instruction[1])
                boundary_x.append(x)
                boundary_y.append(y)

            elif instruction[0]== 'D':
                y += int(instruction[1])
                boundary_x.append(x)
                boundary_y.append(y)

            else: # 'L' by process of elimination
                x -= int(instruction[1])
                boundary_x.append(x)
                boundary_y.append(y)

        ground = dig_verts
        boundary_x = [x for x in reversed(boundary_x)]
        boundary_y = [x for x in reversed(boundary_y)]

    return ground, (boundary_x, boundary_y)


def parse_data(raw_data, part_two = False):
    data = []
    x = 0
    y = 0

    # Graph table
    max_x = 0
    max_y = 0
    min_x = 0
    min_y = 0
    padding = 2

    if part_two:
        for datum in raw_data:
            direction = ''

            result = datum.rstrip(')').split('#')[-1]

            if int(result[-1]) == 0:
                direction = 'R'

            elif int(result[-1]) == 1:
                direction = 'D'

            elif int(result[-1]) == 2:
                direction = 'L'

            else: # 'U' by process of elimination
                direction = 'U'

            new_datum = [direction, int(result[:-1], 16), datum.split()[2]]
            data.append(new_datum)

    else:
        for datum in raw_data:
            data.append(datum.split())

    for datum in data:
        if datum[0]== 'U':
            y -= int(datum[1])
            min_y = min([min_y, y])

        elif datum[0]== 'R':
            x += int(datum[1])
            max_x = max([max_x, x])

        elif datum[0]== 'D':
            y += int(datum[1])
            max_y = max([max_y, y])

        else: # 'L' by process of elimination
            x -= int(datum[1])
            min_x = min([min_x, x])

    # Add 1 to convert this a base-0 number
    grid_size = (max_x - min_x + 1 + padding,max_y - min_y + 1 + padding)# 388, 582
    offset_pos = (-min_x + 1, -min_y + 1)

    return data, grid_size, offset_pos


def main(raw_data, part_two = False):
    data, grid_size, offset_pos = parse_data(raw_data, part_two)
    ground, boundary_coords = process_instructions(data, grid_size, offset_pos, part_two)
    result = calculate_area(ground, boundary_coords, part_two)

    print(f'\nThe trench can hold {result} cubic meters of lava')



if __name__ == "__main__":
    filename = __file__.split('\\')[-1].split('.')[0]
    input = rf"D:\Projects\Advent_of_Code\2023\{filename}_input.txt"
    raw_data = []

    with open(input, "r") as input_file:
        raw_data = [line.rstrip() for line in input_file.readlines( )]

    # main(TEST_DATA)
    # main(raw_data)
    # main(TEST_DATA, part_two = True)
    main(raw_data, part_two = True)

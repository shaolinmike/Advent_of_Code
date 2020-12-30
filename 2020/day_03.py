'''
--- Day 3: Toboggan Trajectory ---

With the toboggan login problems resolved, you set off toward the airport. While travel by toboggan might be easy, it's certainly not safe: there's very minimal steering and the area is covered in trees. You'll need to see which angles will take you near the fewest trees.

Due to the local geology, trees in this area only grow on exact integer coordinates in a grid. You make a map (your puzzle input) of the open squares (.) and trees (#) you can see. For example:

..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#

These aren't the only trees, though; due to something you read about once involving arboreal genetics and biome stability, the same pattern repeats to the right many times:

..##.........##.........##.........##.........##.........##.......  --->
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).

The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start by counting all the trees you would encounter for the slope right 3, down 1:

From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

The locations you'd check in the above example are marked here with O where there was an open square and X where there was a tree:

..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

In this example, traversing the map using this slope would cause you to encounter 7 trees.

Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?

Your puzzle answer was 284.

--- Part Two ---

Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

	Right 1, down 1.
	Right 3, down 1. (This is the slope you already checked.)
	Right 5, down 1.
	Right 7, down 1.
	Right 1, down 2.

In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?

Your puzzle answer was 3510149120.

Both parts of this puzzle are complete! They provide two gold stars: **
'''

MOVE_PATTERN_ALPHA = ( 3, 1 )
MOVE_PATTERN_ONE = ( 1, 1 )
MOVE_PATTERN_TWO = ( 5, 1 )
MOVE_PATTERN_TWO_TURBO = ( 7, 1 )
MOVE_PATTERN_TWO_TURBO_HYPER = ( 1, 2 )


def get_new_position( x, y, move_pattern ):
	new_x = move_pattern[ 0 ] + x
	new_y = move_pattern[ 1 ] + y

	if new_x >= DATA_WIDTH:
		new_x -= DATA_WIDTH

	return new_x, new_y


def check_for_trees( data, move_pattern ):
	current_x = 0
	encountered_trees = 0

	for y in range( 0, DATA_HEIGHT, move_pattern[ 1 ] ):
		if y < DATA_HEIGHT:
			new_x, new_y = get_new_position( current_x, y, move_pattern )

			if new_y <= DATA_HEIGHT:
				if data[ new_y ][ new_x ] == '#':
					encountered_trees += 1

			current_x = new_x

	return encountered_trees


def main( data ):
	trees_1 = check_for_trees( data, MOVE_PATTERN_ALPHA )
	trees_2 = check_for_trees( data, MOVE_PATTERN_ONE )
	trees_3 = check_for_trees( data, MOVE_PATTERN_TWO )
	trees_4 = check_for_trees( data, MOVE_PATTERN_TWO_TURBO )
	trees_5 = check_for_trees( data, MOVE_PATTERN_TWO_TURBO_HYPER )

	result_2 = trees_1 * trees_2 * trees_3 * trees_4 * trees_5

	print( '\nRun 1:\n\tTrees encountered: {0}'.format( trees_1 ) )
	print( '\nRun 2:\n\tTrees encountered: {0}'.format( result_2 ) )



if __name__ == "__main__":
	input = r'D:\Projects\Python\Personal\Advent_of_Code\2020\day_03_input.txt'
	# input = r'D:\Dropbox\Projects\Python\Advent_of_Code\2020\day_03_input.txt'

	raw_data = [ ]

	with open( input, 'r' ) as input_file:
		raw_data = [ line.strip( ) for line in input_file.readlines( ) ]

	DATA_WIDTH = len( raw_data[ 0 ] )
	DATA_HEIGHT = len( raw_data ) - 1

	main( raw_data )

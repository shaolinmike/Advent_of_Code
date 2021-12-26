'''
--- Day 5: Hydrothermal Venture ---

You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.

They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you to review. For example:

0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2

Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:

    An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
    An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.

For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

So, the horizontal and vertical lines from the above list would produce the following diagram:

.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....

In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

Consider only horizontal and vertical lines. At how many points do at least two lines overlap?

Your puzzle answer was 6005.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.

Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

    An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
    An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.

Considering all lines from the above example would now produce the following diagram:

1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....

You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.

Consider all of the lines. At how many points do at least two lines overlap?

'''

from collections import deque

test_data = [ '0,9 -> 5,9', '8,0 -> 0,8', '9,4 -> 3,4', '2,2 -> 2,1', '7,0 -> 7,4', '6,4 -> 2,0', '0,9 -> 2,9', '3,4 -> 1,4', '0,0 -> 8,8', '5,5 -> 8,2' ]


def draw( grid ):
	for i in range( 0, len( grid ) ):
		print( grid[ i ] )
	print( '' )


def parse_data( data ):
	grid = [ ]
	grid_size = 1000
	num_crossings = [ ]

	# Initialize the grid
	for row in range( 0, grid_size ):
		row = [ ]
		for col in range( 0, grid_size ):
			row.append( 0 )
		grid.append( row )

	x1 = 0
	x2 = 0
	y1 = 0
	y2 = 0
	nums = [ ]

	for datum in data:
		end_points = datum.split( ' -> ' )
		points = sorted( [ list( map( int, x.split( ',' ) ) ) for x in end_points ] )
		x1 = points[ 0 ][ 0 ]
		x2 = points[ 1 ][ 0 ]

		y1 = points[ 0 ][ 1 ]
		y2 = points[ 1 ][ 1 ]

		if x1 == x2:
			for y in range( y1, y2 + 1 ):
				grid[ y ][ x1 ] += 1

		elif y1 == y2:
			for x in range( x1, x2 + 1 ):
				grid[ y1 ][ x ] += 1

		else:
			pass

		# draw( grid )

	for row in range( 0, len( grid ) ):
		num_crossings += [ x for x in grid[ row ] if x > 1 ]

	print( 'The number of crossings is: {0}'.format( len( num_crossings ) ) )


def main( data ):
	parse_data( data )


if __name__ == "__main__":
	input = r'D:\Projects\Advent_of_Code\2021\day_05_input.txt'

	raw_data = [ ]

	with open( input, 'r' ) as input_file:
		raw_data = [ x.strip( ) for x in input_file.readlines( ) ]

	main( raw_data )

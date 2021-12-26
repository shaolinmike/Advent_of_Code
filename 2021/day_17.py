'''
--- Day 17: Trick Shot ---

You finally decode the Elves' message. HI, the message says. You continue searching for the sleigh keys.

Ahead of you is what appears to be a large ocean trench. Could the keys have fallen into it? You'd better send a probe to investigate.

The probe launcher on your submarine can fire the probe with any integer velocity in the x (forward) and y (upward, or downward if negative) directions. For example, an initial x,y velocity like 0,10 would fire the probe straight up, while an initial velocity like 10,-1 would fire the probe forward at a slight downward angle.

The probe's x,y position starts at 0,0. Then, it will follow some trajectory by moving in steps. On each step, these changes occur in the following order:

    The probe's x position increases by its x velocity.
    The probe's y position increases by its y velocity.
    Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1 if it is greater than 0, increases by 1 if it is less than 0, or does not change if it is already 0.
    Due to gravity, the probe's y velocity decreases by 1.

For the probe to successfully make it into the trench, the probe must be on some trajectory that causes it to be within a target area after any step. The submarine computer has already calculated this target area (your puzzle input). For example:

target area: x=20..30, y=-10..-5

This target area means that you need to find initial x,y velocity values such that after any step, the probe's x position is at least 20 and at most 30, and the probe's y position is at least -10 and at most -5.

Given this target area, one initial velocity that causes the probe to be within the target area after any step is 7,2:

.............#....#............
.......#..............#........
...............................
S........................#.....
...............................
...............................
...........................#...
...............................
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTT#TT
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTTTTT

In this diagram, S is the probe's initial position, 0,0. The x coordinate increases to the right, and the y coordinate increases upward. In the bottom right, positions that are within the target area are shown as T. After each step (until the target area is reached), the position of the probe is marked with #. (The bottom-right # is both a position the probe reaches and a position in the target area.)

Another initial velocity that causes the probe to be within the target area after any step is 6,3:

...............#..#............
...........#........#..........
...............................
......#..............#.........
...............................
...............................
S....................#.........
...............................
...............................
...............................
.....................#.........
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................T#TTTTTTTTT
....................TTTTTTTTTTT

Another one is 9,0:

S........#.....................
.................#.............
...............................
........................#......
...............................
....................TTTTTTTTTTT
....................TTTTTTTTTT#
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTTTTT

One initial velocity that doesn't cause the probe to be within the target area after any step is 17,-4:

S..............................................................
...............................................................
...............................................................
...............................................................
.................#.............................................
....................TTTTTTTTTTT................................
....................TTTTTTTTTTT................................
....................TTTTTTTTTTT................................
....................TTTTTTTTTTT................................
....................TTTTTTTTTTT..#.............................
....................TTTTTTTTTTT................................
...............................................................
...............................................................
...............................................................
...............................................................
................................................#..............
...............................................................
...............................................................
...............................................................
...............................................................
...............................................................
...............................................................
..............................................................#

The probe appears to pass through the target area, but is never within it after any step. Instead, it continues down and to the right - only the first few steps are shown.

If you're going to fire a highly scientific probe out of a super cool probe launcher, you might as well do it with style. How high can you make the probe go while still reaching the target area?

In the above example, using an initial velocity of 6,9 is the best you can do, causing the probe to reach a maximum y position of 45. (Any higher initial y velocity causes the probe to overshoot the target area entirely.)

Find the initial velocity that causes the probe to reach the highest y position and still eventually be within the target area after any step. What is the highest y position it reaches on this trajectory?

Your puzzle answer was 10296.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

Maybe a fancy trick shot isn't the best idea; after all, you only have one probe, so you had better not miss.

To get the best idea of what your options are for launching the probe, you need to find every initial velocity that causes the probe to eventually be within the target area after any step.

In the above example, there are 112 different initial velocity values that meet these criteria:

23,-10  25,-9   27,-5   29,-6   22,-6   21,-7   9,0     27,-7   24,-5
25,-7   26,-6   25,-5   6,8     11,-2   20,-5   29,-10  6,3     28,-7
8,0     30,-6   29,-8   20,-10  6,7     6,4     6,1     14,-4   21,-6
26,-10  7,-1    7,7     8,-1    21,-9   6,2     20,-7   30,-10  14,-3
20,-8   13,-2   7,3     28,-8   29,-9   15,-3   22,-5   26,-8   25,-8
25,-6   15,-4   9,-2    15,-2   12,-2   28,-9   12,-3   24,-6   23,-7
25,-10  7,8     11,-3   26,-7   7,1     23,-9   6,0     22,-10  27,-6
8,1     22,-8   13,-4   7,6     28,-6   11,-4   12,-4   26,-9   7,4
24,-10  23,-8   30,-8   7,0     9,-1    10,-1   26,-5   22,-9   6,5
7,5     23,-6   28,-10  10,-2   11,-1   20,-9   14,-2   29,-7   13,-3
23,-5   24,-8   27,-9   30,-7   28,-5   21,-10  7,9     6,6     21,-5
27,-10  7,2     30,-9   21,-8   22,-7   24,-9   20,-6   6,9     29,-5
8,-2    27,-8   30,-5   24,-7

How many distinct initial velocity values cause the probe to be within the
target area after any step?
'''

import math

test_data_1 = 'target area: x=20..30, y=-10..-5'

def calculate_distance( velocity_initial, acceleration, time_range ):
	# return( velocity_initial * time + ( acceleration * time ** 2 / 2 ) )
	distance = 0
	if time_range:
		for time in range( 0, time_range ):
			distance += velocity_initial + acceleration * time
			print

	return distance


def calculate_time( velocity_initial, velocity_final, acceleration ):
	return int( (velocity_final - velocity_initial ) / acceleration )


def calculate_initial_velocity( velocity_final, acceleration, distance ):
	# Vf**2 = Vi**2 + 2a * distance
	# velocity_initial = math.sqrt( velocity_final ** 2 - ( 2 * acceleration * distance ) )

	# return velocity_initial

	while distance > 0:
		distance -= velocity_final
		velocity_final -= acceleration

	if distance == 0:
		return velocity_final - 1

	return -1



def calculate_initial_velocity_y( acceleration,  time, delta_y ):
	# velocity_initial_y = delta_y / time - ( acceleration * time / 2 )
	velocity_initial_y = int( delta_y / time )

	return velocity_initial_y


def calculate_final_velocity_y( velocity_initial, acceleration, distance ):
	velocity_final_y = math.sqrt( velocity_initial ** 2 + 2 * acceleration * distance )
	return velocity_final_y


def verify_solution( x, y, acceleration, x_range, y_range, time_range ):
	current_x = x
	current_y = y

	print( 'Initial Velocity: {0},{1}'.format( x, y ) )
	for i in range( time_range[ 0 ], time_range[ 0 ] + 1 ):
		print( 'Time: {0}\n\t\tX: {1}\tY:{2}'.format( i, current_x, current_y ) )
		current_x += acceleration
		current_y += acceleration


def parse_data( data_string ):
	data = [ ]
	raw_data_string = ''

	data = [ tuple( map( int, x.split( '..' ) ) ) for x in data_string.strip( 'target area: x=').split( ', y='  ) ]

	return data


def calculate_optimal_trajectory( data ):
	a = -1

	trench_x_pos_initial = data[ 0 ][ 0 ]
	trench_x_pos_final = data[ 0 ][ 1 ]
	trench_y_pos_initial = data[ 1 ][ 0 ]
	trench_y_pos_final = data[ 1 ][ 1 ]

	possible_Vxi = [ ]
	possible_Vyi = [ ]

	Vxf = 0
	Vyf = 0

	for pos_x in range( trench_x_pos_initial, trench_x_pos_final + 1 ):
		Vxi = calculate_initial_velocity( Vxf, a, pos_x )
		if Vxi > 0:
			time = calculate_time( Vxi, Vxf, a )
			if calculate_distance( Vxi, a, time ) in range( trench_x_pos_initial, trench_x_pos_final ):
				possible_Vxi.append( ( Vxi, time ) )

	possible_times = list( set( [ math.trunc( x[ 1 ] ) for x in possible_Vxi ] ) )

	for time in range( possible_times[ 0 ], possible_times[ 1 ] ):
		distance_final = calculate_distance( int( time / 2 ), a, int( time / 2 ) ) + calculate_distance( 0, a, time )
		print( '\t\tY = {0} @ {1}s'.format( distance_final, time ) )
		print( '\nFinal distance: {0} @ {1}s\n'.format( distance_final, time ) )

		if distance_final in range( trench_y_pos_initial, trench_y_pos_final + 1 ):
			possible_Vyi.append( ( time, int( time / 2 + time ) ) )

	possible_velocities = list( set( possible_Vyi ) )

	print( 'Possible times: {0}'.format( possible_times ) )
	print( 'Possible velocities: {0}'.format( possible_velocities ) )

	depth_range = range( trench_y_pos_initial, trench_y_pos_final + 1 )

	for t in possible_times:
		print( 'Time: {0}'.format( t ) )
		verify_solution( 0, 0, a, ( trench_x_pos_initial, trench_x_pos_final ), ( trench_y_pos_initial, trench_y_pos_final ), ( 0, t ) )
	# print( 'The optimal trajectory is: {0}, {1}'.format( optimal_solution[ 0 ], optimal_solution[ 1 ] ) )


def main( data ):
	data = parse_data( data )
	angle_vector = calculate_optimal_trajectory( data )



if __name__ == "__main__":
	input = r'D:\Projects\Advent_of_Code\2021\day_17_input.txt'

	raw_data = [ ]

	with open( input, 'r' ) as input_file:
		raw_data_string = input_file.read( ).strip( )

	# main( test_data_1 )
	# main( raw_data_string )
	current_x = 15
	current_y = 98
	dist_x = 0
	dist_y = 0
	print( 'Initial Velocity: {0},{1}'.format( current_x, current_y ) )
	for i in range( 0, 200 ):
		dist_x += current_x
		dist_y += current_y
		print( 'Time: {0}\n\t\tX: {1} ( {2} )\n\t\tY: {3} ( {4} )'.format( i, current_x, dist_x, current_y, dist_y ) )
		current_x += -1
		current_y += -1


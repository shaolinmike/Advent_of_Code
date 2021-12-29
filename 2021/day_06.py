'''
--- Day 6: Lanternfish ---

The sea floor is getting steeper. Maybe the sleigh keys got carried this way?

A massive school of glowing lanternfish swims past. They must spawn quickly to reach such large numbers - maybe exponentially quickly? You should model their growth rate to be sure.

Although you know nothing about this specific species of lanternfish, you make some guesses about their attributes. Surely, each lanternfish creates a new lanternfish once every 7 days.

However, this process isn't necessarily synchronized between every lanternfish - one lanternfish might have 2 days left until it creates another lanternfish, while another might have 4. So, you can model each fish as a single number that represents the number of days until it creates a new lanternfish.

Furthermore, you reason, a new lanternfish would surely need slightly longer before it's capable of producing more lanternfish: two more days for its first cycle.

So, suppose you have a lanternfish with an internal timer value of 3:

    After one day, its internal timer would become 2.
    After another day, its internal timer would become 1.
    After another day, its internal timer would become 0.
    After another day, its internal timer would reset to 6, and it would create a new lanternfish with an internal timer of 8.
    After another day, the first lanternfish would have an internal timer of 5, and the second lanternfish would have an internal timer of 7.

A lanternfish that creates a new fish resets its timer to 6, not 7 (because 0 is included as a valid timer value). The new lanternfish starts with an internal timer of 8 and does not start counting down until the next day.

Realizing what you're trying to do, the submarine automatically produces a list of the ages of several hundred nearby lanternfish (your puzzle input). For example, suppose you were given the following list:

3,4,3,1,2

This list means that the first fish has an internal timer of 3, the second fish has an internal timer of 4, and so on until the fifth fish, which has an internal timer of 2. Simulating these fish over several days would proceed as follows:

Initial state: 3,4,3,1,2
After  1 day:  2,3,2,0,1
After  2 days: 1,2,1,6,0,8
After  3 days: 0,1,0,5,6,7,8
After  4 days: 6,0,6,4,5,6,7,8,8
After  5 days: 5,6,5,3,4,5,6,7,7,8
After  6 days: 4,5,4,2,3,4,5,6,6,7
After  7 days: 3,4,3,1,2,3,4,5,5,6
After  8 days: 2,3,2,0,1,2,3,4,4,5
After  9 days: 1,2,1,6,0,1,2,3,3,4,8
After 10 days: 0,1,0,5,6,0,1,2,2,3,7,8
After 11 days: 6,0,6,4,5,6,0,1,1,2,6,7,8,8,8
After 12 days: 5,6,5,3,4,5,6,0,0,1,5,6,7,7,7,8,8
After 13 days: 4,5,4,2,3,4,5,6,6,0,4,5,6,6,6,7,7,8,8
After 14 days: 3,4,3,1,2,3,4,5,5,6,3,4,5,5,5,6,6,7,7,8
After 15 days: 2,3,2,0,1,2,3,4,4,5,2,3,4,4,4,5,5,6,6,7
After 16 days: 1,2,1,6,0,1,2,3,3,4,1,2,3,3,3,4,4,5,5,6,8
After 17 days: 0,1,0,5,6,0,1,2,2,3,0,1,2,2,2,3,3,4,4,5,7,8
After 18 days: 6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8

Each day, a 0 becomes a 6 and adds a new 8 to the end of the list, while each other number decreases by 1 if it was present at the start of the day.

In this example, after 18 days, there are a total of 26 fish. After 80 days, there would be a total of 5934.

Find a way to simulate lanternfish. How many lanternfish would there be after 80 days?

Your puzzle answer was 385391.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

Suppose the lanternfish live forever and have unlimited food and space. Would they take over the entire ocean?

After 256 days in the example above, there would be a total of 26984457539 lanternfish!

How many lanternfish would there be after 256 days?

Your puzzle answer was 1728611055389.

Both parts of this puzzle are complete! They provide two gold stars: **

'''

from collections import defaultdict, deque
import numpy
import time

test_data = [ 3,4,3,1,2 ]

DEBUG = False


def draw( data ):
	print( '\t[-1 ]: {0}\n\t[ 0 ]: {1}\n\t[ 1 ]: {2}\n\t[ 2 ]: {3}\n\t[ 3 ]: {4}\n\t[ 4 ]: {5}\n\t[ 5 ]: {6}\n\t[ 6 ]: {7}\n\t[ 7 ]: {8}\n\t[ 8 ]: {9}\n'.format( data[ -1 ],
																	  data[ 0 ],
																	  data[ 1 ],
																	  data[ 2 ],
																	  data[ 3 ],
																	  data[ 4 ],
																	  data[ 5 ],
																	  data[ 6 ],
																	  data[ 7 ],
																	  data[ 8 ]
																	)
		 )


def simulate_fish( data ):

	for i in range( 0, 10 ):
		data[ i - 1 ] = data[ i ]

	if DEBUG:
		draw( data )

	if data[ -1 ]:
		num_new_fish = data[ -1 ]
		data[ 6 ] = data[ 6 ] + data[ -1 ]
		data[ 8 ] = 1 * num_new_fish
		data[ -1 ] = 0

	return data


def simulate_day( data ):
	# # Slow
	# fish_array = list( data )
	# for i in range( 0, len( fish_array ) ):
		# fish_array[ i ] -= 1
		# if fish_array[ i ] < 0:
			# fish_array[ i ] = 6
			# fish_array.append( 8 )

	# # Faster
	# fish_array = data - 1
	# num_new_fish = numpy.count_nonzero( fish_array == -1 )
	# if num_new_fish:
		# new_fish = numpy.empty( num_new_fish )
		# new_fish.fill( 8 )
		# fish_array = numpy.where( fish_array == -1, 6, fish_array )
		# fish_array = numpy.concatenate( ( fish_array, new_fish ) )

	# Fastest
	fish_array = simulate_fish( data )

	# if DEBUG: print( data )

	return fish_array


def count_fish( data ):
	num_fish = 0

	for i in data.keys( ):
		num_fish += data[ i ]

	return num_fish


def parse_data( data ):
	data_dict = defaultdict( int )

	data_dict[ -1 ] = 0
	for i in range( 0, 9 ):
		data_dict[ i ] = 0

	for x in data:
		data_dict[ x ] += 1

	return data_dict


def main( data ):
	num_days = 256

	# Fastest
	data = parse_data( data )
	if DEBUG: draw( data )

	for i in range( 0, num_days ):
		data = simulate_day( data )

	# num_fish = str( len( data ) )
	# Fastest
	num_fish = count_fish( data )
	print( 'After {0} days, there are {1} lantern fish.'.format( num_days, num_fish ) )



if __name__ == "__main__":
	input = r'D:\Projects\Advent_of_Code\2021\day_06_input.txt'

	raw_data = [ ]

	with open( input, 'r' ) as input_file:
		raw_data = [ int( num ) for num in input_file.read( ) if num.isdigit( ) ]

	# # Slow
	# main( test_data )

	# # Faster
	# main( numpy.array( test_data ) )

	# Fastest
	main( raw_data )
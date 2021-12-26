'''
--- Day 15: Chiton ---

You've almost reached the exit of the cave, but the walls are getting closer together. Your submarine can barely still fit, though; the main problem is that the walls of the cave are covered in chitons, and it would be best not to bump any of them.

The cavern is large, but has a very low ceiling, restricting your motion to two dimensions. The shape of the cavern resembles a square; a quick scan of chiton density produces a map of risk level throughout the cave (your puzzle input). For example:

1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581

You start in the top left position, your destination is the bottom right position, and you cannot move diagonally. The number at each position is its risk level; to determine the total risk of an entire path, add up the risk levels of each position you enter (that is, don't count the risk level of your starting position unless you enter it; leaving it adds no risk to your total).

Your goal is to find a path with the lowest total risk. In this example, a path with the lowest total risk is highlighted here:

1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581

The total risk of this path is 40 (the starting position is never entered, so its risk is not counted).

What is the lowest total risk of any path from the top left to the bottom right?


'''
import itertools
from collections import deque

DEBUG = False

test_data = [ '1163751742', '1381373672', '2136511328', '3694931569', '7463417111', '1319128137', '1359912421', '3125421639', '1293138521', '2311944581' ]

def calculate_leaf( path_data ):
	output = ''
	risk_value = 0


	for x in path_data:
		risk_value += x
		output += str( x ) + ' '

	if DEBUG:
		print( output + '\n\t\t------\n' )

	return risk_value


def calculate_path( path_data ):
	total_risk = 999999999999

	obselete_row = len( path_data[ 0 ] )

	for col in range( 0, len( path_data[ 0 ] )  ):
		current_risk = 0
		processed_row = obselete_row

		# Go through the rows
		for processed_row in reversed( range( 0, len( path_data[ 0 ] ) ) ):
			for row in range( 0, len( path_data ) ):
				if row > processed_row:
					break

				elif row == processed_row - 1:
					for i in range( col, len( path_data[ row ] ) ):
						current_risk += path_data[ row ][ i ]
						if DEBUG:
							print( '{0}'.format( path_data[ row ][ i ] ) )

						last_rows = list( itertools.islice( path_data[ row + 1 ], i, len( path_data[ row ] ) ) )
						current_risk = calculate_leaf( last_rows )

					for j in range( processed_row + 1, len( path_data[ 0 ] ) ):
						current_risk += path_data[ j ][ -1 ]
						if DEBUG:
							print( '{0}'.format( path_data[ j ][ -1 ] ) )
					if DEBUG:
						print( '\n------' )

				elif row == processed_row:
					pass

				else:
					current_risk += path_data[ row ][ col ]
					if DEBUG:
						print( '{0}'.format( path_data[ row ][ col ] ) )

		obselete_row = processed_row
		if current_risk < total_risk:
			total_risk = current_risk

	return total_risk


def parse_data( data ):
	results = deque( )

	for datum in data:
		row_deque = deque( [ int( x ) for x in datum ] )
		results.append( row_deque )

	return results


def main( data ):
	risk_map = [ ]
	risk_map = parse_data( data )
	lowest_risk_path = calculate_path( risk_map )

	print( 'Lowest risk path: {0}'.format( lowest_risk_path ) )



if __name__ == "__main__":
	input = r'D:\Projects\Advent_of_Code\2021\day_15_input.txt'

	raw_data = [ ]

	with open( input, 'r' ) as input_file:
		raw_data = [ x.strip( ) for x in input_file.readlines( ) ]

	main( test_data )

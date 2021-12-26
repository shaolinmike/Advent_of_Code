'''
--- Day 9: Smoke Basin ---

These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly settles like rain.

If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).

Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

2199943210
3987894921
9856789892
8767896789
9899965678

Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.

Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the third row (a 5), and one is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent location, and so are not low points.

The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.

Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?

Your puzzle answer was 465.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

Next, you need to find the largest basins so you know what areas are most important to avoid.

A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.

The top-left basin, size 3:

2199943210
3987894921
9856789892
8767896789
9899965678

The top-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678

The middle basin, size 14:

2199943210
3987894921
9856789892
8767896789
9899965678

The bottom-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678

Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.

What do you get if you multiply together the sizes of the three largest basins?

'''


test_data = [ '2199943210',	'3987894921', '9856789892', '8767896789', '9899965678' ]


def row_find_low_points( row ):
	row_data = list( row )
	idx_low_points = [ ]

	for col_idx in range( 0, len( row_data ) ):
		if col_idx == 0:
			if row_data[ col_idx ] < row_data[ col_idx + 1 ]:
				idx_low_points.append( col_idx )

		elif col_idx == len( row_data ) - 1:
			if row_data[ col_idx ] < row_data[ col_idx - 1 ]:
				idx_low_points.append( col_idx )

		else:
			if row_data[ col_idx - 1 ] > row_data[ col_idx ] < row_data[ col_idx + 1 ]:
				idx_low_points.append( col_idx )

	return idx_low_points


def search_row( data ):
	low_points = [ ]
	low_values = [ ]

	for row_idx in range( 0, len( data ) ):
		result = row_find_low_points( data[ row_idx ] )
		if row_idx == 0:
			for low_point in result:
				if data[ row_idx ][ low_point ] < data[ row_idx + 1 ][ low_point ]:
					low_points.append( ( row_idx, low_point ) )

		elif row_idx == len( data ) - 1:
			for low_point in result:
				if data[ row_idx ][ low_point ] < data[ row_idx - 1 ][ low_point ]:
					low_points.append( ( row_idx, low_point ) )

		else:
			for low_point in result:
				if data[ row_idx ][ low_point ] < data[ row_idx - 1 ][ low_point ] and data[ row_idx ][ low_point ] < data[ row_idx + 1 ][ low_point ]:
					low_points.append( ( row_idx, low_point ) )

	for i in low_points:
		low_values.append( data[ i[ 0 ] ][ i[ 1 ] ] )

	print( 'The low points are: {0}'.format( low_values ) )
	print( 'Sum of risk levels: {0}'.format( sum( [ int( x ) + 1 for x in low_values ] ) ) )



def main( data ):
	search_row( data )



if __name__ == "__main__":
	input = r'D:\Projects\Advent_of_Code\2021\day_09_input.txt'

	raw_data = [ ]

	with open( input, 'r' ) as input_file:
		raw_data = [ x.strip( ) for x in input_file.readlines( ) ]

	main( raw_data )

'''
--- Day 4: Giant Squid ---

You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. What you can see, however, is a giant squid that has attached itself to the outside of your submarine.

Maybe it wants to play bingo?

Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:

7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7

After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space):

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

Finally, 24 is drawn:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).

The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.

To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?

Your puzzle answer was 28082.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

On the other hand, it might be wise to try a different strategy: let the giant squid win.

You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.

In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

Figure out which board will win last. Once it wins, what would its final score be?
'''
import itertools
from collections import deque


test_data = ['7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1',
'',
'22 13 17 11  0',
' 8  2 23  4 24',
'21  9 14 16  7',
' 6 10  3 18  5',
' 1 12 20 15 19',
'',
' 3 15  0  2 22',
' 9 18 13 17  5',
'19  8  7 25 23',
'20 11 10 24  4',
'14 21 16 12  6',
'',
'14 21 17 24  4',
'10 16 15  9 19',
'18  8 23 26 20',
'22 11 13  6  5',
' 2  0 12  3  7' ]
# Test data for columns
# '14 10 18  2 22',
# '21 16 15  9 19',
# '17  8 23 26 20',
# '24 11 13  6  5',
# ' 4  0 12  3  7' ]


LEFT = -1
RIGHT = 1

DOWN = 5
DOWN_LEFT = 4
DOWN_RIGHT = 6

UP = -5
UP_LEFT = -6
UP_RIGHT =  -4



def parse_data( data ):
	bingo_boards = [ ]
	current_deque = deque(  )
	num_columns = 0

	bingo_numbers = [ int( x ) for x in data.pop( 0 ).split( ',' ) ]
	data.pop( 0 ) # Clean up the data after extracting the bingo numbers

	num_columns = len( [ x for x in data[ 0 ].split( ) ] )
	for datum in data:
		if datum:
			[ current_deque.append( int( x ) ) for x in datum.split( ) ]

		else:
			bingo_boards.append( current_deque )
			current_deque = deque( )

	# Append the last board
	bingo_boards.append( current_deque )

	return bingo_numbers, bingo_boards, num_columns

def check_column( column, called_numbers ):

	current_column = set( column )
	all_numbers = set( called_numbers )

	# print( '\t\tcheck numbers (col):\n\t\t{0} --- {1}'.format( column, called_numbers )  )

	if current_column.issubset( all_numbers ):
		return True

	return False


def check_row( row, called_numbers ):

	current_row = set( row )
	all_numbers = set( called_numbers )

	# print( '\t\tcheck numbers(row):\n\t\t{0} --- {1}'.format( row, called_numbers )  )

	if current_row.issubset( all_numbers ):
		return True

	return False


def check_board( board, called_numbers, num_columns = 5 ):
	board_sum = -1
	result = False

	# check row
	num_rows = int( len( board ) / num_columns )
	for row in range( 0, num_rows ):
		current_row = list( itertools.islice( board, row * 5, row * 5 + 5 ) )
		if called_numbers[ -1 ] in current_row:

			# Bingo row!
			if check_row( current_row, called_numbers ):
				board_sum = sum( set( board ).difference( called_numbers ) )
				result = True
				# print( '******************** {0}'.format( current_row ) )
				return result, board_sum

	# check columns
	for column in range( 0, num_columns ):
		current_column = [ board[ x ] for x in range( column, len( board ), 5 ) ]
		if called_numbers[ -1 ] in current_column:

			# Bingo column!
			if check_column( current_column, called_numbers ):
				board_sum = sum( set( board ).difference( called_numbers ) )
				result = True
				# print( '******************** {0}'.format( current_column ) )
				return result, board_sum

	return result, board_sum


def find_winning_board( bingo_boards, called_numbers, num_columns = 5 ):
	bingo = False
	score = 0

	for board in bingo_boards:
		matching_numbers = set( called_numbers ).intersection( board )
		# print( '\t***** [{0}] matching numbers: {1}'.format( bingo_boards.index( board ), matching_numbers ) )

		if len( matching_numbers ) >= 5:
			bingo, board_sum = check_board( board, called_numbers, num_columns )

		if bingo:
			score = board_sum * called_numbers[ -1 ]
			return bingo, score, board

	return bingo, None, None


def main( data ):
	bingo = False
	called_numbers = [ ]

	bingo_numbers, bingo_boards, num_columns = parse_data( data )

	for number in bingo_numbers:
		called_numbers.append( number )
		# print( 'Number {0}!\t{1}'.format( number, called_numbers ) )

		found_board, score, board = find_winning_board( bingo_boards, called_numbers, num_columns = num_columns )

		if found_board:
			bingo = True
			print( '\nBingo! The score is: {0}, board #{1}'.format( score,bingo_boards.index( board ) ) )


	if not bingo:
		print( '\nAll numbers called! No more winners!' )


if __name__ == "__main__":
	input = r'D:\Projects\Advent_of_Code\2021\day_04_input.txt'

	raw_data = [ ]

	with open( input, 'r' ) as input_file:
		raw_data = [ x.strip( ) for x in input_file.readlines( ) ]

	main( raw_data )

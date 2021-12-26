'''
--- Day 18: Snailfish ---

You descend into the ocean trench and encounter some snailfish. They say they saw the sleigh keys! They'll even tell you which direction the keys went if you help one of the smaller snailfish with his math homework.

Snailfish numbers aren't like regular numbers. Instead, every snailfish number is a pair - an ordered list of two elements. Each element of the pair can be either a regular number or another pair.

Pairs are written as [x,y], where x and y are the elements within the pair. Here are some example snailfish numbers, one snailfish number per line:

[1,2]
[[1,2],3]
[9,[8,7]]
[[1,9],[8,5]]
[[[[1,2],[3,4]],[[5,6],[7,8]]],9]
[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]
[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]

This snailfish homework is about addition. To add two snailfish numbers, form a pair from the left and right parameters of the addition operator. For example, [1,2] + [[3,4],5] becomes [[1,2],[[3,4],5]].

There's only one problem: snailfish numbers must always be reduced, and the process of adding two snailfish numbers can result in snailfish numbers that need to be reduced.

To reduce a snailfish number, you must repeatedly do the first action in this list that applies to the snailfish number:

	If any pair is nested inside four pairs, the leftmost such pair explodes.
	If any regular number is 10 or greater, the leftmost such regular number splits.

Once no action in the above list applies, the snailfish number is reduced.

During reduction, at most one action applies, after which the process returns to the top of the list of actions. For example, if split produces a pair that meets the explode criteria, that pair explodes before other splits occur.

To explode a pair, the pair's left value is added to the first regular number to the left of the exploding pair (if any), and the pair's right value is added to the first regular number to the right of the exploding pair (if any). Exploding pairs will always consist of two regular numbers. Then, the entire exploding pair is replaced with the regular number 0.

Here are some examples of a single explode action:

	[[[[[9,8],1],2],3],4] becomes [[[[0,9],2],3],4] (the 9 has no regular number to its left, so it is not added to any regular number).
	[7,[6,[5,[4,[3,2]]]]] becomes [7,[6,[5,[7,0]]]] (the 2 has no regular number to its right, and so it is not added to any regular number).
	[[6,[5,[4,[3,2]]]],1] becomes [[6,[5,[7,0]]],3].
	[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]] becomes [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]] (the pair [3,2] is unaffected because the pair [7,3] is further to the left; [3,2] would explode on the next action).
	[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]] becomes [[3,[2,[8,0]]],[9,[5,[7,0]]]].

To split a regular number, replace it with a pair; the left element of the pair should be the regular number divided by two and rounded down, while the right element of the pair should be the regular number divided by two and rounded up. For example, 10 becomes [5,5], 11 becomes [5,6], 12 becomes [6,6], and so on.

Here is the process of finding the reduced result of [[[[4,3],4],4],[7,[[8,4],9]]] + [1,1]:

after addition: [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]
after explode:  [[[[0,7],4],[7,[[8,4],9]]],[1,1]]
after explode:  [[[[0,7],4],[15,[0,13]]],[1,1]]
after split:    [[[[0,7],4],[[7,8],[0,13]]],[1,1]]
after split:    [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]
after explode:  [[[[0,7],4],[[7,8],[6,0]]],[8,1]]

Once no reduce actions apply, the snailfish number that remains is the actual result of the addition operation: [[[[0,7],4],[[7,8],[6,0]]],[8,1]].

The homework assignment involves adding up a list of snailfish numbers (your puzzle input). The snailfish numbers are each listed on a separate line. Add the first snailfish number and the second, then add that result and the third, then add that result and the fourth, and so on until all numbers in the list have been used once.

For example, the final sum of this list is [[[[1,1],[2,2]],[3,3]],[4,4]]:

[1,1]
[2,2]
[3,3]
[4,4]

The final sum of this list is [[[[3,0],[5,3]],[4,4]],[5,5]]:

[1,1]
[2,2]
[3,3]
[4,4]
[5,5]

The final sum of this list is [[[[5,0],[7,4]],[5,5]],[6,6]]:

[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
[6,6]

Here's a slightly larger example:

[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]

The final sum [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]] is found after adding up the above snailfish numbers:

  [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
+ [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
= [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]

  [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]
+ [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
= [[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]

  [[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]
+ [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
= [[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]

  [[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]
+ [7,[5,[[3,8],[1,4]]]]
= [[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]

  [[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]
+ [[2,[2,2]],[8,[8,1]]]
= [[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]

  [[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]
+ [2,9]
= [[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]

  [[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]
+ [1,[[[9,3],9],[[9,0],[0,7]]]]
= [[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]

  [[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]
+ [[[5,[7,4]],7],1]
= [[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]

  [[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]
+ [[[[4,2],2],6],[8,7]]
= [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]

To check whether it's the right answer, the snailfish teacher only checks the magnitude of the final sum. The magnitude of a pair is 3 times the magnitude of its left element plus 2 times the magnitude of its right element. The magnitude of a regular number is just that number.

For example, the magnitude of [9,1] is 3*9 + 2*1 = 29; the magnitude of [1,9] is 3*1 + 2*9 = 21. Magnitude calculations are recursive: the magnitude of [[9,1],[1,9]] is 3*29 + 2*21 = 129.

Here are a few more magnitude examples:

    [[1,2],[[3,4],5]] becomes 143.
    [[[[0,7],4],[[7,8],[6,0]]],[8,1]] becomes 1384.
    [[[[1,1],[2,2]],[3,3]],[4,4]] becomes 445.
    [[[[3,0],[5,3]],[4,4]],[5,5]] becomes 791.
    [[[[5,0],[7,4]],[5,5]],[6,6]] becomes 1137.
    [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]] becomes 3488.

So, given this example homework assignment:

[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]

The final sum is:

[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]

The magnitude of this final sum is 4140.

Add up all of the snailfish numbers from the homework assignment in the order they appear. What is the magnitude of the final sum?
'''

import ast
import math


test_data_0 = [ [ 1,2 ],
				[ [ 1,2 ],3 ],
				[ 9, [ 8,7 ] ],
				[ [ 1,9 ], [ 8,5 ] ],
				[ [ [ [ 1,2 ], [ 3,4 ] ], [ [ 5,6 ], [ 7,8 ] ] ],9 ],
				[ [ [ 9, [ 3,8 ] ], [ [ 0,9 ],6 ] ], [ [ [ 3,7 ], [ 4,9 ] ],3 ] ],
				[ [ [ [ 1,3 ], [ 5,3 ] ], [ [ 1,3 ], [ 8,7 ] ] ], [ [ [ 4,9 ], [ 6,9 ] ], [ [ 8,2 ], [ 7,3 ] ] ] ]
				]

test_data_1 = [ [ 1, 1 ], [ 2, 2 ], [ 3, 3 ], [ 4,4 ] ]
test_data_2 = [ [ 1, 1 ], [ 2, 2 ], [ 3, 3 ], [ 4,4 ], [ 5, 5 ] ]
test_data_3 = [ [ 1, 1 ], [ 2, 2 ], [ 3, 3 ], [ 4,4 ], [ 5, 5 ], [ 6, 6 ] ]

test_data_4 = [ [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],
				[7,[[[3,7],[4,3]],[[6,3],[8,8]]]],
				[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]],
				[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]],
				[7,[5,[[3,8],[1,4]]]],
				[[2,[2,2]],[8,[8,1]]],
				[2,9],
				[1,[[[9,3],9],[[9,0],[0,7]]]],
				[[[5,[7,4]],7],1],
				[[[[4,2],2],6],[8,7]]
			  ]


def set_leftmost_num( num, explodey_value ):

	if isinstance( num[ 0 ], list ):
		set_leftmost_num( num[ 0 ], explodey_value )

	else:
		num[ 0 ] += explodey_value


def split_pair( snailfish_number ):
	result = [ ]
	result = [ math.floor( snailfish_number / 2 ), math.ceil( snailfish_number / 2 ) ]

	return result

def recurse_right_hand( right_hand, depth ):
	sub_explodey_left = -1
	sub_explodey_right = -1

	right_hand, explodey_left, explodey_right = parse_snailfish_pairs( right_hand, depth + 1 )

	if isinstance( sub_explodey_right, list ):
		right_hand, sub_explodey_left, sub_explodey_right = recurse_right_hand( right_hand, depth + 1 )

	if sub_explodey_left > 0:
		explodey_left += sub_explodey_left

	if sub_explodey_right > 0:
		explodey_right += sub_explodey_right

	return right_hand, explodey_left, explodey_right


def parse_snailfish_pairs( data, depth = 0 ):
	left_hand = data[ 0 ]
	right_hand  = data[ 1 ]

	explodey_left = -1
	explodey_right = -1

	split_result = [ ]

	if isinstance( left_hand, list ):
		left_hand, explodey_left, explodey_right = parse_snailfish_pairs( left_hand, depth + 1 )

	else:
		# If nested 4 layers deep, explode
		if depth == 4:
			temp_right = -1
			if isinstance( right_hand, list ):
				temp_right, explodey_left, explodey_right = parse_snailfish_pairs( right_hand, depth + 1 )
			else:
				temp_right = right_hand
			explodey_left = left_hand
			explodey_right = temp_right
			return 0, explodey_left, explodey_right

		else:
			if left_hand > 10:
				left_hand = split_pair( left_hand )
				print( 'split' )

			else:
				output = ''
				for i in range( 0, depth ):
					output += '\t'
				print( '{0}{1}'.format( output, data ) )

	if isinstance( explodey_right, list ):
		sub_explodey_left = -1
		sub_explodey_right = -1

		right_hand, sub_explodey_left, sub_explodey_right, recurse_right_hand( right_hand, depth + 1 )

		if sub_explodey_left > 0:
			explodey_left += sub_explodey_left

	if isinstance( right_hand, list ):
		if isinstance( right_hand[ 0 ], list ):
			sub_explodey_left = -1
			sub_explodey_right = -1

			right_hand, sub_explodey_left, sub_explodey_right, recurse_right_hand( right_hand, depth + 1 )

			if sub_explodey_left > 0:
				explodey_left += sub_explodey_left

			if sub_explodey_right > 0:
				explodey_right += explodey_right

		if explodey_right > 0:
			set_leftmost_num( right_hand, explodey_right )
		right_hand, explodey_left, explodey_right = parse_snailfish_pairs( right_hand, depth + 1 )

	else:
		if right_hand > 10:
			right_hand = split_pair( right_hand )
			print( 'split' )

		else:
			output = ''
			for i in range( 0, depth ):
				output += '\t'
			print( '{0}{1}'.format( output, data ) )

	if explodey_left > 0:
		left_hand = explodey_left
		explodey_left = -1

	output = ''
	for i in range( 0, depth ):
		output += '\t'
	print( '{0}[ {1}, {2} ], {3}, {4}'.format( output, left_hand, right_hand, explodey_left, explodey_right ) )
	return [ left_hand, right_hand ], explodey_left, explodey_right


def depopulate_snailfish( snailfish ):
	snailfish_num = [ ]

	snailfish_num, _, _ = parse_snailfish_pairs( snailfish )

	return snailfish_num


def join_snailfish( snailfish_1, snailfish_2 ):
	snailfish = [ ]
	snailfishies = [ ]

	snailfishies = [ snailfish_1,  snailfish_2 ]
	snailfish = depopulate_snailfish( snailfishies )

	return snailfish


def parse_data( data ):
	result = ''

	print( 'left leaf'.format( ) )


	print( 'right leaf'.format( ) )


	print( 'Result: {0}'.format( result ) )


def main( data ):
	snailfish_number = data[ 0 ]

	print( '*** {0}'.format( data ) )
	for datum in data[ 1: ]:
		result = join_snailfish( snailfish_number, datum )
		snailfish_number = depopulate_snailfish( result )
		# print( '*** {0}'.format( snailfish_number ) )
		print( snailfish_number )

	print( 'The snailfish number is: {0}'.format( snailfish_number ) )



if __name__ == "__main__":
	input = r'D:\Projects\Advent_of_Code\2021\day_18_input.txt'

	raw_data = [ ]

	with open( input, 'r' ) as input_file:
		raw_data = [ ast.literal_eval( x ) for x in input_file.read( ).split( ) ]

	# main( test_data_1 )
	# main( test_data_2 )
	# main( test_data_3 )
	main( test_data_4 )

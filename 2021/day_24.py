'''
--- Day 24: Arithmetic Logic Unit ---

Magic smoke starts leaking from the submarine's arithmetic logic unit (ALU). Without the ability to perform basic arithmetic and logic functions, the submarine can't produce cool patterns with its Christmas lights!

It also can't navigate. Or run the oxygen system.

Don't worry, though - you probably have enough oxygen left to give you enough time to build a new ALU.

The ALU is a four-dimensional processing unit: it has integer variables w, x, y, and z. These variables all start with the value 0. The ALU also supports six instructions:

    inp a - Read an input value and write it to variable a.
    add a b - Add the value of a to the value of b, then store the result in variable a.
    mul a b - Multiply the value of a by the value of b, then store the result in variable a.
    div a b - Divide the value of a by the value of b, truncate the result to an integer, then store the result in variable a. (Here, "truncate" means to round the value toward zero.)
    mod a b - Divide the value of a by the value of b, then store the remainder in variable a. (This is also called the modulo operation.)
    eql a b - If the value of a and b are equal, then store the value 1 in variable a. Otherwise, store the value 0 in variable a.

In all of these instructions, a and b are placeholders; a will always be the variable where the result of the operation is stored (one of w, x, y, or z), while b can be either a variable or a number. Numbers can be positive or negative, but will always be integers.

The ALU has no jump instructions; in an ALU program, every instruction is run exactly once in order from top to bottom. The program halts after the last instruction has finished executing.

(Program authors should be especially cautious; attempting to execute div with b=0 or attempting to execute mod with a<0 or b<=0 will cause the program to crash and might even damage the ALU. These operations are never intended in any serious ALU program.)

For example, here is an ALU program which takes an input number, negates it, and stores it in x:

inp x
mul x -1

Here is an ALU program which takes two input numbers, then sets z to 1 if the second input number is three times larger than the first input number, or sets z to 0 otherwise:

inp z
inp x
mul z 3
eql z x

Here is an ALU program which takes a non-negative integer as input, converts it into binary, and stores the lowest (1's) bit in z, the second-lowest (2's) bit in y, the third-lowest (4's) bit in x, and the fourth-lowest (8's) bit in w:

inp w
add z w
mod z 2
div w 2
add y w
mod y 2
div w 2
add x w
mod x 2
div w 2
mod w 2

Once you have built a replacement ALU, you can install it in the submarine, which will immediately resume what it was doing when the ALU failed: validating the submarine's model number. To do this, the ALU will run the MOdel Number Automatic Detector program (MONAD, your puzzle input).

Submarine model numbers are always fourteen-digit numbers consisting only of digits 1 through 9. The digit 0 cannot appear in a model number.

When MONAD checks a hypothetical fourteen-digit model number, it uses fourteen separate inp instructions, each expecting a single digit of the model number in order of most to least significant. (So, to check the model number 13579246899999, you would give 1 to the first inp instruction, 3 to the second inp instruction, 5 to the third inp instruction, and so on.) This means that when operating MONAD, each input instruction should only ever be given an integer value of at least 1 and at most 9.

Then, after MONAD has finished running all of its instructions, it will indicate that the model number was valid by leaving a 0 in variable z. However, if the model number was invalid, it will leave some other non-zero value in z.

MONAD imposes additional, mysterious restrictions on model numbers, and legend says the last copy of the MONAD documentation was eaten by a tanuki. You'll need to figure out what MONAD does some other way.

To enable as many submarine features as possible, find the largest valid fourteen-digit model number that contains no 0 digits. What is the largest model number accepted by MONAD?

To begin, get your puzzle input.
'''

alu_memory = { }
test_data = [ 	[ 'inp', 'w' ],
				[ 'add', 'z', 'w' ],
				[ 'mod', 'z', '2' ],
				[ 'div', 'w', '2' ],
				[ 'add', 'y', 'w' ],
				[ 'mod', 'y', '2' ],
				[ 'div', 'w', '2' ],
				[ 'add', 'x', 'w' ],
				[ 'mod', 'x', '2' ],
				[ 'div', 'w', '2' ],
				[ 'mod', 'w', '2' ],
			]

DEBUG = False



def alu_inp( arg1 ):
	if arg1.isalpha:
		if arg1 == 'w':
			alu_memory[ arg1 ] = alu_memory[ 'model_num' ].pop( 0 )


def alu_add( arg1: str, arg2 ):
	if arg2.isalpha( ):
		arg2 = alu_memory[ arg2 ]

	alu_memory[ arg1 ] = alu_memory[ arg1 ] + int( arg2 )


def alu_mul( arg1: str, arg2 ):
	if arg2.isalpha( ):
		arg2 = alu_memory[ arg2 ]

	alu_memory[ arg1 ] = alu_memory[ arg1 ] * int( arg2 )


def alu_div( arg1: str, arg2 ):
	if arg2.isalpha( ):
		arg2 = alu_memory[ arg2 ]

	if int( arg2 ) != 0:
		alu_memory[ arg1 ] = alu_memory[ arg1 ] // int( arg2 )

	else:
		raise AssertionError( 'Null input! Received {0}. Expected a non-zero number'.format( arg2 ) )


def alu_mod( arg1: str, arg2 ):
	if arg2.isalpha( ):
		arg2 = alu_memory[ arg2 ]

	if int( arg2 ) != 0:
		alu_memory[ arg1 ] = alu_memory[ arg1 ] % int( arg2 )

	else:
		raise AssertionError( 'Null input! Received {0}. Expected a non-zero number'.format( arg2 ) )


def alu_eql( arg1: str, arg2 ):
	if arg2.isalpha( ):
		arg2 = alu_memory[ arg2 ]

	elif arg2.isdigit( ):
		arg2 = int( arg2 )

	else:
		pass

	if alu_memory[ arg1 ] == arg2:
		alu_memory[ arg1 ] = 1

	else:
		alu_memory[ arg1 ] = 0


def initialize_memory( memory ):
	memory[ 'w' ] = memory[ 'x' ] = memory[ 'y' ] = memory[ 'z' ] = 0
	memory[ 'model_num' ] = 0


def process_instruction( instruction ):
	cmd = instruction[ 0 ]
	arg1 = instruction[ 1 ]

	if cmd == 'inp':
		alu_inp( arg1 )

	else:
		arg2 = instruction[ 2 ]

		if cmd == 'add':
			alu_add( arg1, arg2)

		elif cmd == 'mul':
			alu_mul( arg1, arg2)

		elif cmd == 'div':
			alu_div( arg1, arg2)

		elif cmd == 'mod':
			alu_mod( arg1, arg2)

		elif cmd == 'eql':
			alu_eql( arg1, arg2)


def is_valid_model_num( model_num, data ):

	alu_memory[ 'model_num' ] = [ int( x ) for x in model_num ]

	for inst in data:
		# if DEBUG: print( 'Mem report: [ {0} ]'.format( ' '.join( inst ) ) )
		process_instruction( inst )
		# if DEBUG: print( '\t\t{0} : {1} : {2} : {3}'.format( alu_memory[ 'w' ], alu_memory[ 'x' ], alu_memory[ 'y' ], alu_memory[ 'z' ] ) )

	if alu_memory[ 'z' ] == 0:
		return True

	return False


def search_model_numbers( data, n1, n2 ):
	model_num = ''

	num = n1
	while num < n2:
		n = str( num )
		if '0' in n:
			idx = n.index( '0' )
			n = ''.join( list( n[ 0:idx ] ) + ( [ '1' ] * ( len( n ) - idx ) ) )
			num = int( n )

		is_valid = is_valid_model_num( n, data )
		if is_valid:
			model_num = n
			print( 'Model number {0} is valid'.format( model_num ) )

		num += 1

	return model_num


def find_best_model_num( data ):
	model_num = ''
	result = False

				# 84217691436862 too low
				# 84218135599872 too low
				# 84218135611111
	n_initial 	= 84218135599872
	n_final 	= 99955554192826
				# 94358948136858
				# 99955554192826 too high
	n = 0

	while result == False:
		if n_final < n_initial:
			return None

		elif n_final == n_initial:
			return model_num

		else:
			# Find the midpoint of the search
			n = str( round( ( n_initial + n_final ) / 2 ) )
			# print( '\t{0}'.format( n ) )
			if n == str( n_initial ) or n == str( n_final ):
				result = True
			if '0' in n:
				# n = n.replace( '0', '1' )
				n = ''.join( list( n[ 0:n.index( '0' ) ] ) + ( [ '1' ] * ( len( n ) - n.index( '0' ) ) ) )

			is_valid = is_valid_model_num( n, data )
			if is_valid:
				model_num = str( n )
				n_initial = int( n )

			else:
				n_final = int( n )

	raise AssertionError( 'No solution! This should never happen' )


def main( data ):

	initialize_memory( alu_memory )
	result = find_best_model_num( data )
	# result = search_model_numbers( data, 92111111111111, 99955554192826 )

	if result:
		print( 'Highest possible model number: {0}'.format( str( result ) ) )

	# Test data
	# model_num = '13579246899999'
	# is_valid = is_valid_model_num( model_num, data )
	# if is_valid:
		# print( 'Model number: {0} is valid'.format( model_num ) )


if __name__ == "__main__":
	input = r'D:\Projects\Advent_of_Code\2021\day_24_input.txt'

	raw_data = [ ]

	with open( input, 'r' ) as input_file:
		raw_data = [ x.strip( ).split(' ' ) for x in input_file.readlines( ) ]


	main( raw_data )

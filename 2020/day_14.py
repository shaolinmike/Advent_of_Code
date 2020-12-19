'''
--- Day 14: Docking Data ---
As your ferry approaches the sea port, the captain asks for your help again. The computer system that runs this port isn't compatible with the docking program on the ferry, so the docking parameters aren't being correctly initialized in the docking program's memory.

After a brief inspection, you discover that the sea port's computer system uses a strange bitmask system in its initialization program. Although you don't have the correct decoder chip handy, you can emulate it in software!

The initialization program (your puzzle input) can either update the bitmask or write a value to memory. Values and memory addresses are both 36-bit unsigned integers. For example, ignoring bitmasks for a moment, a line like mem[8] = 11 would write the value 11 to memory address 8.

The bitmask is always given as a string of 36 bits, written with the most significant bit (representing 2^35) on the left and the least significant bit (2^0, that is, the 1s bit) on the right. The current bitmask is applied to values immediately before they are written to memory: a 0 or 1 overwrites the corresponding bit in the value, while an X leaves the bit in the value unchanged.

For example, consider the following program:

mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
This program starts by specifying a bitmask (mask = ....). The mask it specifies will overwrite two bits in every written value: the 2s bit is overwritten with 0, and the 64s bit is overwritten with 1.

The program then attempts to write the value 11 to memory address 8. By expanding everything out to individual bits, the mask is applied as follows:

value:  000000000000000000000000000000001011  (decimal 11)
mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
result: 000000000000000000000000000001001001  (decimal 73)
So, because of the mask, the value 73 is written to memory address 8 instead. Then, the program tries to write 101 to address 7:

value:  000000000000000000000000000001100101  (decimal 101)
mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
result: 000000000000000000000000000001100101  (decimal 101)
This time, the mask has no effect, as the bits it overwrote were already the values the mask tried to set. Finally, the program tries to write 0 to address 8:

value:  000000000000000000000000000000000000  (decimal 0)
mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
result: 000000000000000000000000000001000000  (decimal 64)
64 is written to address 8 instead, overwriting the value that was there previously.

To initialize your ferry's docking program, you need the sum of all values left in memory after the initialization program completes. (The entire 36-bit address space begins initialized to the value 0 at every address.) In the above example, only two values in memory are not zero - 101 (at address 7) and 64 (at address 8) - producing a sum of 165.

Execute the initialization program. What is the sum of all values left in memory after it completes?

Your puzzle answer was 9296748256641.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

For some reason, the sea port's computer system still can't communicate with your ferry's docking program. It must be using version 2 of the decoder chip!

A version 2 decoder chip doesn't modify the values being written at all. Instead, it acts as a memory address decoder. Immediately before a value is written to memory, each bit in the bitmask modifies the corresponding bit of the destination memory address in the following way:

	If the bitmask bit is 0, the corresponding memory address bit is unchanged.
	If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
	If the bitmask bit is X, the corresponding memory address bit is floating.

A floating bit is not connected to anything and instead fluctuates unpredictably. In practice, this means the floating bits will take on all possible values, potentially causing many memory addresses to be written all at once!

For example, consider the following program:

mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1

When this program goes to write to memory address 42, it first applies the bitmask:

address: 000000000000000000000000000000101010  (decimal 42)
mask:    000000000000000000000000000000X1001X
result:  000000000000000000000000000000X1101X

After applying the mask, four bits are overwritten, three of which are different, and two of which are floating. Floating bits take on every possible combination of values; with two floating bits, four actual memory addresses are written:

000000000000000000000000000000011010  (decimal 26)
000000000000000000000000000000011011  (decimal 27)
000000000000000000000000000000111010  (decimal 58)
000000000000000000000000000000111011  (decimal 59)

Next, the program is about to write to memory address 26 with a different bitmask:

address: 000000000000000000000000000000011010  (decimal 26)
mask:    00000000000000000000000000000000X0XX
result:  00000000000000000000000000000001X0XX

This results in an address with three floating bits, causing writes to eight memory addresses:

000000000000000000000000000000010000  (decimal 16)
000000000000000000000000000000010001  (decimal 17)
000000000000000000000000000000010010  (decimal 18)
000000000000000000000000000000010011  (decimal 19)
000000000000000000000000000000011000  (decimal 24)
000000000000000000000000000000011001  (decimal 25)
000000000000000000000000000000011010  (decimal 26)
000000000000000000000000000000011011  (decimal 27)

The entire 36-bit address space still begins initialized to the value 0 at every address, and you still need the sum of all values left in memory at the end of the program. In this example, the sum is 208.

Execute the initialization program using an emulator for a version 2 decoder chip. What is the sum of all values left in memory after it completes?

'''

from itertools import permutations

test_data_1 = [ 'mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X',
					 'mem[8] = 11',
					 'mem[7] = 101',
					 'mem[8] = 0' ]

test_data_2 = [ 'mask = 000000000000000000000000000000X1001X',
					 'mem[42] = 100',
					 'mask = 00000000000000000000000000000000X0XX',
					 'mem[26] = 1' ]


class Memory_Array( ):

	def __init__( self, bit_length = 36 ):
		self.bit_length = bit_length
		self.mask = [ ]
		self.memory = { }
		self.floating_memory = [ ]


	def apply_bitmask( self, bit_string, mask ):
		new_bit_array = list( '000000000000000000000000000000000000' )
		bit_array = list( bit_string )

		for idx in reversed( range( 0, self.bit_length ) ):
			# Apply mask
			if mask[ idx ] == 'X':
				new_bit_array[ idx ] = bit_array[ idx ]

			elif mask[ idx ] == '1':
				new_bit_array[ idx ] = '1'

			elif mask[ idx ] == '0':
				new_bit_array[ idx ] = '0'

		return new_bit_array


	def generate_floating_registers( self, register, bit_string ):
		floating_registers = [ ]
		num_floats = self.mask.count( 'X' )
		raw_float_data = [ 0 for x in range( 0, num_floats ) ] + [ 1 for x in range( 0, num_floats ) ]

		float_vals = sorted( set( list( permutations( raw_float_data, num_floats ) ) ) )
		float_idxs = [ idx for idx, x in enumerate( self.mask ) if x == 'X' ]
		on_idxs = [ idx for idx, x in enumerate( self.mask ) if x == '1' ]

		for floating_bits in float_vals:
			temp_address = list( '{0:036b}'.format( register ) )
			for idx, bit in enumerate( floating_bits ):
				temp_address[ float_idxs[ idx ] ] = bit

				for x in on_idxs:
					temp_address[ x ] = '1'

			floating_registers.append( int( ''.join( map( str, temp_address ) ), 2 ) )
			# print( '\t\tFloating mem: [{0}] {1} ( decimal {2} )'.format( register, ''.join( map( str, temp_address ) ), int( ''.join( map( str, temp_address ) ), 2 ) ) )

		return floating_registers


	def read_memory( self, register, binary = False ):
		val =  ''.join( map( str, self.memory[ register ] ) )

		if binary:
			return val

		return int( val, 2 )


	def write_memory( self, register, val : int, floating_bit ):
		bit_string = '{0:036b}'.format( int( val ) )
		registers = [ register ]

		if floating_bit:
			registers = self.generate_floating_registers( register, bit_string )

		for register in registers:
			self.memory[ register ] = list( '000000000000000000000000000000000000' )
			if floating_bit:
				new_bitarray = list( bit_string )
			else:
				new_bitarray = self.apply_bitmask( bit_string, self.mask )
			self.memory[ register ] = new_bitarray


def initialize_memory( raw_data, mem_array, floating_bit = False ):

	for data in raw_data:
		datum = data.split( ' = ' )

		if 'mask' in datum[ 0 ]:
			mem_array.mask = datum[ 1 ]
			# print( '\tMask: {0}'.format( mem_array.mask ) )
		elif 'mem[' in datum[ 0 ]:
			register = int( datum[ 0 ].replace( ']', '' ).split( '[' )[ 1 ] )
			mem_array.write_memory( register, datum[ 1 ], floating_bit )

			# print( '\t\tmem[{0}]: {1} ( decimal {2} )\n'.format( register, mem_array.read_memory( register, binary = True ), mem_array.read_memory( register ) ) )

	return



if __name__ == "__main__":
	input = r'D:\Projects\Python\Personal\Advent_of_Code\2020\day_14_input.txt'
	# input = r'D:\Dropbox\Projects\Python\Advent_of_Code\2020\day_14_input.txt'

	with open( input, 'r' ) as input_file:
		raw_data = input_file.read( ).split( '\n' )

	# mem_register = Memory_Array( )
	# initialize_memory( raw_data, mem_register )
	# print( '[ v1 ] The sum of all values in memory: {0}\n'.format( sum( [ mem_register.read_memory( x ) for x in mem_register.memory ] ) ) )

	mem_register = Memory_Array( )
	initialize_memory( raw_data, mem_register, floating_bit = True )
	print( '[ v2 ] The sum of all values in memory: {0}'.format( sum( [ mem_register.read_memory( x ) for x in mem_register.memory ] ) ) )
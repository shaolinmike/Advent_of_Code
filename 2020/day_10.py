'''
--- Day 10: Adapter Array ---

Patched into the aircraft's data port, you discover weather forecasts of a massive tropical storm. Before you can figure out whether it will impact your vacation plans, however, your device suddenly turns off!

Its battery is dead.

You'll need to plug it in. There's only one problem: the charging outlet near your seat produces the wrong number of jolts. Always prepared, you make a list of all of the joltage adapters in your bag.

Each of your joltage adapters is rated for a specific output joltage (your puzzle input). Any given adapter can take an input 1, 2, or 3 jolts lower than its rating and still produce its rated output joltage.

In addition, your device has a built-in joltage adapter rated for 3 jolts higher than the highest-rated adapter in your bag. (If your adapter list were 3, 9, and 6, your device's built-in adapter would be rated for 12 jolts.)

Treat the charging outlet near your seat as having an effective joltage rating of 0.

Since you have some time to kill, you might as well test all of your adapters. Wouldn't want to get to your resort and realize you can't even charge your device!

If you use every adapter in your bag at once, what is the distribution of joltage differences between the charging outlet, the adapters, and your device?

For example, suppose that in your bag, you have adapters with the following joltage ratings:

	16
	10
	15
	5
	1
	11
	7
	19
	6
	12
	4

With these adapters, your device's built-in joltage adapter would be rated for 19 + 3 = 22 jolts, 3 higher than the highest-rated adapter.

Because adapters can only connect to a source 1-3 jolts lower than its rating, in order to use every adapter, you'd need to choose them like this:

 The charging outlet has an effective rating of 0 jolts, so the only adapters that could connect to it directly would need to have a joltage rating of 1, 2, or 3 jolts. Of these, only one you have is an adapter rated 1 jolt (difference of 1).
 From your 1-jolt rated adapter, the only choice is your 4-jolt rated adapter (difference of 3).
 From the 4-jolt rated adapter, the adapters rated 5, 6, or 7 are valid choices. However, in order to not skip any adapters, you have to pick the adapter rated 5 jolts (difference of 1).
 Similarly, the next choices would need to be the adapter rated 6 and then the adapter rated 7 (with difference of 1 and 1).
 The only adapter that works with the 7-jolt rated adapter is the one rated 10 jolts (difference of 3).
 From 10, the choices are 11 or 12; choose 11 (difference of 1) and then 12 (difference of 1).
 After 12, only valid adapter has a rating of 15 (difference of 3), then 16 (difference of 1), then 19 (difference of 3).
 Finally, your device's built-in adapter is always 3 higher than the highest adapter, so its rating is 22 jolts (always a difference of 3).

In this example, when using every adapter, there are 7 differences of 1 jolt and 5 differences of 3 jolts.

Here is a larger example:

	28
	33
	18
	42
	31
	14
	46
	20
	48
	47
	24
	23
	49
	45
	19
	38
	39
	11
	1
	32
	25
	35
	8
	17
	7
	9
	4
	2
	34
	10
	3

In this larger example, in a chain that uses all of the adapters, there are 22 differences of 1 jolt and 10 differences of 3 jolts.

Find a chain that uses all of your adapters to connect the charging outlet to your device's built-in adapter and count the joltage differences between the charging outlet, the adapters, and your device. What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?

Your puzzle answer was 2590.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

To completely determine whether you have enough adapters, you'll need to figure out how many different ways they can be arranged. Every arrangement needs to connect the charging outlet to your device. The previous rules about when adapters can successfully connect still apply.

The first example above (the one that starts with 16, 10, 15) supports the following arrangements:

(0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 6, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 6, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 6, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 7, 10, 12, 15, 16, 19, (22)

(The charging outlet and your device's built-in adapter are shown in parentheses.) Given the adapters from the first example, the total number of arrangements that connect the charging outlet to your device is 8.

The second example above (the one that starts with 28, 33, 18) has many arrangements. Here are a few:

(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49, (52)

(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 49, (52)

(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 46, 48, 49, (52)

(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 46, 49, (52)

(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 47, 48, 49, (52)

(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
46, 48, 49, (52)

(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
46, 49, (52)

(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
47, 48, 49, (52)

(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
47, 49, (52)

(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
48, 49, (52)

In total, this set of adapters can connect the charging outlet to your device in 19208 distinct arrangements.

You glance back down at your bag and try to remember why you brought so many adapters; there must be more than a trillion valid ways to arrange them! Surely, there must be an efficient way to count the arrangements.

What is the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device?


'''

from collections import  deque

test_data_1 = [ 16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4 ]
test_data_2 = [ 28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3 ]


def find_configs_by_joltage_diff( adapters, diff ):
	valid_adapters = [ ]
	plugged_adapters = sorted( adapters )

	if abs( 0 - plugged_adapters[ 0 ] ) == diff:
		valid_adapters.append( plugged_adapters[ 0 ] )

	for idx, x in enumerate( plugged_adapters ):
		if idx < len( adapters ) - 1:
			if abs( x - plugged_adapters[ idx + 1 ] ) == diff:
				valid_adapters.append( plugged_adapters[ idx + 1 ] )

		elif idx == len( adapters ) - 1:
			if abs( x - plugged_adapters[ -1 ] + 3 ) == diff:
				valid_adapters.append( plugged_adapters[ -1 ] + 3 )

		# print( '{0} : {1}\t\t{2}'.format( idx, x, plugged_adapters ) )

	return valid_adapters


def test_adapter_config( test_adapters ):
	valid_adapters = [ ]
	plugged_adapters = sorted( test_adapters )

	if abs( 0 - plugged_adapters[ 0 ]) not in [ 1, 2, 3 ]:
		return [ ]

	for idx, x in enumerate( plugged_adapters ):
		if idx != len( test_adapters ) - 1:
			if abs( x - plugged_adapters[ idx + 1 ] ) in [ 1, 2, 3 ]:
				valid_adapters.append( x )
				# print( '\t[ {0} ] : {1}'.format( x, plugged_adapters ) )
			else:
				return [ ]
		elif idx == len( test_adapters ):
			if abs( x - plugged_adapters[ idx + 1 ] ) in [ 1, 2, 3 ]:
				valid_adapters.append( x )
			else:
				return [ ]

	return valid_adapters


def optimize_adapters( adapter_configs ):
	valid_adapters = [ ]

	plugged_adapters = sorted( adapter_configs )
	one_joltage_configs = deque( find_configs_by_joltage_diff( plugged_adapters, 1 ) )

	while one_joltage_configs:
		test_case = plugged_adapters.copy( )
		test_case.remove( one_joltage_configs.popleft( )  )
		if test_adapter_config( test_case ):
			valid_adapters.append( test_case )

	# for x in one_joltage_configs:
		# test_case = plugged_adapters.copy( )
		# test_case.remove( x )
		# # print( '{0}'.format( x ) )
		# if test_adapter_config( test_case ):
			# valid_adapters.append( test_case )

	return valid_adapters


def find_optimized_configs( adapters ):
	plugged_adapters = sorted( adapters )
	optimized_configs = [ plugged_adapters ]
	initial_configs = optimize_adapters( plugged_adapters )
	optimized_configs.extend( initial_configs )
	valid_adapter_configs = deque( initial_configs )

	while valid_adapter_configs:
		output = optimize_adapters( valid_adapter_configs.popleft( ) )
		result = [ x for x in output if x not in optimized_configs ]
		# print( '{0}\n\n{1}\n******************'.format( optimized_configs, result ) )
		# print( '{0}\n******************'.format( result ) )
		optimized_configs.extend( result )
		if result:
			valid_adapter_configs.extend( result )
		# for x in result:
			# valid_adapter_configs.append( x )

	temp = [ x for x in optimized_configs if x ]
	config_set = set( tuple( x ) for x in temp )
	return optimized_configs


def find_optimized_configs2( adapters ):
	plugged_adapters = sorted( adapters )
	optimized_configs = [ ]
	valid_adapter_configs = deque( [ plugged_adapters ] )
	one_joltage_configs = find_configs_by_joltage_diff( data, 1 )

	while valid_adapter_configs:
		output = optimize_adapters( valid_adapter_configs.popleft( ) )
		result = [ x for x in output if x not in optimized_configs ]
		# print( '{0}\n\n{1}\n******************'.format( optimized_configs, result ) )
		# print( '{0}\n******************'.format( result ) )
		optimized_configs.append( result )
		if result:
			valid_adapter_configs.append( result )
		# for x in result:
			# valid_adapter_configs.append( x )

	config_set = set( tuple( x ) for x in optimized_configs )
	return optimized_configs



if __name__ == "__main__":
	input = r'D:\Projects\Python\Personal\Advent_of_Code\2020\day_10_input.txt'
	data = [ ]

	with open( input, 'r' ) as input_file:
		data = [ int( line.strip( ) ) for line in input_file.readlines( ) ]

	data = test_data_2

	one_joltage_configs = find_configs_by_joltage_diff( data, 1 )
	three_joltage_configs = find_configs_by_joltage_diff( data, 3 )
	valid_optimizations = find_optimized_configs( data )

	# for x in one_joltage_adapters:
		# print( '\t{0}'.format( x ) )
	# print( )
	print( '+/- 1J adapters: {0}'.format( len( one_joltage_configs ) ) )

	# for x in three_joltage_adapters:
		# print( '\t{0}'.format( x ) )
	# print( )
	print( '+/- 3J adapters: {0}'.format( len( three_joltage_configs ) ) )
	print( '\nTotal possible configurations: {0}'.format( len( valid_optimizations ) ) )

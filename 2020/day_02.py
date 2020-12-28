'''
--- Day 2: Password Philosophy ---

Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

	1-3 a: abcde
	1-3 b: cdefg
	2-9 c: ccccccccc

Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?

Your puzzle answer was 515.

--- Part Two ---

While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

	1-3 a: abcde is valid: position 1 contains a and position 3 does not.
	1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
	2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

How many passwords are valid according to the new interpretation of the policies?

Your puzzle answer was 711.

Both parts of this puzzle are complete! They provide two gold stars: **
'''

def get_password_policy( raw_data ):
	data = raw_data.split( )
	pwd_key = data[ 1 ]
	pwd_rules = data[ 0 ].split( '-' )

	valid_range = tuple( map( int, pwd_rules ) )

	return valid_range, pwd_key


def check_password_rental( entry ):
	password = entry[ 1 ]

	valid_hits, pwd_key = get_password_policy( entry[ 0 ] )
	hits = password.count( pwd_key )

	if valid_hits[ 0 ] <= hits <= valid_hits[ 1 ]:
		return True

	return False


def check_password_toboggan( entry ):
	is_valid = False
	password = entry[ 1 ]

	valid_positions, pwd_key = get_password_policy( entry[ 0 ] )

	for idx in valid_positions:
		relative_idx = idx - 1

		if relative_idx > len( password ):
			is_valid = False

		else:
			if password[ relative_idx ] == pwd_key:
				is_valid = not is_valid

	return is_valid


def main( data,  use_rental_policy = False ):
	result = False
	invalid_passwords = [ ]
	valid_passwords = [ ]

	for datum in data:
		if use_rental_policy:
			result = check_password_rental( datum )
		else:
			result = check_password_toboggan( datum )

		if result:
			valid_passwords.append( datum )
		else:
			invalid_passwords.append( datum )

	print( '\tValid passwords:\t\t{0}*\n\tInvalid passwords: \t{1}\n'.format( len( valid_passwords ), len( invalid_passwords ) ) )



if __name__ == "__main__":
	input = r'D:\Projects\Python\Personal\Advent_of_Code\2020\day_02_input.txt'
	# input = r'D:\Dropbox\Projects\Python\Advent_of_Code\2020\day_02_input.txt'

	with open( input, 'r' ) as input_file:
		raw_data = [ x.strip( ).split( ': ' ) for x in input_file.readlines( ) ]

	print( 'Part One:' )
	main( raw_data, use_rental_policy = True )

	print( 'Part Two:' )
	main( raw_data )
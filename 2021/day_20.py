'''
--- Day 20: Trench Map ---

With the scanners fully deployed, you turn their attention to mapping the floor of the ocean trench.

When you get back the image from the scanners, it seems to just be random noise. Perhaps you can combine an image enhancement algorithm and the input image (your puzzle input) to clean it up a little.

For example:

..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##
#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###
.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.
.#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....
.#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..
...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....
..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###

The first section is the image enhancement algorithm. It is normally given on a single line, but it has been wrapped to multiple lines in this example for legibility. The second section is the input image, a two-dimensional grid of light pixels (#) and dark pixels (.).

The image enhancement algorithm describes how to enhance an image by simultaneously converting all pixels in the input image into an output image. Each pixel of the output image is determined by looking at a 3x3 square of pixels centered on the corresponding input image pixel. So, to determine the value of the pixel at (5,10) in the output image, nine pixels from the input image need to be considered: (4,9), (4,10), (4,11), (5,9), (5,10), (5,11), (6,9), (6,10), and (6,11). These nine input pixels are combined into a single binary number that is used as an index in the image enhancement algorithm string.

For example, to determine the output pixel that corresponds to the very middle pixel of the input image, the nine pixels marked by [...] would need to be considered:

# . . # .
#[. . .].
#[# . .]#
.[. # .].
. . # # #

Starting from the top-left and reading across each row, these pixels are ..., then #.., then .#.; combining these forms ...#...#.. By turning dark pixels (.) into 0 and light pixels (#) into 1, the binary number 000100010 can be formed, which is 34 in decimal.

The image enhancement algorithm string is exactly 512 characters long, enough to match every possible 9-bit binary number. The first few characters of the string (numbered starting from zero) are as follows:

0         10        20        30  34    40        50        60        70
|         |         |         |   |     |         |         |         |
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##

In the middle of this first group of characters, the character at index 34 can be found: #. So, the output pixel in the center of the output image should be #, a light pixel.

This process can then be repeated to calculate every pixel of the output image.

Through advances in imaging technology, the images being operated on here are infinite in size. Every pixel of the infinite output image needs to be calculated exactly based on the relevant pixels of the input image. The small input image you have is only a small region of the actual infinite input image; the rest of the input image consists of dark pixels (.). For the purposes of the example, to save on space, only a portion of the infinite-sized input and output images will be shown.

The starting input image, therefore, looks something like this, with more dark pixels (.) extending forever in every direction not shown here:

...............
...............
...............
...............
...............
.....#..#......
.....#.........
.....##..#.....
.......#.......
.......###.....
...............
...............
...............
...............
...............

By applying the image enhancement algorithm to every pixel simultaneously, the following output image can be obtained:

...............
...............
...............
...............
.....##.##.....
....#..#.#.....
....##.#..#....
....####..#....
.....#..##.....
......##..#....
.......#.#.....
...............
...............
...............
...............

Through further advances in imaging technology, the above output image can also be used as an input image! This allows it to be enhanced a second time:

...............
...............
...............
..........#....
....#..#.#.....
...#.#...###...
...#...##.#....
...#.....#.#...
....#.#####....
.....#.#####...
......##.##....
.......###.....
...............
...............
...............

Truly incredible - now the small details are really starting to come through. After enhancing the original input image twice, 35 pixels are lit.

Start with the original input image and apply the image enhancement algorithm twice, being careful to account for the infinite size of the images. How many pixels are lit in the resulting image?

To begin, get your puzzle input.

'''

test_data = ['''..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##\
#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###\
.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.\
.#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....\
.#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..\
...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....\
..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#''',
			'',
			'#..#.',
			'#....',
			'##..#',
			'..#..',
			'..###'
			]

DEBUG = True


def create_row_padding( length, padding ):
	row_padding = [ ]

	for i in range( 0, padding ):
		row_data = ''
		for l in range( 0, length ):
			row_data += '.'
		row_padding.append( row_data )

	return row_padding


def create_width_padding( data, padding, right_only = False ):
	pad_data = ''
	new_data = [ ]

	for i in range( 0, padding ):
		pad_data += '.'

	if right_only:
		for datum in data:
			datum = datum + pad_data
			new_data.append( datum )

	else:
		for datum in data:
			datum = pad_data + datum + pad_data
			new_data.append( datum )

	return new_data


def draw( data ):
	num = 0
	for i in data:
		print( '{0:3} {1}'.format( num, i ) )
		num += 1


def pixels_to_binary( pixels ):
	result = ''

	for pixel in pixels:
		if pixel == '.':
			result += '0'

		elif pixel == '#':
			result += '1'

		else:
			raise AssertionError( 'Invalid pixel input! Received {0}. Expected . or #'.format( pixel ) )

	return result


def scan_pixel( img_enhancer, data, row_idx, col_idx ):

	a = data[ row_idx - 1 ][ col_idx - 1: col_idx + 2 ]
	b = data[ row_idx ][ col_idx - 1: col_idx + 2 ]
	c = data[ row_idx + 1 ][ col_idx - 1: col_idx + 2 ]

	# print( '{0}'.format( a ) )
	# print( '{0}'.format( b ) )
	# print( '{0}'.format( c ) )

	pixels = a + b + c
	pixel_num = pixels_to_binary( pixels )
	lookup_num = int( pixel_num, 2 )
	pixel = img_enhancer[ lookup_num ]

	# print( '{0}, {1}, {2}, pixel: {3}'.format( a, b, c, pixel ) )
	return pixel



def enhance_pixel( magic_num, img_enhancer, data, row_length ):
	new_data = data.copy( )

	# scan row
	for row_idx in range( magic_num, len( data ) - 1 - magic_num ):
		output = ''
		for col_idx in range( magic_num, row_length - magic_num ):
			pixel = data[ row_idx ][ col_idx ]

			# print pixel
			output += '{0}'.format( pixel )

			# process pixel
			new_pixel = scan_pixel( img_enhancer, data, row_idx, col_idx )

			# set pixel
			row_pixels = list( new_data[ row_idx ] )
			row_pixels[ col_idx ] = new_pixel
			new_data[ row_idx ] = ''.join( row_pixels )

		# print( '{0}'.format( output ) )

	if DEBUG:
		draw( new_data )
		print( 'enhanced_image\n' )

	return new_data

def count_lit_pixels( data ):
	return ''.join( data ).count( '#' )


def init_image_data( data, num_refinements = 0 ):
	image_data = [ ]
	row_length = len( data[ 0 ] )

	image_data = image_data + create_row_padding( row_length, num_refinements )
	image_data = image_data + data
	image_data = image_data + create_row_padding( row_length, num_refinements )
	image_data = create_width_padding( image_data, num_refinements )

	if DEBUG:
		draw( image_data )
		print( 'image_data\n' )

	return image_data


def parse_data( data ):
	img_enhancer = ''
	data = data

	img_enhancer = data.pop( 0 )
	data.pop( 0 )
	input_image = data

	if DEBUG:
		draw( data )
		print( 'data\n' )

	return img_enhancer, input_image


def main( data ):
	num_refinements = 2

	img_enhancer, img_data = parse_data( data )
	img_data = init_image_data( img_data, num_refinements )
	enhanced_image = enhance_pixel( 4, img_enhancer, img_data, len( img_data ) )
	# enhanced_image = create_width_padding( enhanced_image, 2, right_only = True )
	# enhanced_image = enhanced_image + create_row_padding( len( enhanced_image ) + 2, 1 )
	enhanced_image = enhance_pixel( 3, img_enhancer, enhanced_image, len( enhanced_image ) )
	# enhanced_image_2 = enhance_pixel( 0, img_enhancer, img_data_2, len( img_data_2 ) )


	if DEBUG:
		draw( enhanced_image )
		print( 'enhanced_image\n' )

	lit_pixels = count_lit_pixels( enhanced_image )
	print( 'There are {0} lit pixels in this image.'.format( lit_pixels ) )


if __name__ == "__main__":
	input = r'D:\Projects\Advent_of_Code\2021\day_20_input.txt'

	raw_data = [ ]

	with open( input, 'r' ) as input_file:
		raw_data = [ num.strip( ) for num in input_file.readlines( ) ]

	main( raw_data )

	#5117

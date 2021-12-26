'''
--- Day 23: Amphipod ---

A group of amphipods notice your fancy submarine and flag you down. "With such an impressive shell," one amphipod says, "surely you can help us with a question that has stumped our best scientists."

They go on to explain that a group of timid, stubborn amphipods live in a nearby burrow. Four types of amphipods live there: Amber (A), Bronze (B), Copper (C), and Desert (D). They live in a burrow that consists of a hallway and four side rooms. The side rooms are initially full of amphipods, and the hallway is initially empty.

They give you a diagram of the situation (your puzzle input), including locations of each amphipod (A, B, C, or D, each of which is occupying an otherwise open space), walls (#), and open space (.).

For example:

#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########

The amphipods would like a method to organize every amphipod into side rooms so that each side room contains one type of amphipod and the types are sorted A-D going left to right, like this:

#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #########

Amphipods can move up, down, left, or right so long as they are moving into an unoccupied open space. Each type of amphipod requires a different amount of energy to move one step: Amber amphipods require 1 energy per step, Bronze amphipods require 10 energy, Copper amphipods require 100, and Desert ones require 1000. The amphipods would like you to find a way to organize the amphipods that requires the least total energy.

However, because they are timid and stubborn, the amphipods have some extra rules:

    Amphipods will never stop on the space immediately outside any room. They can move into that space so long as they immediately continue moving. (Specifically, this refers to the four open spaces in the hallway that are directly above an amphipod starting position.)
    Amphipods will never move from the hallway into a room unless that room is their destination room and that room contains no amphipods which do not also have that room as their own destination. If an amphipod's starting room is not its destination room, it can stay in that room until it leaves the room. (For example, an Amber amphipod will not move from the hallway into the right three rooms, and will only move into the leftmost room if that room is empty or if it only contains other Amber amphipods.)
    Once an amphipod stops moving in the hallway, it will stay in that spot until it can move into a room. (That is, once any amphipod starts moving, any other amphipods currently in the hallway are locked in place and will not move again until they can move fully into a room.)

In the above example, the amphipods can be organized using a minimum of 12521 energy. One way to do this is shown below.

Starting configuration:

#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########

One Bronze amphipod moves into the hallway, taking 4 steps and using 40 energy:

#############
#...B.......#
###B#C#.#D###
  #A#D#C#A#
  #########

The only Copper amphipod not in its side room moves there, taking 4 steps and using 400 energy:

#############
#...B.......#
###B#.#C#D###
  #A#D#C#A#
  #########

A Desert amphipod moves out of the way, taking 3 steps and using 3000 energy, and then the Bronze amphipod takes its place, taking 3 steps and using 30 energy:

#############
#.....D.....#
###B#.#C#D###
  #A#B#C#A#
  #########

The leftmost Bronze amphipod moves to its room using 40 energy:

#############
#.....D.....#
###.#B#C#D###
  #A#B#C#A#
  #########

Both amphipods in the rightmost room move into the hallway, using 2003 energy in total:

#############
#.....D.D.A.#
###.#B#C#.###
  #A#B#C#.#
  #########

Both Desert amphipods move into the rightmost room using 7000 energy:

#############
#.........A.#
###.#B#C#D###
  #A#B#C#D#
  #########

Finally, the last Amber amphipod moves into its room, using 8 energy:

#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #########

What is the least energy required to organize the amphipods?

Your puzzle answer was 15338.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

As you prepare to give the amphipods your solution, you notice that the diagram they handed you was actually folded up. As you unfold it, you discover an extra part of the diagram.

Between the first and second lines of text that contain amphipod starting positions, insert the following lines:

  #D#C#B#A#
  #D#B#A#C#

So, the above example now becomes:

#############
#...........#
###B#C#B#D###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
  #########

The amphipods still want to be organized into rooms similar to before:

#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########

In this updated example, the least energy required to organize these amphipods is 44169:

#############
#...........#
###B#C#B#D###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
  #########

#############
#..........D#
###B#C#B#.###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
  #########

#############
#A.........D#
###B#C#B#.###
  #D#C#B#.#
  #D#B#A#C#
  #A#D#C#A#
  #########

#############
#A........BD#
###B#C#.#.###
  #D#C#B#.#
  #D#B#A#C#
  #A#D#C#A#
  #########

#############
#A......B.BD#
###B#C#.#.###
  #D#C#.#.#
  #D#B#A#C#
  #A#D#C#A#
  #########

#############
#AA.....B.BD#
###B#C#.#.###
  #D#C#.#.#
  #D#B#.#C#
  #A#D#C#A#
  #########

#############
#AA.....B.BD#
###B#.#.#.###
  #D#C#.#.#
  #D#B#C#C#
  #A#D#C#A#
  #########

#############
#AA.....B.BD#
###B#.#.#.###
  #D#.#C#.#
  #D#B#C#C#
  #A#D#C#A#
  #########

#############
#AA...B.B.BD#
###B#.#.#.###
  #D#.#C#.#
  #D#.#C#C#
  #A#D#C#A#
  #########

#############
#AA.D.B.B.BD#
###B#.#.#.###
  #D#.#C#.#
  #D#.#C#C#
  #A#.#C#A#
  #########

#############
#AA.D...B.BD#
###B#.#.#.###
  #D#.#C#.#
  #D#.#C#C#
  #A#B#C#A#
  #########

#############
#AA.D.....BD#
###B#.#.#.###
  #D#.#C#.#
  #D#B#C#C#
  #A#B#C#A#
  #########

#############
#AA.D......D#
###B#.#.#.###
  #D#B#C#.#
  #D#B#C#C#
  #A#B#C#A#
  #########

#############
#AA.D......D#
###B#.#C#.###
  #D#B#C#.#
  #D#B#C#.#
  #A#B#C#A#
  #########

#############
#AA.D.....AD#
###B#.#C#.###
  #D#B#C#.#
  #D#B#C#.#
  #A#B#C#.#
  #########

#############
#AA.......AD#
###B#.#C#.###
  #D#B#C#.#
  #D#B#C#.#
  #A#B#C#D#
  #########

#############
#AA.......AD#
###.#B#C#.###
  #D#B#C#.#
  #D#B#C#.#
  #A#B#C#D#
  #########

#############
#AA.......AD#
###.#B#C#.###
  #.#B#C#.#
  #D#B#C#D#
  #A#B#C#D#
  #########

#############
#AA.D.....AD#
###.#B#C#.###
  #.#B#C#.#
  #.#B#C#D#
  #A#B#C#D#
  #########

#############
#A..D.....AD#
###.#B#C#.###
  #.#B#C#.#
  #A#B#C#D#
  #A#B#C#D#
  #########

#############
#...D.....AD#
###.#B#C#.###
  #A#B#C#.#
  #A#B#C#D#
  #A#B#C#D#
  #########

#############
#.........AD#
###.#B#C#.###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########

#############
#..........D#
###A#B#C#.###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########

#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########

Using the initial configuration from the full diagram, what is the least energy required to organize the amphipods?

'''


test_data = [ ]


def main( data ):
	pass


if __name__ == "__main__":
	input = r'D:\Projects\Advent_of_Code\2021\day_23_input.txt'

	raw_data = [ ]

	with open( input, 'r' ) as input_file:
		raw_data = [ int( num ) for num in input_file.read( ).split( ) ]

	main( raw_data )

# Day 23.1 Solution
	#############      #############      #############      #############
	#...........#      #.........A.#      #.....B...A.#      #.A...B...A.#
	###D#B#C#A###      ###D#B#C#.###      ###D#.#C#.###      ###D#.#C#.###
	  #C#A#D#B#          #C#A#D#B#          #C#A#D#B#          #C#.#D#B#
	  #########          #########          #########          #########

#		2                  20                 5      27


	#############      #############      #############      #############
	#.A.......A.#      #.A.......A.#      #.A.......A.#      #.A...C...A.#
	###D#.#C#.###      ###D#B#C#.###      ###.#B#C#.###      ###.#B#.#.###
	  #C#B#D#B#          #C#B#D#.#          #C#B#D#D#          #C#B#D#D#
	  #########          #########          #########          #########

#		30                 70                9000               200     9300

	#############      #############      #############      #############      #############
	#.A...C...A.#      #.A.......A.#      #.A.......A.#      #.........A.#      #...........#
	###.#B#.#D###      ###.#B#.#D###      ###.#B#C#D###      ###.#B#C#D###      ###A#B#C#D###
	  #C#B#.#D#          #C#B#C#D#          #.#B#C#D#          #A#B#C#D#          #A#B#C#D#
	  #########          #########          #########          #########          #########

#		5000                300                700                 3                  8      15341

# Day 23.2 Solution
	#############      #############      #############      #############
	#...........#      #AA.........#      #AA.......BC#      #AA.......BC#
	###D#B#C#A###      ###D#B#C#.###      ###D#B#C#.###      ###.#B#C#.###
	  #D#C#B#A#          #D#C#B#.#          #D#C#B#.#          #.#C#B#D#
	  #D#B#A#C#          #D#B#A#C#          #D#B#A#.#          #.#B#A#D#
	  #C#A#D#B#          #C#A#D#B#          #C#A#D#.#          #C#A#D#D#
	  #########          #########          #########          #########

#                            18                550               33000

	#############      #############      #############      #############
	#AA.....C.BC#      #.......C.BC#      #.....B.C.BC#      #C....B.C.BC#
	###.#B#C#.###      ###.#B#C#.###      ###.#.#C#.###      ###.#.#C#.###
	  #.#C#B#D#          #.#C#B#D#          #.#C#B#D#          #.#.#B#D#
	  #.#B#A#D#          #A#B#A#D#          #A#B#A#D#          #A#B#A#D#
	  #.#A#D#D#          #A#A#D#D#          #A#A#D#D#          #A#A#D#D#
	  #########          #########          #########          #########

#        900                 10                 20                600

	#############      #############      #############      #############
	#CB...B.C.BC#      #CB...B.C.BC#      #C......C.BC#      #CC.....C.BC#
	###.#.#C#.###      ###.#.#C#.###      ###.#.#C#.###      ###.#.#.#.###
	  #.#.#B#D#          #A#.#B#D#          #A#.#B#D#          #A#.#B#D#
	  #A#.#A#D#          #A#.#A#D#          #A#B#A#D#          #A#B#A#D#
	  #A#A#D#D#          #A#.#D#D#          #A#B#D#D#          #A#B#D#D#
	  #########          #########          #########          #########

#         60                 8                 110                600

	#############      #############      #############      #############
	#CC.....C.BC#      #CC.....C.BC#      #CC...D.C.BC#      #CC...D...BC#
	###.#.#.#.###      ###A#.#.#.###      ###A#.#.#.###      ###A#.#.#.###
	  #A#B#.#D#          #A#B#.#D#          #A#B#.#D#          #A#B#.#D#
	  #A#B#A#D#          #A#B#.#D#          #A#B#.#D#          #A#B#.#D#
	  #A#B#D#D#          #A#B#D#D#          #A#B#.#D#          #A#B#C#D#
	  #########          #########          #########          #########

#         60                 8                5000                500

	#############      #############	#############
	#CC.......BC#      #CC........C#	#...........#
	###A#.#.#D###      ###A#B#.#D###	###A#B#C#D###
	  #A#B#.#D#          #A#B#.#D#  	  #A#B#C#D#
	  #A#B#.#D#          #A#B#.#D#  	  #A#B#C#D#
	  #A#B#C#D#          #A#B#C#D#  	  #A#B#C#D#
	  #########          #########  	  #########

#       4000                 60              2100

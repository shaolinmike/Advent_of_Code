'''
--- Day 5: Binary Boarding ---

You board your plane only to discover a new problem: you dropped your
boarding pass! You aren't sure which seat is yours, and all of the flight
attendants are busy with the flood of people that suddenly made it through
passport control.

You write a quick program to use your phone's camera to scan all of the
nearby boarding passes (your puzzle input); perhaps you can find your seat
through process of elimination.

Instead of zones or groups, this airline uses binary space partitioning to
seat people. A seat might be specified like FBFBBFFRLR, where F means
"front", B means "back", L means "left", and R means "right".

The first 7 characters will either be F or B; these specify exactly one of
the 128 rows on the plane (numbered 0 through 127). Each letter tells you
which half of a region the given seat is in. Start with the whole list of
rows; the first letter indicates whether the seat is in the front (0
through 63) or the back (64 through 127). The next letter indicates which
half of that region the seat is in, and so on until you're left with
exactly one row.

For example, consider just the first seven characters of FBFBBFFRLR:

    Start by considering the whole range, rows 0 through 127.
    F means to take the lower half, keeping rows 0 through 63.
    B means to take the upper half, keeping rows 32 through 63.
    F means to take the lower half, keeping rows 32 through 47.
    B means to take the upper half, keeping rows 40 through 47.
    B keeps rows 44 through 47.
    F keeps rows 44 through 45.
    The final F keeps the lower of the two, row 44.

The last three characters will be either L or R; these specify exactly one
of the 8 columns of seats on the plane (numbered 0 through 7). The same
process as above proceeds again, this time with only three steps. L means
to keep the lower half, while R means to keep the upper half.

For example, consider just the last 3 characters of FBFBBFFRLR:

    Start by considering the whole range, columns 0 through 7.
    R means to take the upper half, keeping columns 4 through 7.
    L means to take the lower half, keeping columns 4 through 5.
    The final R keeps the upper of the two, column 5.

So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

Every seat also has a unique seat ID: multiply the row by 8, then add the
column. In this example, the seat has ID 44 * 8 + 5 = 357.

Here are some other boarding passes:

    BFFFBBFRRR: row 70, column 7, seat ID 567.
    FFFBBBFRRR: row 14, column 7, seat ID 119.
    BBFFBBFRLL: row 102, column 4, seat ID 820.

As a sanity check, look through your list of boarding passes. What is the
highest seat ID on a boarding pass?

Your puzzle answer was 908.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

Ding! The "fasten seat belt" signs have turned on. Time to find your seat.

It's a completely full flight, so your seat should be the only missing
boarding pass in your list. However, there's a catch: some of the seats at
the very front and back of the plane don't exist on this aircraft, so
they'll be missing from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1
and -1 from yours will be in your list.

What is the ID of your seat?

Your puzzle answer was 619.

Both parts of this puzzle are complete! They provide two gold stars: **

'''

import bisect

test_data_1 = ['FBFBBFFRLR']
test_data_2 = ['BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']

NUM_ROWS = 128
NUM_SEATS = 8


def lookup_seat(lookup_val, boarding_pass, seating_section):
    idx_high = len(seating_section)
    idx_low = 0
    idx_mid = 0

    for step in boarding_pass:
        if step  == lookup_val[0]:
            idx_mid = bisect.bisect_left(seating_section, seating_section[int((idx_high + idx_low) / 2)], lo = idx_low, hi = idx_high)
            idx_high = idx_mid
        elif step == lookup_val[1]:
            idx_mid = bisect.bisect_left( seating_section, seating_section[int((idx_high + idx_low) / 2)], lo = idx_low, hi = idx_high)
            idx_low = idx_mid

    return idx_low


def generate_seating_list(data):
    result = {}

    for boarding_pass in data:
        row_num = 0
        seat_num = 0

        rows = list(range(0, NUM_ROWS))
        seats = list(range(0, NUM_SEATS))

        row_pass = boarding_pass[:7]
        seat_pass = boarding_pass[7:]

        row_num = lookup_seat('FB', row_pass, rows)
        seat_num = lookup_seat('LR', seat_pass, seats)
        seat_id = row_num * NUM_SEATS + seat_num
        result[seat_id] = boarding_pass

    return result


def main(data, part_two = False):
    result = 0
    seating_list = {}

    seating_list = generate_seating_list(data)

    if not part_two:
        print(f'Highest assigned seat number: {sorted(seating_list.keys())[-1]}')
    else:
        total_seats = [x for x in sorted(seating_list.keys())]
        result = [x for x in range(total_seats[0], total_seats[-1]) if x not in total_seats][0]
        print(f'My seat number: {result}')



if __name__ == "__main__":
    filename = __file__.split('\\')[-1].split('.')[0]
    input = rf"D:\Projects\Advent_of_Code\2020\{filename}_input.txt"
    raw_data = []

    with open(input, 'r') as input_file:
        raw_data = [line.strip() for line in input_file.readlines()]

    main(raw_data)
    main(raw_data, part_two = True)
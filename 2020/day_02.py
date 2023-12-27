'''
--- Day 2: Password Philosophy ---

Your flight departs in a few days from the coastal airport; the easiest way
down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day.
"Something's wrong with our computers; we can't log in!" You ask if you can
take a look.

Their password database seems to be a little corrupted: some of the
passwords wouldn't have been allowed by the Official Toboggan Corporate
Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input)
of passwords (according to the corrupted database) and the corporate policy
when that password was set.

For example, suppose you have the following list:

    1-3 a: abcde
    1-3 b: cdefg
    2-9 c: ccccccccc

Each line gives the password policy and then the password. The password
policy indicates the lowest and highest number of times a given letter must
appear for the password to be valid. For example, 1-3 a means that the
password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is
not; it contains no instances of b, but needs at least 1. The first and
third passwords are valid: they contain one a or nine c, both within the
limits of their respective policies.

How many passwords are valid according to their policies?

Your puzzle answer was 515.

--- Part Two ---

While it appears you validated the passwords correctly, they don't seem to
be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the
password policy rules from his old job at the sled rental place down the
street! The Official Toboggan Corporate Policy actually works a little
differently.

Each policy actually describes two positions in the password, where 1 means
the first character, 2 means the second character, and so on. (Be careful;
Toboggan Corporate Policies have no concept of "index zero"!) Exactly one
of these positions must contain the given letter. Other occurrences of the
letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

    1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

How many passwords are valid according to the new interpretation of the
policies?

Your puzzle answer was 711.

Both parts of this puzzle are complete! They provide two gold stars: **
'''

def check_password(data, part_two = False):
    results = []

    for datum in data:
        is_valid = False

        password = datum[1]
        password_key = datum[0][0]
        valid_indexes = datum[0][1]

        # Rental password policy
        if not part_two:
            hits = password.count(password_key)
            if valid_indexes[0] <= hits <= valid_indexes[1]:
                results.append((datum, True))

        # Toboggan password policy
        else:
            for idx in valid_indexes:
                idx_base0 = idx - 1

                if idx_base0 > len(password):
                    is_valid = False

                # Set validity, depending on how many times the password key is found
                else:
                    if password[idx_base0] == password_key:
                        is_valid = not is_valid

        if is_valid:
            results.append((datum, is_valid))

    return results


def parse_data(raw_data):
    data = []

    for datum in raw_data:
        password = datum[1]
        result, pwd_key = datum[0].split()
        pwd_rules = list(map(int, result.split('-')))
        data.append([[pwd_key, pwd_rules], password])

    return data


def main(raw_data, part_two = False):
    data = parse_data(raw_data)
    result = []

    if not part_two:
        result = check_password(data)
    else:
        result = check_password(data, part_two = part_two)

    print(f'{len(result)} passwords are valid')



if __name__ == "__main__":
    filename = __file__.split('\\')[-1].split('.')[0]
    input = rf"D:\Projects\Advent_of_Code\2020\{filename}_input.txt"
    raw_data = []

    with open(input, 'r') as input_file:
        raw_data = [x.strip().split(': ') for x in input_file.readlines()]

    main(raw_data)
    main(raw_data, part_two = True)
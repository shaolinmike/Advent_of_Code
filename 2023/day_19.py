#! python3.11
"""
--- Day 19: Aplenty ---
The Elves of Gear Island are thankful for your help and send you on your
way. They even have a hang glider that someone stole from Desert Island;
since you're already going that direction, it would help them a lot if you
would use it to get down there and return it to them.

As you reach the bottom of the relentless avalanche of machine parts, you
discover that they're already forming a formidable heap. Don't worry,
though - a group of Elves is already here organizing the parts, and they
have a system.

To start, each part is rated in each of four categories:

x: Extremely cool looking
m: Musical (it makes a noise when you hit it)
a: Aerodynamic
s: Shiny

Then, each part is sent through a series of workflows that will ultimately
accept or reject the part. Each workflow has a name and contains a list of
rules; each rule specifies a condition and where to send the part if the
condition is true. The first rule that matches the part being considered is
applied immediately, and the part moves on to the destination described by
the rule. (The last rule in each workflow has no condition and always
applies if reached.)

Consider the workflow ex{x>10:one,m<20:two,a>30:R,A}. This workflow is
named ex and contains four rules. If workflow ex were considering a
specific part, it would perform the following steps in order:

    Rule "x>10:one": If the part's x is more than 10, send the part to the
    workflow named one.
    Rule "m<20:two": Otherwise, if the part's m is less than 20, send the
    part to the workflow named two.
    Rule "a>30:R": Otherwise, if the part's a is more than 30, the part is
    immediately rejected (R).
    Rule "A": Otherwise, because no other rules matched the part, the part
    is immediately accepted (A).

If a part is sent to another workflow, it immediately switches to the start
of that workflow instead and never returns. If a part is accepted (sent to
A) or rejected (sent to R), the part immediately stops any further
processing.

The system works, but it's not keeping up with the torrent of weird metal
shapes. The Elves ask if you can help sort a few parts and give you the
list of workflows and some part ratings (your puzzle input). For example:

px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
The workflows are listed first, followed by a blank line, then the ratings
of the parts the Elves would like you to sort. All parts begin in the
workflow named in. In this example, the five listed parts go through the
following workflows:

{x=787,m=2655,a=1222,s=2876}: in -> qqz -> qs -> lnx -> A
{x=1679,m=44,a=2067,s=496}: in -> px -> rfg -> gd -> R
{x=2036,m=264,a=79,s=2244}: in -> qqz -> hdj -> pv -> A
{x=2461,m=1339,a=466,s=291}: in -> px -> qkq -> crn -> R
{x=2127,m=1623,a=2188,s=1013}: in -> px -> rfg -> A

Ultimately, three parts are accepted. Adding up the x, m, a, and s rating
for each of the accepted parts gives 7540 for the part with x=787, 4623 for
the part with x=2036, and 6951 for the part with x=2127. Adding all of the
ratings for all of the accepted parts gives the sum total of 19114.

Sort through all of the parts you've been given; what do you get if you add
together all of the rating numbers for all of the parts that ultimately get
accepted?

Your puzzle answer was 376008.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
Even with your help, the sorting process still isn't fast enough.

One of the Elves comes up with a new plan: rather than sort parts
individually through all of these workflows, maybe you can figure out in
advance which combinations of ratings will be accepted or rejected.

Each of the four ratings (x, m, a, s) can have an integer value ranging
from a minimum of 1 to a maximum of 4000. Of all possible distinct
combinations of ratings, your job is to figure out which ones will be
accepted.

In the above example, there are 167409079868000 distinct combinations of
ratings that will be accepted.

Consider only your list of workflows; the list of part ratings that the
Elves wanted you to sort is no longer relevant. How many distinct
combinations of ratings will be accepted by the Elves' workflows?

"""

TEST_DATA = [ 'px{a<2006:qkq,m>2090:A,rfg}',
              'pv{a>1716:R,A}',
              'lnx{m>1548:A,A}',
              'rfg{s<537:gd,x>2440:R,A}',
              'qs{s>3448:A,lnx}',
              'qkq{x<1416:A,crn}',
              'crn{x>2662:A,R}',
              'in{s<1351:px,qqz}',
              'qqz{s>2770:qs,m<1801:hdj,R}',
              'gd{a>3333:R,R}',
              'hdj{m>838:A,pv}',
              '',
              '{x=787,m=2655,a=1222,s=2876}',
              '{x=1679,m=44,a=2067,s=496}',
              '{x=2036,m=264,a=79,s=2244}',
              '{x=2461,m=1339,a=466,s=291}',
              '{x=2127,m=1623,a=2188,s=1013}'
            ]



class Xmas_Part():

    def __init__(self, id, x=0, m=0, a=0, s=0):
        self.id = id
        self.x = x
        self.m = m
        self.a = a
        self.s = s

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.id} ({self.m},{self.a})>"

    def __str__(self):
        return f"<{self.__class__.__name__} {self.id} ({self.m},\n\t\t\t\t{self.a})>"


class Sorter_Workflow():

    def __init__(self, id, instructions):
        self.id = id
        self.instructions = instructions
        self.x = 0
        self.m = 0
        self.a = 0
        self.s = 0

    def sort_parts(self, part):
        part_values = {}

        for p in part:
            exec(p,globals(),part_values)

        self.x = part_values['x']
        self.m = part_values['m']
        self.a = part_values['a']
        self.s = part_values['s']



def parse_data(raw_data):
    raw_data = [x.rstrip('}') for x in raw_data]
    data = []
    workflows = {}
    parts = []


    workflows_processed = False

    for datum in raw_data:
        if datum == '':
            workflows_processed = True

        else:
            if not workflows_processed:
                id, instructions = datum.split('{')
                workflow = instructions.split(',')
                workflows[id] = workflow
            else:
                part = datum.strip('{').split(',')
                parts.append(part)

    return workflows, parts


def _process_part(start_workflow, part_data, workflow_data):
    part_values = {}
    result = 0


    # Initialize the part values
    for datum in part_data:
        exec(datum,globals(),part_values)

    workflow_steps = workflow_data[start_workflow]
    for step in workflow_steps:
        sub_steps = step.split(':')

        # Process condition-less instruction or Acceptance/Rejection
        if len(sub_steps) == 1:
            if sub_steps[0] not in ['A', 'R']:
                return _process_part(sub_steps[0], part_data, workflow_data)
            elif sub_steps[0] == 'A':
                return sum([part_values[key] for key in part_values.keys()])
            else:
                return # Reject this part and don't return an aggregate part value

        # if condition, then action
        else:
            x = part_values['x']
            m = part_values['m']
            a = part_values['a']
            s = part_values['s']

            condition, action = sub_steps[0], sub_steps[1]
            if eval(condition):
                if action not in ['A', 'R']:
                    return _process_part(sub_steps[1], part_data, workflow_data)
                else:
                    if action == 'A':
                        return sum([part_values[key] for key in part_values.keys()])
                    else:
                        return # Reject this part and don't return an aggregate part value


def process_parts(workflows, parts):
    results = []

    for part in parts:
        result =  _process_part('in', part, workflows)
        if result:
            results.append(result)

    return results


def main(raw_data, part_two = False):
    workflows, parts = parse_data(raw_data)
    results = process_parts(workflows, parts)

    if not part_two:
        print(f'\nThe sum of all the rating numbers for the accepted parts is {sum(results)}')
    else:
        print(f'\nThe numbers is {min([x[0] for x in result])}')



if __name__ == "__main__":
    input = r"D:\Projects\Advent_of_Code\2023\day_19_input.txt"
    raw_data = []

    with open(input, "r") as input_file:
        raw_data = [line.rstrip() for line in input_file.readlines( )]

    # main(TEST_DATA)
    main(raw_data)
    # main(TEST_DATA, part_two = True)
    # main(raw_data, part_two = True)

from collections import deque

# do the thing
input = open('input', 'r')
lines = input.readlines()

# separate crates and instructions
crates = []
instructions = []
instr = False
for each in lines:
    # empty line indicates we are moving to instructions
    if each.strip() == "":
        instr = True
        continue
    if instr:
        instructions.append(each.strip())
    else:
        crates.append(each.strip('\n'))

# rearrange crates to a list of lists
# left-to-right, top-to-bottom
count = int(crates[-1].split()[-1])
# init empty stacks
stacks = []
for i in range(count):
    stacks.append([])
# iterate through lines, fill stacks in
for each in crates:
    i = 0
    stack = 0
    while i < len(each):
        contents = each[i:i + 4].strip(' []')
        if contents:
            stacks[stack].append(contents)
        i += 4
        stack += 1
# deque the stacks, remove last element from each since that's the index
for i in range(len(stacks)):
    stacks[i] = deque(stacks[i][:-1])

# do the operations
for each in instructions:
    # extract #s
    each = each.split()
    count = int(each[1])
    src = int(each[3]) - 1
    dest = int(each[5]) - 1

    # move stuff
    for i in range(count):
        item = stacks[src].popleft()
        stacks[dest].appendleft(item)

# get solution for part 1
solution = ""
for each in stacks:
    solution += each[0]
print(solution)

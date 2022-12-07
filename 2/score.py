# disclaimer: yes i could do more logic but that's boring, just a bunch of comparisons

# map tuples to result for latter player
scores = {
    ('A', 'X'): 4,
    ('A', 'Y'): 8,
    ('A', 'Z'): 3,
    ('B', 'X'): 1,
    ('B', 'Y'): 5,
    ('B', 'Z'): 9,
    ('C', 'X'): 7,
    ('C', 'Y'): 2,
    ('C', 'Z'): 6
}

# do the thing
input = open('input', 'r')
lines = input.readlines()

# Part 1
score = 0
for each in lines:
    them, me = each.split()
    score += scores[(them, me)]
print(score)

# Part 2
scores = {
    ('A', 'X'): 3,
    ('A', 'Y'): 4,
    ('A', 'Z'): 8,
    ('B', 'X'): 1,
    ('B', 'Y'): 5,
    ('B', 'Z'): 9,
    ('C', 'X'): 2,
    ('C', 'Y'): 6,
    ('C', 'Z'): 7
}

score = 0
for each in lines:
    them, me = each.split()
    score += scores[(them, me)]
print(score)

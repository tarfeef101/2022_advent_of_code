# do the thing
input = open('input', 'r')
lines = input.readlines()

# part 1
bad_pairs = 0
for each in lines:
    each = each.strip()
    a, b = each.split(',')
    a = a.split('-')
    b = b.split('-')
    a = set(list(range(int(a[0]), int(a[1]) + 1)))
    b = set(list(range(int(b[0]), int(b[1]) + 1)))
    if a <= b or b <= a:
        bad_pairs += 1

print(bad_pairs)

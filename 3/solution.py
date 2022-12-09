# get value of chars
def value(char):
    val = ord(char)
    if val > 90 :
        return val - 96
    return val - 38

# do the thing
input = open('input', 'r')
lines = input.readlines()

# part 1
sum = 0
for each in lines:
    each = each.strip()
    a = set(each[0:int(len(each) / 2)])
    b = set(each[int(len(each) / 2):])
    sum += value(list(a.intersection(b))[0])

print(sum)

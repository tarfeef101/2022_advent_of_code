# do the thing
input = open('input', 'r')
lines = input.readlines()
line = lines[0].strip()

# go through the chars
for i in range(len(line)):
    chars = line[i:i+4]
    if len(set(chars)) == 4:
        print(str(i + 1))
        break

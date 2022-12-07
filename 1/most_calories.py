import heapq

input = open('input', 'r')
lines = input.readlines()
elves = [] # heap

elf = 0 # current elf
for each in lines:
    # remove \n
    line = each.strip('\n') # remove \n
    
    # if this is a number
    if line:
        # minus because min heap things
        elf -= int(line)
    # end of current elf, push to heap
    else:
        heapq.heappush(elves, elf)
        elf = 0
heapq.heappush(elves, elf)

# PART 1 ANSWER
# print top of heap, inverted
#print(str(0 - elves[0]))

answer = 0
for i in range(3):
    answer -= heapq.heappop(elves)
print(answer)

from collections import deque

# do the thing
input = open('input', 'r')
lines = input.readlines()

# iterate through lines, build tree
tree = {}
posn = deque()
for each in lines:
    each = each.split()
    
    # command
    if each[0] == '$':
        # cd
        if each[1] = 'cd':
            # went to root
            if each[2] == '/':
                posn.clear()
                continue
            # up 1 level
            elif each[2] == '..':
                posn.pop()
            # we need to go deeper!
            else:
                posn.append(each[2])
                # add the dir if we haven't mapped it already
                dic = tree
                for each in posn:
                    if each in dic:
                        dic = dic[each]
                        continue
                    else:
                        for each2 in posn:


        # ls
        else:
            next
    # dir
    elif each[0] == 'dir':
        next
    # file
    else:
        next
    break

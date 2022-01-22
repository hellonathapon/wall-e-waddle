import re
import sys

def walking(str):
    x = 0
    y = 0
    facing_dir = 0
    directions = ['North', 'South', 'East', 'West']
    cmd_str = re.sub(r'([W|R|L])(?!$)', r',\1', str) # regex = insert comma in front of W|R|L chars.
    cmd_lst = cmd_str.split(",")                     # split each commands into list
    cmd_lst.pop(0)                                   # pop out the fist index which is an extra comma
    
    for cmd in cmd_lst:
        if 'W' in cmd:
            n = int(cmd[1:])    # slicing W char and parse the rest to int
            if facing_dir == 0: # moves either x or y accordingly to its coordinate planes
                y += n
            elif facing_dir == 1:
                x += n
            elif facing_dir == 2:
                y -= n
            elif facing_dir == 3:
                x -= n
        elif cmd == 'R':
            if facing_dir == 3:
                facing_dir = 0
            elif facing_dir == 0:
                facing_dir += 1
            elif facing_dir == 1:
                facing_dir += 1
            else:
                facing_dir += 1
        elif cmd == 'L':
            if facing_dir == 0:
                facing_dir = 3
            elif facing_dir == 3:
                facing_dir -= 1
            elif facing_dir == 2:
                facing_dir -= 1
            else:
                facing_dir -= 1
    return 'X: {} Y: {} Direction: {}'.format(x,y,directions[facing_dir])

print(walking(sys.argv[1]))
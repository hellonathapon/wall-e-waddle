import re

def foo(str):
    cmd_str = re.sub(r'([W|R|L])(?!$)', r',\1', str) # regex = insert comma in front of W|R|L chars.
    cmd_lst = cmd_str.split(",")                     # split each commands into list
    cmd_lst.pop(0)                                   # pop out the fist index which is an extra comma
    
    return cmd_lst

print(foo("W3RW2LLRRLRLRW34W67"))
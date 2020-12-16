#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: wws
import sys

OPRATIONS = ['-', '&', '|', '^', '<', '>', '>=', '<=', '==', '(' ,')']
HELP_INFO = '''
Compared files with through python set operations.

Support operations:
    &   intersection
    |   union
    -   difference
    ^   symmetric difference
    <   Test whether the set is a proper subset of other, that is, set <= other and set != other.
    <=  Test whether every element in the set is in other.
    >   Test whether every element in the set is in other.
    >=  Test whether every element in other is in the set.

Features:
    1. Auto strip space for each line in file.
    2. Auto sorted the result.

Examples:
    1. compared from files
        setop fpath1 - fpath2
        setop 'fpath1 & fpath2'
        setop '( fpath1 & fpath2 ) <= fpath3'

    2. compared from variables
    fish
        ❯ setop  (seq 1 3|psub) '&' (seq 2 4|psub)
            2
            3
    bash
        ❯ setop  <(seq 1 3) '&' <(seq 2 4)
            2
            3 
'''


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ['-h', '--help']:
        print(HELP_INFO)
        return
    set_map = dict()
    argv = sum([i.split() for i in sys.argv[1:]], [])
    for i in argv:
        if i not in OPRATIONS:
            with open(i) as f:
                set_map[i] = {line.strip()
                            for line in f.read().splitlines() if line}
    cmd = ' '.join(
        [i if i in OPRATIONS else f'set_map["{i}"]' for i in argv])
    
    result = eval(cmd)
    if isinstance(result, set):
        for i in sorted(list(result)):
            print(i)
    else:
        print(result)


if __name__ == "__main__":
    main()


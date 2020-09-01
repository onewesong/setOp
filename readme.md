# Introduction
```
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
        set_operator.py fpath1 - fpath2
        set_operator.py 'fpath1 & fpath2'
        set_operator.py '( fpath1 & fpath2 ) <= fpath3'

    2. compared from variables
    fish
        ❯ set_operator.py  (seq 1 3|psub) '&' (seq 2 4|psub)
            2
            3
    bash
        ❯ set_operator.py  <(seq 1 3) '&' <(seq 2 4)
            2
            3 
```


# Install
```
bash -c 'curl https://raw.githubusercontent.com/onewesong/setOp/master/set_operator.py  -o /usr/local/bin/set_operator.py && chmod +x /usr/local/bin/set_operator.py && set_operator.py -h'
```
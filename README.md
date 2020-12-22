CFG is a library for working with context free grammars (CFG) in [Python](https://www.python.org/).

## Using library
CFG library is in `cfg.py` module and can be imported and be used easily. For example:
```Python
from cfg import CFG

grammar = CFG(variables={'S'},
              terminals={'a', 'b', 'c', 'λ'},
              start_variable='S',
              null_character='λ',
              rules={('S', 'aSa'),
                     ('S', 'bSb'),
                     ('S', 'cSc'),
                     ('S', 'λ')})

string = input("Enter a string: ")

if grammar.cyk(string):
    print("Grammar can generate the string!")
else:
    print("Grammar cannot generate the string!")
```
Above program gets a string from input and tells if the defined grammer can generate the string or not.
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

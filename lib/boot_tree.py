stree = ['And',
 ['rule',
  ['rule_name', 'grammar'],
  ['flags'],
  ['args'],
  ['and',
   ['output', ['quantified', ['apply', 'rule'], ['quantifier', '*']]],
   ['apply', 'spaces']]],]
tree = ['And',
 ['rule',
  ['rule_name', 'name'],
  ['flags'],
  ['args'],
  ['and',
   ['or', ['apply', 'letter'], ['exactly', '_']],
   ['quantified',
    ['or', ['apply', 'letter'], ['apply', 'digit'], ['exactly', '_']],
    ['quantifier', '*']]]],
 ['rule',
  ['rule_name', 'expr'],
  ['flags'],
  ['args'],
  ['or',
   ['apply', 'apply'],
   ['apply', 'exactly'],
   ['apply', 'token'],
   ['apply', 'parenthesis'],
   ['apply', 'output']]],
 ['rule',
  ['rule_name', 'exactly'],
  ['flags', '!'],
  ['args'],
  ['and',
   ['token', "'"],
   ['output',
    ['quantified',
     ['or',
      ['apply', 'escaped_char'],
      ['and', ['negation', ['exactly', "'"]], ['apply', 'anything']]],
     ['quantifier', '*']]],
   ['token', "'"]]],
 ['rule',
  ['rule_name', 'token'],
  ['flags', '!'],
  ['args'],
  ['and',
   ['token', '"'],
   ['output',
    ['quantified',
     ['or',
      ['apply', 'escaped_char'],
      ['and', ['negation', ['exactly', '"']], ['apply', 'anything']]],
     ['quantifier', '*']]],
   ['token', '"']]],
 ['rule',
  ['rule_name', 'escaped_char'],
  ['flags', '!'],
  ['args'],
  ['and',
   ['exactly', '\\'],
   ['output',
    ['or',
     ['exactly', 'n'],
     ['exactly', 'r'],
     ['exactly', 't'],
     ['exactly', 'b'],
     ['exactly', 'f'],
     ['exactly', '"'],
     ['exactly', "'"],
     ['exactly', '\\']]]]],
 ['rule',
  ['rule_name', 'apply'],
  ['flags', '!'],
  ['args'],
  ['and',
   ['quantified',
    ['or', ['exactly', '\t'], ['exactly', ' ']],
    ['quantifier', '*']],
   ['output', ['apply', 'name']]]],
 ['rule',
  ['rule_name', 'parenthesis'],
  ['flags'],
  ['args'],
  ['and', ['token', '('], ['output', ['apply', 'or']], ['token', ')']]],
 ['rule',
  ['rule_name', 'output'],
  ['flags', '!'],
  ['args'],
  ['and', ['token', '{'], ['output', ['apply', 'or']], ['token', '}']]],
 ['rule',
  ['rule_name', 'not'],
  ['flags'],
  ['args'],
  ['or',
   ['and',
    ['token', '~'],
    ['output', ['bound', ['apply', 'expr'], ['inline', 'negation']]]],
   ['apply', 'expr']]],
 ['rule',
  ['rule_name', 'quantified'],
  ['flags'],
  ['args'],
  ['and',
   ['apply', 'not'],
   ['quantified',
    ['bound',
     ['or', ['exactly', '*'], ['exactly', '+'], ['exactly', '?']],
     ['inline', 'quantifier']],
    ['quantifier', '?']]]],
 ['rule',
  ['rule_name', 'bound'],
  ['flags'],
  ['args'],
  ['and',
   ['apply', 'quantified'],
   ['quantified',
    ['and',
     ['exactly', '='],
     ['output', ['bound', ['apply', 'name'], ['inline', 'inline']]]],
    ['quantifier', '?']]]],
 ['rule',
  ['rule_name', 'and'],
  ['flags'],
  ['args'],
  ['quantified', ['apply', 'bound'], ['quantifier', '*']]],
 ['rule',
  ['rule_name', 'or'],
  ['flags'],
  ['args'],
  ['and',
   ['apply', 'and'],
   ['quantified',
    ['and', ['token', '|'], ['output', ['apply', 'and']]],
    ['quantifier', '*']]]],
 ['rule',
  ['rule_name', 'rule'],
  ['flags'],
  ['args'],
  ['and',
   ['apply', 'spaces'],
   ['output',
    ['and',
     ['bound', ['apply', 'name'], ['inline', 'rule_name']],
     ['bound',
      ['quantified', ['exactly', '!'], ['quantifier', '?']],
      ['inline', 'flags']],
     ['bound', ['apply', 'and'], ['inline', 'args']],
     ['and', ['token', '='], ['output', ['apply', 'or']]]]]]],
 ['rule',
  ['rule_name', 'grammar'],
  ['flags'],
  ['args'],
  ['and',
   ['output', ['quantified', ['apply', 'rule'], ['quantifier', '*']]],
   ['apply', 'spaces']]],
 ['rule',
  ['rule_name', 'letter'],
  ['flags'],
  ['args'],
  ['or',
   ['exactly', 'a'],
   ['exactly', 'b'],
   ['exactly', 'c'],
   ['exactly', 'd'],
   ['exactly', 'e'],
   ['exactly', 'f'],
   ['exactly', 'g'],
   ['exactly', 'h'],
   ['exactly', 'i'],
   ['exactly', 'j'],
   ['exactly', 'k'],
   ['exactly', 'l'],
   ['exactly', 'm'],
   ['exactly', 'n'],
   ['exactly', 'o'],
   ['exactly', 'p'],
   ['exactly', 'q'],
   ['exactly', 'r'],
   ['exactly', 's'],
   ['exactly', 't'],
   ['exactly', 'u'],
   ['exactly', 'v'],
   ['exactly', 'w'],
   ['exactly', 'x'],
   ['exactly', 'y'],
   ['exactly', 'z'],
   ['exactly', 'A'],
   ['exactly', 'B'],
   ['exactly', 'C'],
   ['exactly', 'D'],
   ['exactly', 'E'],
   ['exactly', 'F'],
   ['exactly', 'G'],
   ['exactly', 'H'],
   ['exactly', 'I'],
   ['exactly', 'J'],
   ['exactly', 'K'],
   ['exactly', 'L'],
   ['exactly', 'M'],
   ['exactly', 'N'],
   ['exactly', 'O'],
   ['exactly', 'P'],
   ['exactly', 'Q'],
   ['exactly', 'R'],
   ['exactly', 'S'],
   ['exactly', 'T'],
   ['exactly', 'U'],
   ['exactly', 'V'],
   ['exactly', 'W'],
   ['exactly', 'X'],
   ['exactly', 'Y'],
   ['exactly', 'Z']]],
 ['rule',
  ['rule_name', 'digit'],
  ['flags'],
  ['args'],
  ['or',
   ['exactly', '0'],
   ['exactly', '1'],
   ['exactly', '2'],
   ['exactly', '3'],
   ['exactly', '4'],
   ['exactly', '5'],
   ['exactly', '6'],
   ['exactly', '7'],
   ['exactly', '8'],
   ['exactly', '9']]],
 ['rule',
  ['rule_name', 'space'],
  ['flags'],
  ['args'],
  ['or',
   ['exactly', '\t'],
   ['exactly', '\n'],
   ['exactly', '\r'],
   ['exactly', ' ']]],
 ['rule',
  ['rule_name', 'spaces'],
  ['flags'],
  ['args'],
  ['quantified', ['apply', 'space'], ['quantifier', '*']]]]
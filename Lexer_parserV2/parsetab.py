
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'NUMBER PLUS TIMES MINUS DIVIDEexpression : expression term PLUSexpression : termterm : term factor TIMESterm : term factor DIVIDEterm : factorfactor : NUMBER'
    
_lr_action_items = {'DIVIDE':([2,5,],[-6,8,]),'TIMES':([2,5,],[-6,7,]),'PLUS':([2,3,6,7,8,],[-6,-5,9,-3,-4,]),'NUMBER':([0,1,2,3,4,6,7,8,9,],[2,2,-6,-5,2,2,-3,-4,-1,]),'$end':([1,2,3,4,7,8,9,],[-2,-6,-5,0,-3,-4,-1,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'term':([0,4,],[1,6,]),'expression':([0,],[4,]),'factor':([0,1,4,6,],[3,5,3,5,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression term PLUS','expression',3,'p_expression_plus','parser_rules.py',5),
  ('expression -> term','expression',1,'p_expression_term','parser_rules.py',9),
  ('term -> term factor TIMES','term',3,'p_term_times','parser_rules.py',13),
  ('term -> term factor DIVIDE','term',3,'p_term_divide','parser_rules.py',22),
  ('term -> factor','term',1,'p_term_factor','parser_rules.py',26),
  ('factor -> NUMBER','factor',1,'p_factor_num','parser_rules.py',30),
]

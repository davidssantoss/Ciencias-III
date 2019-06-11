from lexer_rules import tokens
from expressions import *

def p_expression_plus(subexpr):
    'expression : expression term PLUS'
    subexpr[0] = subexpr[1] + subexpr[2]

def p_expression_term(subexpr):
    'expression : term'
    subexpr[0] = subexpr[1]

def p_term_times(subexpr):
    'term : term factor TIMES'
    subexpr[0] = subexpr[1] * subexpr[2]

def p_expression_minus(subexpr):
    print(subexpr)
    'expression : expression term MINUS'
    subexpr[0] = subexpr[1] - subexpr[2]

def p_term_divide(subexpr):
    'term : term factor DIVIDE'
    subexpr[0] = subexpr[1] / subexpr[2]

def p_term_factor(subexpr):
    'term : factor'
    subexpr[0] = subexpr[1]

def p_factor_num(subexpr):
    'factor : NUMBER'
    subexpr[0] = subexpr[1]
    
def p_factor_expr(subexpr):
    'factor: expression'
    subexpr[0] = subexpr[1]

def p_error(subexpr):
    print(subexpr)
    raise Exception("Syntax error.")

import sys

Symbol = str          # A Scheme Symbol is implemented as a Python str
List   = list         # A Scheme List is implemented as a Python list
Number = (int, float) # A Scheme Number is implemented as a Python int or float

def tokenize(chars):
    "Convert a string of characters into a list of tokens."
    return chars.replace('(', ' ( ').replace(')', ' ) ').split()

def parse(program):
    "Read a Scheme expression from a string."
    return read_from_tokens(tokenize(program))

def read_from_tokens(tokens):
    "Read an expression from a sequence of tokens."
    if len(tokens) == 0:
        raise SyntaxError('unexpected EOF while reading')
    token = tokens.pop(0)
    if '(' == token:
        L = []
        while tokens[0] != ')':
            L.append(read_from_tokens(tokens))
        tokens.pop(0) # pop off ')'
        return L
    elif ')' == token:
        raise SyntaxError('unexpected )')
    else:
        return atom(token)

def atom(token):
    "Numbers become numbers; every other token is a symbol."
    try: return int(token)
    except ValueError:
        try: return float(token)
        except ValueError:
            return Symbol(token)

def apply_cps(s):
    r = []
    param = ['k']
    body = [param[0],s]
    r.append('lambda')
    r.append(param)
    r.append(body)
    return r

def lambda_cps(p,b):
    r = []
    param = ['K']
    r.append('lambda')
    r.append(param)
    r.append(param[0])

    
    pass

def symbol_cps(s):
    r = []
    param = ['K']
    body = [param[0],s]
    r.append('lambda')
    r.append(param)
    r.append(body)
    return r

def cps_trans(ast):
    cps_r = []
    if not isinstance(ast,List):
        cps_r.extend(symbol_cps(ast))
    elif ast[0] == 'lambda':
        (_, param, body) = ast
        lambda_cps(param,body)
        pass
    else:
        cps_r.extend(apply_cps(ast))
    return cps_r

def unparse_ast(s):
    for i in s:
        if isinstance(i,str):
            sys.stdout.write(i+" ");
        elif isinstance(i,list):
            sys.stdout.write('(')
            unparse_ast(i)
            sys.stdout.write(')')
        else:
            sys.stdout.write(str(i)+' ')

def cps_out(cps_r):
    sys.stdout.write('(')
    unparse_ast(cps_r)
    print(')\n')
##PyCps##
Convert lambda-calculus to CPS form implemented by python

###Example###
*python>* from cps import *

*python>* docps('(lambda (x) (lambda (y) (+ x y)))')

*python>* docps('(lambda (x) (+ x 2))')

*python>* docps('((lambda (x) (+ x 2)) 3)')
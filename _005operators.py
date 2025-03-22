# Python divide the operators in the following groups:
from traceback import print_tb

number_one = 100
number_two = 10
number_three = 3

# Arithmetic (+, -, *, /) and
var = number_one % number_two           # módulo
result = number_one ** 10               # exponenciação
resultt = number_one // number_three    # divisão inteira


# Assignment (=, +=, -=. *=, /=, //=, **=, %=) and
x = 2
print(x)
print(x :=100) # walrus(:=) atribui valor a variável e usa na mesma expressão - Python 3.8+

# Comparisons (==, !=, >, >=, <, <=)


# Logical Operators (and, or, not)

print(10 > 5 and 1 > 0) # True
print(10 % 2 == 0 and 10 > 100) #False
print(not 10 == 10) # False (not inverte o resultado da expressão)


# Identity Operators - usados para comparar os endereços de memória
# is - verifica se dois objetos referenciam o mesmo endereço
# is not - verifica se dois objetos NÃO referenciam o mesmo endereço
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b) # True
print(a is c) # False
print(a is not c) # True
print()


# Membership Operators - verifica a presença de um valor em sequências

my_list = [1, 2, 3]
print(3 in my_list)        # True
print("a" not in "banana") # False


# Operator Precedence(se dois operadores tiverem a mesma precedência, a expressão é avaliada da esqueda p/ direita)
'''
Precedência mais alta no topo

()
**
+x -x ~x (unary)
* / // %
+ -
<<>> bitwise left and right shifts
& bitwise and
^ bitwise xor
| bitwise or
comparisons, identity, and membership
not
and
or
'''
# Tuple
# São ordenadas; São imutáveis; Aceita duplicatas; Indexadas; permiete elementos variados
# Principal diferença para listas é a imutalidade
from traceback import print_tb

mytuple = ("Apple", "Banana", "Orange")
tuple_hetero = (1, 2, 3, "Python", True)

# Acess items
print(mytuple[0])
print(mytuple[-1])
print(mytuple[:2])  # suporte a fatiamento
print(mytuple.index("Orange")) # retorna o indice do item procurado


#Alternativa para alterar valores em um tupla

tuple_numbers = (5, 6, 7)
my_list = list(tuple_numbers)       # converte p/ litsa
my_list[0] = 100
my_list.append(8)
tuple_numbers = tuple(my_list)      # converte p/ tuple

# É permitido add tuplas e tuplas

tuple_um = ("a", "b")
tuple_dois = ("c",)
tuple_um +=tuple_dois
print(tuple_um)   #(a, b, c)


# Unpacking - o número de variáveis deve corresponder ao numero de items na tupla

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)        # apple
print(type(yellow)) # str

# Outra opção
fruits = ("apple", "banana", "cherry")
(green, *others) = fruits       #green = apple - others = [banana, cherry]


# Join or Multiply

numbers = (1, 2, 3)
letters = ("d", "e", "f")
result = numbers + letters
print(result)           #(1, 2, 3, 'd', 'e', 'f')

numbers = numbers * 2
print(numbers)         #(1, 2, 3, 1, 2, 3)
# This is comment

print("Hello World!")

# Creating variable

number = 25
name = "Gabriel"
last_name = "Silva"
first_name, second_name, third_name = "Gabriel", "Maria", "João"
x = y = z = "Python"


# Output variables

print(name + last_name)  # por padrão quebra a linnha \n
print(first_name, second_name, third_name)  # por padrão os valores são separdos com ' '
print("Python", "é", "legal", sep="*")  # personaliza o separador


# Cast explicit

age = int("30")
height = float("1.75")
is_true = bool("False")  # qualquer string não vazia retorna True
is_false = bool(0)  # qualquer valor vazio [], {}, () ou None, 0, etc.. retorna False


# Get the type
print(type(age))
print(type([1, 2, 3]))
print(type({'one': 10, 'two': 20, 'three': 30}))
print(type((50, 60, 70)))


# Unpacking                 # processo de 'desempacotar' valores de um iterável, em variávies individuais

fruits = ['banana', 'apple', 'orange']
a, b, c = fruits  # a = banana, b = apple, c = orange

numbers = (1, 2, 3, 4, 5)  # operador * captura mútiplos valores em uma variável
first, *rest, last = numbers  # first = 1, *rest[2, 3, 4], last = 5

dictionary = {"key_1": 1, "key_2": 2}
dictionary_2 = {**dictionary, "key_3": 3}  # desempacota e adiciona um novo item

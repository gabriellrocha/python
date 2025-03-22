# built-in by default, in these categories
import random

# text type
name: str = "gabriel"

# numeric types
age: int = 25
height: float = 1.75

#sequences types
list_numbers: list = [1, 2, 3, 4, 5]
tuple_str: tuple = ('gabriel', 'silva')
range_sequence: range = range(2, 13, 2)     #sequencia imutável (start, stop(não incluso), step) - não armazena dados

#mapping type
dict_contacts: dict = {"gabriel": 12345678, "irineu": 87654321}

#set types
my_set: set = {50, 75, 100} # mutável (podemos add e remover, mas os elementos em si devem ser imutáveis)
fs = frozenset([5, 6, 7])   # imutável

#boolean types
is_true = True
is_false = False


#binary types
b: bytes = b"hello" # 'b' indica que é um tipo bytes (sequencia imutável de bytes - valor ASCII)


ba: bytearray = bytearray([65, 66, 67]) #mutável
ba[0] = 68


# Para criar números aleatórios em python use o módulo random
print(random.randrange(1, 10))


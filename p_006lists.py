# Listas
# São ordenadas; permite duplicatas; indexadas; mutáveis; permite elementos variados


thislist = ["apple", "banana", "orange", "cherry", 12, 1.99, True]
print(thislist)
print(thislist[2])  # orange
print(thislist[-2])  # 1.99
print(thislist[2:5])  # range of indexes (5 not included)
print(thislist[:4])  # (4 not included)
print("banana" in thislist)  # True

# Add items

thislist.insert(2, "watermelon")
thislist.append("kiwi")  # add an item to the end
thislist.extend(["mango", "papaya"])  # append elements from another list ( or any iterable tuples, sets, dict etc.)

# Remove items
thislist.remove("apple")  # remove a primeira ocorrência em caso de duplicatas
thislist.pop(0)  # remove do índice específicado ( se não especificar remove o útlimo)
# thislist.clear()
# del thislist            # remove a lista inteira


# Loop Lists

for x in thislist:
    print(x)

for i in range(len(thislist)):  # range(0, len(thislist) -1)
    print(thislist[i])

# [print(x) for x in thislist]  #list comprehension (não recomendado p/ imprimir elementos, pois o objetivo é gerar uma nova lista)

i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1

# list comprehension
# sintaxe new_list = [expression for item in iterable if condition == True]
# 'expression' pode ser o item atual ou o resultado

list_numbers = [1, 3, 5, 7, 9]
new_list = [x * 2 for x in list_numbers] # deixa a lista antiga inalterada


# Sort Lists (classifica a lista alfanumericamente)

thislistnumber = [100, 23, 82, 50, 65, 17]
thislistnumber.sort()
thislistnumber.sort(reverse=True)


# Funções integradas como funções-chave
thislistnames: list[str] = ["bia", "otavio", "katia", "Carla"]
thislistnames.sort(key = str.lower)
for i in thislistnames:
    print(i)


# Copy Lists (todas geram o mesmo resultado)

my_list1 = list_numbers.copy()
my_list2 = list(list_numbers)
my_list3 = list_numbers[:]


# Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3, 4]
list3 = list1 + list2

list1.extend(list2)

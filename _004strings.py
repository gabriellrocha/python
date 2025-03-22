# Strings - cercadas com aspas simples ou duplas
string_1 = "python"
string_2 = 'python'

# Citações dentro de citações
print("Meu nome é 'Gabriel'")
print('Meu nome é "Gabriel"')

# multilinhas

texto = """Este é 
um texto em python
multilinha."""
print(texto) # quebra de linnhas são inseridas

print(texto[0])             # Para pegar caracteres essa é a sintaxe
print(len(texto))           # comprimento
print("pyth" in texto)      # verifica se uma sequencia está presente
print("java" not in texto)  # verifica se uma sequencia NÃO está presente


#Slicing (fatiamento)

text = "Hello World!"
print(text[2:7])  #llo W
print(text[:5])   #Hello
print(text[0:])   #Hello World!
print(text[-6:-2])   #Worl - inicia a partir do final


#Others - Todos os métodos de String retornam uma nova String
name = "Gabb RIel"
print(name.lower()) #lower case
print(name.upper()) #upper case
print(name.replace("G", "X"))
print(name.split(" ")) #['Gabb', 'RIel']


#F-Strings - Python 3.6+
age = 25
color = "blue"
price = 59

print(f"My age: {age}. My favorite color: {color}")
print(f"The price is {price:.2f} dollars")
print(f"The price is {20 * 59} dollars")

# Escape Character - use uma \ antes do caractere

print("Python is \"fast\" ")
print("Python is \tfast")
# Funções são definidas utilizando a palavra-chave def
"""
Do ponto de vista da função:
 Um parâmetro é a variável dentro dos parênteses na definição da função
 Um argumento é o valor que é enviado para a função quando ela é chamada
"""


# função mínima
def minha_funcao():
    print("Função em Python")


# função com parâmetros
def minha_funcao_2(nome):
    print(f"Olá, {nome}")


# pass - se por algum motivo precisar definir uma função sem conteúdo
def sem_implementacao():
    pass


# parâmetros arbitrários *args (a função receberá uma tupla de argumentos)
# São frequentemente abreviados para *args na documentação oficial
def somar_numeros(*numeros):
    total = 0
    for numero in range(len(numeros)):
        total += numero
    return total


somar_numeros(1, 2, 4, 5)
somar_numeros(1, 2, 4, 5, 8, 9)


def apresentacao(nome, idade):
    print(f"Nome {nome}. Idade {idade}")


# Argumentos de palavra-chave
# Pode enviar argumentos com a sintaxe chave = valor (a ordem nao importa)
apresentacao(idade=25, nome="Gabriel")


# Argumentos de palavra-chave arbitrárias
# A função receberá um dicionário de argumentos
# São frequentemente abreviados para **kwargs na documentação oficial
def frutas_favoritas(**frutas):
    print("Fruta favorita:", frutas["primeira"])


frutas_favoritas(primeira="abacaxi", segunda="melancia")  # Note que passei mais de um arg e funciona


# Função com o valor do parâmetro padrão
# Ou seja, se NÃO passarmos argumento, a função usará o valor padrão
# Também é uma forma de 'simular' o polimorfismo de sobrecarga no Python
def linguagem_favorita(linguagem="Todas"):
    print(f"Minha linguagem favorita é... {linguagem}")


linguagem_favorita()
linguagem_favorita("Java")


# Argumentos somente posicionais
# / separador de parâmetros posicional - qualquer parâmetro a esquerda do / deve ser fornecido de forma posicional
def somar_tres_numeros(x, /, y, z):
    print(x + y + z)


somar_tres_numeros(3, z=5, y=2)  # 'x' não pode ser nomeado


# Argumentos somente nomeados
# Qualquer argumento a direita do * deve ser fornecido de forma nomeada
def divisao(*, dividendo, divisor):
    print(dividendo / divisor)


divisao(dividendo=10, divisor=2)  # 5.0

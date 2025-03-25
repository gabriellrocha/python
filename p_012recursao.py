"""
- Recursão é quando uma função chama a si mesma para 'resolver um subproblema'
"""


# Base - condição que faz a recursão parar (pode ser mais de um como em fibonacci)
# Chamada recursiva - chama a si mesma ate o valor alcançar a base

# função que calcula o fatorial n!
def fatorial(numero):
    if numero == 1 or numero == 0:  ## caso base
        return 1
    return numero * fatorial(numero - 1)


# função que retorna o n-ésimo elemento da sequencia de fibonacci
def fibonacci(p):
    if p < 2:  ## caso base
        return p
    return fibonacci(p - 1) + fibonacci(p - 2)

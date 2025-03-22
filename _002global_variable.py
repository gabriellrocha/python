# The global keyword

variable_x = "awesome"
variable_y = "python"

def my_def():
    variable_x = "fantastic"  # variável com o memso nome da global, mas seŕa local


def mey_def_1():
    global variable_y         # 'global' - para alterar o valor de uma variável global dentro da função
    variable_y = "python 3"

mey_def_1()
print(variable_y)
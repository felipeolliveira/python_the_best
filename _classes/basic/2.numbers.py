###################################
########### Numbers ###############
###################################
# Em Python, há três tipos de números:
# - int: números inteiros.
# - float: números decimais.
# - complex: números complexos.

MY_NAME = "Felipe"
MY_AGE = 25
MY_PI = 3.14

# É possível converter um tipo de variável para outro usando as funções built-in do Python.
# Os tipos precisam ser compatíveis para a conversão, como int para float e vice-versa.
my_age_float = float(MY_AGE)
print("int: ", MY_AGE, ", age: ", my_age_float)

# Especificamente no Python, há uma operação que difere de outras linguagens, que é a divisão com retorno de inteiros.
# Para isso, você pode usar o operador //.
divider_int = 10 // 3  # 3
divider_float = 10 / 3  # 3.3333333333333335
print("divider_int: ", divider_int, ", divider_float: ", divider_float)

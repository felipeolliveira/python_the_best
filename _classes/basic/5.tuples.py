# Tuplas são ordenadas e imutáveis. Permitem itens duplicados.
# Tuplas são definidas por parênteses ().

my_tuple = (1, 2, 3, 4, 5, "string", 3.14)
print("my_tuple: ", my_tuple)

# Acessando elementos da tupla
print("my_tuple[0]: ", my_tuple[0])

# Para acessar um intervalo de elementos, use a notação de fatiamento.
#  - O primeiro índice é inclusivo.
#  - O segundo índice é exclusivo.
#  - Se o primeiro índice for omitido, o padrão é 0.
#  - Se o segundo índice for omitido, o padrão é o tamanho da tupla.
print("my_tuple[1:3]: ", my_tuple[1:3])
print("my_tuple[:3]: ", my_tuple[:3])  # Equivalente a my_tuple[0:3]
print("my_tuple[3:]: ", my_tuple[3:])  # Equivalente a my_tuple[3:len(my_tuple)]

# Métodos uteis para tuplas são semelhantes aos métodos de listas, mas não incluem métodos que alteram a estrutura da tupla.

# Listas são ordernadas e mutáveis. Permitem itens duplicados.
# Listas são definidas por colchetes [].

my_list = [1, 2, 3, 4, 5, "string", 3.14]
print("my_list: ", my_list)

# Acessando elementos da lista
print("my_list[0]: ", my_list[0])

# Para acessar um intervalo de elementos, use a notação de fatiamento.
#  - O primeiro índice é inclusivo.
#  - O segundo índice é exclusivo.
#  - Se o primeiro índice for omitido, o padrão é 0.
#  - Se o segundo índice for omitido, o padrão é o tamanho da lista.
print("my_list[1:3]: ", my_list[1:3])
print("my_list[:3]: ", my_list[:3])  # Equivalente a my_list[0:3]
print("my_list[3:]: ", my_list[3:])  # Equivalente a my_list[3:len(my_list)]


# Métodos uteis para listas
# - append() - Adiciona um elemento ao final da lista.
# - insert() - Adiciona um elemento em uma posição específica.
# - remove() - Remove um elemento específico da lista.
# - pop() - Remove um elemento de uma posição específica.
# - clear() - Remove todos os elementos da lista.
# - index() - Retorna o índice do primeiro elemento com o valor especificado.
# - count() - Retorna o número de elementos com o valor especificado.
# - sort() - Classifica a lista.
# - reverse() - Inverte a ordem da lista.
# - copy() - Retorna uma cópia da lista.
my_list.append(6)
print("my_list.append(6):", my_list)

my_list.insert(5, 0)
print("my_list.insert(5, 0):", my_list)

my_list.remove(0)
print("my_list.remove(0):", my_list)

my_list.pop(0)
print("my_list.pop(0):", my_list)

my_list.clear()
print("my_list.clear():", my_list)

my_list = [1, 2, 3, 4, 5, 3, 3, 3]
print("my_list:", my_list)
print("my_list.index(3):", my_list.index(3))
print("my_list.count(3):", my_list.count(3))

my_list.sort()
print("my_list.sort():", my_list)

my_list.reverse()
print("my_list.reverse():", my_list)

my_list_copy = my_list.copy()
print("my_list_copy:", my_list_copy)

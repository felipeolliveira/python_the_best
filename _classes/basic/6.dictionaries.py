# Dicionário é uma coleção de dados que contém chave e valor, não ordenada e mutável.
# Dicionários são definidos por chaves {}.
# dict[type_key, type_value]

person = {"name": "John", "age": 36, "country": "Norway", 3: 0.14}
print("person: ", person)

# Acessando elementos do dicionário
print("person['name']: ", person["name"], type(person["name"]))
print("person[3]: ", person[3], type(person[3]))

# Métodos uteis para dicionários
# - clear(): Remove todos os elementos do dicionário
# - copy(): Retorna uma cópia rasa do dicionário
# - fromkeys(): Retorna um dicionário com as chaves e valores especificados
# - get(): Retorna o valor da chave especificada
# - items(): Retorna uma lista contendo uma tupla para cada par de chave-valor
# - keys(): Retorna uma lista contendo as chaves do dicionário como dict_keys
# - values(): Retorna uma lista de todos os valores no dicionário como dict_values
# - pop(): Remove o elemento com a chave especificada
# - popitem(): Remove o último item inserido
# - setdefault(): Retorna o valor da chave especificada. Se a chave não existir, insere a chave com o valor especificado
# - update(): Atualiza o dicionário com os elementos especificados
# - del dict[key]: Remove o item com a chave especificada

person.clear()
print("person.clear(): ", person)

person = {"name": "John", "age": 36, "country": "Norway", 3: 0.14}
person_copy = person.copy()
print("person_copy: ", person_copy)

person_fromkeys = dict.fromkeys(person)
print("person_fromkeys: ", person_fromkeys)

person_get = person.get("name")
print("person_get: ", person_get)

person_items = person.items()
person_items_list = list(person_items)
print("person_items_dict: ", person_items)
print("person_items_list: ", person_items_list)

person_keys = person.keys()
person_keys_list = list(person_keys)
print("person_keys_dict: ", person_keys)
print("person_keys_list: ", person_keys_list)

person_values = person.values()
person_values_list = list(person_values)
print("person_values: ", person_values)
print("person_values_list: ", person_values_list)

person_pop = person.pop("name")
print("person_pop: ", person_pop)
print("person: ", person)

person_popitem = person.popitem()
print("person_popitem: ", person_popitem)
print("person: ", person)

person.setdefault("name", "John")
print("person.setdefault('name', 'John'): ", person)

person.update({"name": "John update"})
print("person.update({'name': 'John update'}): ", person)

del person["name"]
print("del person['name']: ", person)

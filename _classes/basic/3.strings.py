MY_NAME = "Felipe"
MY_AGE = 25
MY_PI = 3.14
MY_LAST_NAME = "Oliveira"

# Em Python, as strings são representadas por aspas simples ou duplas.
# Pode usar aspas triplas para strings multilinhas.
normal_string = "Felipe Oliveira"

multiple_line_string = """ Lorem ipsum dolor sit amet,
consectetur adipiscing elit. """

string_with_break_declaration = "Felipe \
Oliveira"

string_concat = MY_NAME + " " + MY_LAST_NAME

# É possível usar o operador % para formatar strings.
# Semelhante ao printf em C e o uso dos verbos de formatação.
string_sprintf = "My name is %s" % MY_NAME
string_sprintf_with_multiple_verbs = "My age is %d and my pi is %.2f" % (MY_AGE, MY_PI)

# Outra forma de formatar strings é usando o método format.
string_format = "My name is {}".format(MY_NAME)
string_format_with_multiple_values = "My name is {} and my age is {}".format(
    MY_NAME, MY_AGE
)
string_format_short = f"My name is {MY_NAME}"

print("normal_string: ", normal_string)
print("multiple_line_string: ", multiple_line_string)
print("string_with_break_declaration: ", string_with_break_declaration)
print("string_concat: ", string_concat)
print("string_sprintf: ", string_sprintf)
print("string_sprintf_with_multiple_verbs: ", string_sprintf_with_multiple_verbs)
print("string_format: ", string_format)
print("string_format_with_multiple_values: ", string_format_with_multiple_values)
print("string_format_short: ", string_format_short)

# Strings podem ser usadas de maneira mais segura codificando-as e decodificando-as em bytes

string_bytes = normal_string.encode()
print("normal_string.encode(): %s" % list(string_bytes))
print("string_bytes.decode(): ", string_bytes.decode())

# Mais funções úteis para strings
# - len(): retorna o tamanho da string.
# - lower(): retorna a string em minúsculo.
# - upper(): retorna a string em maiúsculo.
# - strip(): remove valores do início e do fim da string.
#   - lstrip(): remove valores do início da string.
#   - rstrip(): remove valores do fim da string.
# - replace(): substitui uma string por outra.
# - split(): divide a string em substrings.
# - join(): junta as substrings.
# - find(): procura por uma substring.
# - count(): conta quantas vezes uma substring aparece na string.
# - startswith(): verifica se a string começa com uma substring.
# - endswith(): verifica se a string termina com uma substring.

# Exemplos
print("len(normal_string): ", len(normal_string))
print("normal_string.lower(): ", normal_string.lower())
print("normal_string.upper(): ", normal_string.upper())
print("normal_string.strip(): ", normal_string.strip())
print("normal_string.replace('e', 'a'): ", normal_string.replace("e", "a"))
print("normal_string.split('e'): ", normal_string.split("e"))
print("'-'.join(normal_string): ", "-".join(normal_string))
print("normal_string.find('e'): ", normal_string.find("e"))
print("normal_string.count('e'): ", normal_string.count("e"))
print("normal_string.startswith('Fel'): ", normal_string.startswith("Fel"))
print("normal_string.endswith('eira'): ", normal_string.endswith("eira"))

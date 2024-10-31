# Em Python, as variáveis são criadas no momento em que você atribui um valor a ela.

# O tipo da variável é definido no momento da atribuição.
# Uma variavel não pode começar com número, não pode conter espaços e não pode conter
# caracteres especiais.
# Caso você queira separar as palavras de uma variável, você pode usar o underscore (_).
# Por convenção:
# - as variáveis são escritas em snake_case.
# - as constantes são escritas em UPPER_CASE.
# - as funções são escritas em snake_case.
# - as classes são escritas em PamelCase.

MY_NAME = "Felipe"
MY_AGE = 25
MY_PI = 3.14
MY_LAST_NAME = "Oliveira"


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def function_example() -> str:
    return "Hello World"


# Para saber o tipo de uma variável, você pode usar a função type().
print(type(MY_NAME))
print(type(MY_AGE))
print(type(MY_PI))
print(type(Person))
print(type(function_example))

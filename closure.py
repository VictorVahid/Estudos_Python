"""
Closure e funções que retornam outras funções
"""


def create_hello(greeting):
    def hello(nome):
        return f"{greeting}, {nome}!"

    return hello


say_goodMorning = create_hello("Bom dia")
say_goodNight = create_hello("Boa noite")


for nome in ["Otávio", "Maria", "Victor", "Thea"]:
    print(say_goodMorning(nome))
    print(say_goodNight(nome))

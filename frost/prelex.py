class PreLexFunc:
    def __init__(self, name: str, func):
        self.name: str = name
        self.func = func


def prelex(code: tuple[str], prelexers_funcs: list[PreLexFunc], env: dict):
    pl = []
    codel = list(code)
    for x, i in enumerate(code):
        if i.startswith("#"):
            pl.append(x)
            for y in prelexers_funcs:
                if y.name == i[1:]:
                    y.func(i[1:].split()[1:], env)
    for num in pl:
        del codel[num]
    return codel, env
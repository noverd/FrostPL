from frost.ltypes import TypeN, ParseFunc


def var_typer(arg: TypeN, env):
    return env.get_var(arg.value)


def string_typer(arg: TypeN, env):
    return TypeN(arg.type, arg.value[1:-1])


def zombie_string_typer(arg: TypeN, env):
    strf: str = arg.value[2:-1]
    formstr = False
    formstr_new = []
    for i in strf:
        if i == "{":
            formstr_new.append("")
            formstr = True
        elif i == "}":
            formstr = False
        elif formstr:
            formstr_new[-1] += i
    for x in formstr_new:
        try:
            strf = strf.replace("{" + x + "}", str(env.get_var(x).value))
        except:
            pass

    return TypeN(arg.type, strf)


partp = [
    ParseFunc("Var", var_typer),
    ParseFunc("String", string_typer),
    ParseFunc("StringZ", zombie_string_typer),
]

from ltypes import TypeN


def var_typer(arg: TypeN, env):
    s = env.get_var(arg.value)
    return s


def string_typer(arg: TypeN, env):
    s = TypeN(arg.type, arg.value[1:-1])
    return s


def zombie_string_typer(arg: TypeN, env):
    strf: str = arg.value[2:-1]
    formstr = False
    formstr_new = []
    for i in strf:
        if i == "{":
            formstr_new.append("")
            formstr = True
        else:
            if i == "}":
                formstr = False
            else:
                if formstr:
                    formstr_new[-1] += i
    for x in formstr_new:
        try:
            strf = strf.replace("{" + x + "}", str(env.get_var(x).value))
        except:
            pass

    s = TypeN(arg.type, strf)
    return s

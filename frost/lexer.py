from .ltypes import Func, FuncN


def lex(code: tuple, env):
    cd = [i.split(";")[0] for i in code]
    funcl = []
    for i in cd:
        cds = i.split()
        com = cds[0]
        del cds[0]
        args = cds
        for x, arg in enumerate(args):
            for t in env["types"]:
                if t.check(arg) and t.regxp != "None":
                    args[x] = t.typen(arg)
                    break
        func_found: bool = False
        for func in env["funcs"]:
            if func.name == com and func.valid(com, args):
                funcl.append(func.funcn(args))
                func_found = True
                break
        if not func_found:
            argsty = [i.type for i in args]
            funcl.append(FuncN(Func(com, tuple(argsty)), args))
    return funcl

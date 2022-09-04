from .ltypes import Func, FuncN


def lex(code: tuple, env):
    cd = []
    for i in code:
        for x in i.split(";"):
            cd.append(x)
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
            if func.name == com:
                if func.valid(com, args):
                    funcl.append(func.funcn(args))
                    func_found = True
                    break
                else:
                    continue
        if not func_found:
            argsty = []
            for i in args:
                argsty.append(i.type)
            funcl.append(FuncN(Func(com, tuple(argsty)), args))
    return funcl

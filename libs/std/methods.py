from frost.lerrno import *
from frost.ltypes import Type, Func, RunPythonFunc

funcs = [
    Func("add", ("Number", "Number", "String")),
    Func("sub", ("Number", "Number", "String")),
    Func("mul", ("Number", "Number", "String")),
    Func("div", ("Number", "Number", "String")),
    Func("tdef", ("String", "String", "String")),
    Func("var", ("String", "String", "Any")),
    Func("out", ("String",)),
    Func("eval", ("String", "String", "String")),
    Func("jump_if", ("String", "Int")),
    Func("jump", ("Int",)),

]


def add(args: tuple, env):
    try:
        buf = int(args[0].value) + int(args[1].value)
    except:
        raise_err(Error("adding error", at_format(env.ic, env.fl, env.cd)))
        return
    else:
        env.set_var(args[2].value, "Int", str(buf))


def sub(args: tuple, env):
    try:
        buf = int(args[0].value) - int(args[1].value)
    except:
        raise_err(Error("subbing error", at_format(env.ic, env.fl, env.cd)))
        return
    else:
        env.set_var(args[2].value, "Int", str(buf))


def mul(args: tuple, env):
    try:
        buf = int(args[0].value) * int(args[1].value)
    except:
        raise_err(Error("muling error", at_format(env.ic, env.fl, env.cd)))
        return
    else:
        env.set_var(args[2].value, "Int", str(buf))


def div(args: tuple, env):
    try:
        buf = int(args[0].value) / int(args[1].value)
    except:
        raise_err(Error("division error", at_format(env.ic, env.fl, env.cd)))
        return
    else:
        env.set_var(args[2].value, "Int", str(int(buf)))


def var(args: tuple, env):
    try:
        env.set_var(args[0].value, args[1].value, args[2].value)
    except:
        raise_err(Error("setting var error", at_format(env.ic, env.fl, env.cd)))
        return


def frost_print(args: tuple, env):
    try:
        print(str(args[0].value).replace("\s", " "))
    except:
        raise_err(Error("out error", at_format(env.ic, env.fl, env.cd)))
        return


def eval_exp(args: tuple, env):
    try:
        r = eval(args[0].value)
    except:
        raise_err(Error("eval error: eval is not correct", at_format(env.ic, env.fl, env.cd)))
        return
    tp: str = ""
    try:
        if args[1].value == "Int":
            r = int(r)
            tp = "Int"
        elif args[1].value == "Float":
            r = float(r)
            tp = "Float"
        else:
            raise Exception("Error")
    except:
        raise_err(Error("eval typing error", at_format(env.ic, env.fl, env.cd)))
        return
    env.set_var(args[2].value, tp, r)


def jump_if(args: tuple, env):
    try:
        print(args[0].value)
        r = int(eval(args[0].value))
    except:
        raise_err(Error("jump_if error: logic eval is not correct", at_format(env.ic, env.fl, env.cd)))
        return
    if bool(r):
        env.ic = int(args[1].value) - 2


def jump(args: tuple, env):
    env.ic = int(args[0].value) - 2


def typedef(args: tuple, env):
    try:
        for t in env.env["types"]:
            if t.typename == args[0].value:
                raise_err(Error(f"tdef error: type {args[0].value} is defied ", at_format(env.ic, env.fl, env.cd)))
                return
        env.env["types"].append(Type(args[0].value, args[1].value, args[2].value))
    except:
        raise_err(Error(f"tdef error", at_format(env.ic, env.fl, env.cd)))


runfuncs = [
    RunPythonFunc(add, "add"),
    RunPythonFunc(sub, "sub"),
    RunPythonFunc(mul, "mul"),
    RunPythonFunc(div, "div"),
    RunPythonFunc(var, "var"),
    RunPythonFunc(typedef, "tdef"),
    RunPythonFunc(frost_print, "out"),
    RunPythonFunc(eval_exp, "eval"),
    RunPythonFunc(jump_if, "jump_if"),
    RunPythonFunc(jump, "jump"),

]

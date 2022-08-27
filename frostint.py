from frost import Runner
from ltypes import Func, Type, RunPythonFunc, ParseFunc
from lerrno import *
import methods
import partypes

env = {
    "funcs": [
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

    ],
    "runfuncs": [
        RunPythonFunc(methods.add, "add"),
        RunPythonFunc(methods.sub, "sub"),
        RunPythonFunc(methods.mul, "mul"),
        RunPythonFunc(methods.div, "div"),
        RunPythonFunc(methods.var, "var"),
        RunPythonFunc(methods.typedef, "tdef"),
        RunPythonFunc(methods.frost_print, "out"),
        RunPythonFunc(methods.eval_exp, "eval"),
        RunPythonFunc(methods.jump_if, "jump_if"),
        RunPythonFunc(methods.jump, "jump"),

    ],
    "types": [
        Type("\d*", "Int", "Number"),
        Type("\d*\.\d*", "Float", "Number"),
        Type('^(").*(")$', "String", "String"),
        Type('^(z").*(")$', "StringZ", "String"),
        Type('^([a-zA-Z])[a-z_A-Z0-9]*', "Var", "Var")
    ],
    "parsetype": [
        ParseFunc("Var", partypes.var_typer),
        ParseFunc("String", partypes.string_typer),
        ParseFunc("StringZ", partypes.zombie_string_typer),
    ],
    "vars": {}
}
s = sys.argv[1]
f = open(s, "r")
l = f.readlines()
l = [line.rstrip() for line in l]
l = tuple(l)
rn = Runner(env, s)
rn.run_code(l)

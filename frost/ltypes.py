import re


class Type:
    def __init__(self, regxp: str, typename: str, typegroup: str = "None"):
        self.regxp = regxp
        self.typename = typename
        self.typegroup = typegroup

    def check(self, tp: str):
        return re.fullmatch(self.regxp, tp) is not None

    def typen(self, value: str):
        return TypeN(self, value)


class TypeN:
    def __init__(self, maintype: Type, value: str):
        self.type = maintype
        self.value = value

    def __repr__(self):
        return f'TypeN< "MainType" : "{self.type.typename}", "Value" : {self.value} >'


class Func:
    def __init__(self, name: str, argst: tuple):
        self.argst = argst
        self.argc = len(argst)
        self.name = name

    def valid(self, com: str, args: list):
        try:
            if com != self.name:
                return False
            for arg in args:
                for typearg in self.argst:
                    if (
                        arg.type.typename != typearg
                        and arg.type.typegroup != typearg != "Any"
                    ):
                        return False
        except:
            return False
        return True

    def funcn(self, args: list):
        return FuncN(self, args)


class FuncN:
    def __init__(self, func: Func, args: list):
        self.func: Func = func
        self.args: list = args

    def __repr__(self):
        return f'FuncN< "FuncName" : "{self.func.name}", "Args" : {self.args}>'


class RunPythonFunc:
    def __init__(self, func, name):
        self.func = func
        self.name = name

    def run(self, args, env):
        self.func(args, env)


class RunFrostFunc:
    def __init__(self, code: tuple, name, args: tuple):
        self.code = code
        self.name = name
        self.args = args

    def run(self, args, env):
        for x, i in enumerate(self.args):
            env.env["var"][i] = args[x]
        env.run_code(self.code)
        for i in self.args:
            del env.env["var"][i]


class ParseFunc:
    def __init__(self, typename: str, func):
        self.typename: str = typename
        self.func = func

    def parse(self, arg, env):
        return self.func(arg, env)

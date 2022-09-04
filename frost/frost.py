from .lexer import lex
from .ltypes import FuncN, TypeN
from .lerrno import *

ic = 0


class Runner:
    def __init__(self, env: dict, fl: str):
        self.env = env
        self.ic = 0
        self.cd = ""
        self.fl = fl

    def set_var(self, varname: str, typename: str, value: str):
        for i in self.env["types"]:
            if typename == i.typename or typename == i.typegroup:
                self.env["vars"][varname] = TypeN(i, value)
                return
        raise_err(Error(f"var setting error: type {typename} is not defied", at_format(self.ic, self.fl, self.cd)))

    def get_var(self, varname: str):
        try:
            return self.env["vars"][varname]
        except:
            raise_err(Error(f"var {varname} is not defined", at_format(self.ic, self.fl, self.cd)))

    def parse(self, codestr: FuncN):
        args = []
        nopt: bool
        for t in codestr.args:
            nopt = True
            for pt in self.env["parsetype"]:
                if pt.typename == t.type.typename:
                    ptc = pt.parse(t, self)
                    args.append(ptc)
                    nopt = False
                    break
            if nopt:
                args.append(t)
        return FuncN(codestr.func, args)

    def run_code(self, code: tuple):
        lexed = lex(code, self.env)
        self.ic = 0
        while self.ic + 1 <= len(lexed):
            self.cd = code[self.ic]
            codeln = self.parse(lexed[self.ic])
            funcfound: bool = False
            for i in self.env["runfuncs"]:
                if i.name == codeln.func.name:
                    i.run(codeln.args, self)
                    funcfound = True
            if not funcfound:
                raise_err(Error("function is not defined", at_format(self.ic, self.fl, self.cd)))
                break

            self.ic += 1
        return lexed

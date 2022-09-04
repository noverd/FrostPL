from frost.frost import Runner
from frost.modimport import import_from_json
import sys
env = import_from_json("/libs/std/")
env["vars"] = {}
s = sys.argv[1]
f = open(s, "r")
l = f.readlines()
l = [line.rstrip() for line in l]
l = tuple(l)
rn = Runner(env, s)
rn.run_code(l)

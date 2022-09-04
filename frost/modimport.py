import importlib.util
import json
import os
from frost.lerrno import *


def import_file(name: str, filename: str):
    module_file_path = filename
    module_name: str = name

    module_spec = importlib.util.spec_from_file_location(
        module_name, module_file_path
    )

    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    return module


def replace_sm(imp: dict, string: str):
    listobj = string.split(".")
    return getattr(imp[listobj[0]], listobj[1])


def import_from_json(path: str):
    old_path = os.getcwd()
    path = os.getcwd() + path
    try:
        os.chdir(path)
    except:
        raise_err(Error("Lib import error: path is not correct", "importing"))

    with open(path + "mod.json") as f:
        data = json.load(f)
    imports = {}
    for imp in data["imports"].keys():
        imports[imp] = import_file(imp, data["imports"][imp])
    objc = data["env"]
    for obj in data["env"].keys():
        if type(objc[obj]) == dict:
            for i in obj.keys():
                objc[obj][i] = replace_sm(imports, objc[obj][i])
        elif type(objc[obj]) == list:
            for x, i in enumerate(obj):
                objc[obj][x] = replace_sm(imports, i)
        elif type(objc[obj]) == str:
            objc[obj] = replace_sm(imports, objc[obj])
        else:
            continue
    os.chdir(old_path)
    return objc

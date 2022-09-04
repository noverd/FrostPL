from frost.ltypes import Type

types = [
    Type("\d*", "Int", "Number"),
    Type("\d*\.\d*", "Float", "Number"),
    Type('^(").*(")$', "String", "String"),
    Type('^(z").*(")$', "StringZ", "String"),
    Type('^([a-zA-Z])[a-z_A-Z0-9]*', "Var", "Var")
]

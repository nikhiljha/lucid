from collections import UserDict
import sys
import tomlkit
import types


class ModuleDict(types.ModuleType, UserDict):
    data = {}
    with open("versions.toml", "r") as configfile:
        data = tomlkit.parse(configfile.read())


sys.modules[__name__] = ModuleDict(__name__)

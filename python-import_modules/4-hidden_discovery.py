#!/usr/bin/python3
import sys
import importlib.util

if __name__ == "__main__":
    module_name = "hidden_4"
    module_path = "~/Desktop/Git_repos/alu-higher_level_programming/python-import_modules"

    spec = importlib.util.spec_from_file_location(module_name, module_path)
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    names = dir(hidden_4)

    for name in sorted(names):
        if not name.startswith("__"):
            print(name)

import importlib
import os
from pathlib import Path

import pytest


def load_from_module(path, module):
    testdata = importlib.import_module(f'data.test_cases.{path}.{module}').testdata
    return testdata


def package_contents(path, module):
    counter = module.count('_')
    submodules = []
    for n in range(0, counter + 1):
        module = module.replace("_", ".", 1)
        module_name = f'data.test_cases.{path}.{module}'
        spec = importlib.util.find_spec(module_name)
        if spec is None:
            if n < counter:
                continue
            else:
                pytest.xfail(f'Module {module_name} does not exist')
        elif spec.submodule_search_locations is None:
            return module

    pathname = Path(spec.origin).parent
    with os.scandir(pathname) as entries:
        for entry in entries:
            if entry.name.startswith('__'):
                continue
            current = '.'.join((module, entry.name.partition('.')[0]))
            if entry.is_file():
                if entry.name.endswith('.py'):
                    submodules.append(current)
            elif entry.is_dir():
                submodules.append(current)
                submodules |= package_contents(current)
    return submodules

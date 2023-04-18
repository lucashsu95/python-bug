import importlib

try:
    importlib.import_module('requests')
except ImportError:
    print('requests模块未安装')
else:
    print('requests模块已安装')

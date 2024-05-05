from setuptools import setup, Extension

setup(name='example_module', ext_modules=[Extension('example_module', sources=['example_module.c'], )], )

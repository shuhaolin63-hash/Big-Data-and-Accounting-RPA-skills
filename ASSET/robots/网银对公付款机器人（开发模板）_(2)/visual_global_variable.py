#!/usr/bin/python
# -*- coding: utf-8 -*-

def _init():
    global _global_dict
    try:
        _global_dict
    except:
        _global_dict = {}


def init_value(name, value):
    if name not in _global_dict:
        set_value(name, value)


def set_value(name, value):
    _global_dict[name] = value


def set_values(variable_dict):
    for key in variable_dict:
        _global_dict[key] = variable_dict[key]


def get_value(name, default_value=None):
    try:
        return _global_dict[name]
    except KeyError:
        return default_value

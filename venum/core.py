from collections import namedtuple


def Enum(*args, name=None):
    fields, values = zip(*args)
    return namedtuple(name or 'Enum', fields)(*values)

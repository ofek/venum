from collections import namedtuple


def Enum(*args, **kwargs):
    fields, values = zip(*args)
    return namedtuple(kwargs.get('name') or 'Enum', fields)(*values)

venum
=====

.. image:: https://img.shields.io/pypi/v/venum.svg?style=flat-square
    :target: https://pypi.org/project/venum

.. image:: https://img.shields.io/travis/ofek/venum.svg?branch=master&style=flat-square
    :target: https://travis-ci.org/ofek/venum

.. image:: https://img.shields.io/codecov/c/github/ofek/venum.svg?style=flat-square
    :target: https://codecov.io/gh/ofek/venum

.. image:: https://img.shields.io/pypi/pyversions/venum.svg?style=flat-square
    :target: https://pypi.org/project/venum

.. image:: https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square
    :target: https://en.wikipedia.org/wiki/MIT_License

-----

venum provides an Enum that is actually just a namedtuple, but easier to create.
This means an Enum doesn't have to be defined before program execution (similar
to the functional API) and members are truly immutable (can't dynamically add
new ones). Also, this saves a bit of memory over the stdlib's Enum.

Usage
-----

.. code-block:: python

    >>> from venum import Enum
    >>>
    >>> ContentTypes = Enum(
    ...     ('JSON', 'application/json; charset=utf-8'),
    ...     ('HTML', 'text/html; charset=utf-8'),
    ...     ('JS', 'text/javascript; charset=utf-8'),
    ...     ('XML', 'application/xml'),
    ...     ('TEXT', 'text/plain; charset=utf-8'),
    ...     ('JPEG', 'image/jpeg'),
    ...     ('PNG', 'image/png'),
    ...     ('YAML', 'application/x-yaml'),
    ...     name='ContentTypes'
    ... )
    >>> ContentTypes
    ContentTypes(JSON='application/json; charset=UTF-8', HTML='text/html; charset=utf-8', JS='text/javascript; charset=utf-8', XML='application/xml', TEXT='text/plain; charset=utf-8', JPEG='image/jpeg', PNG='image/png', YAML='application/x-yaml')

Attribute lookup
^^^^^^^^^^^^^^^^

No need for ``.value``.

.. code-block:: python

    >>> from venum import Enum
    >>>
    >>> sample = Enum(('BLUE', 1), ('RED', 2))
    >>> sample
    Enum(BLUE=1, RED=2)
    >>> sample.BLUE
    1

Comparison by value
^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    >>> from venum import Enum
    >>>
    >>> sample = Enum(('SPADES', 1))
    >>> sample.SPADES == 1
    True

Memory-efficiency
^^^^^^^^^^^^^^^^^

.. code-block:: python

    >>> from sys import getsizeof
    >>> from enum import Enum as StdEnum
    >>> from venum import Enum
    >>>
    >>> class SomeEnum(StdEnum):
    ...     BLUE = 3
    >>>
    >>> getsizeof(SomeEnum)
    1056
    >>> getsizeof(Enum(('BLUE', 3)))
    56

Installation
------------

venum is distributed on `PyPI`_ as a universal wheel and is available on
Linux/macOS and Windows and supports Python 2.7/3.3+ and PyPy.

.. code-block:: bash

    $ pip install venum

Final words
-----------

That's really all there is to it, but if you're keen on seeing more words that
begin with the letter **V**, here's V's monologue from `V for Vendetta`_.

    "Voilà! In view, a humble vaudevillian veteran, cast vicariously as both
    victim and villain by the vicissitudes of Fate. This visage, no mere veneer
    of vanity, is a vestige of the vox populi, now vacant, vanished. However,
    this valorous visitation of a by-gone vexation, stands vivified and has
    vowed to vanquish these venal and virulent vermin vanguarding vice and
    vouchsafing the violently vicious and voracious violation of volition.

    The only verdict is vengeance; a vendetta, held as a votive, not in vain,
    for the value and veracity of such shall one day vindicate the vigilant
    and the virtuous.

    Verily, this vichyssoise of verbiage veers most verbose, so let me simply
    add that it's my very good honor to meet you and you may call me V."

    -- V

.. _PyPI: https://pypi.org/project/venum
.. _V for Vendetta: https://en.wikipedia.org/wiki/V_for_Vendetta_(film)

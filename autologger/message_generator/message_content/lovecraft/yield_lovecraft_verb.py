#!
# -*- coding: utf-8 -*-

from typing import Iterator
from ordered_set import OrderedSet
from random import choice


def yield_lovecraft_verb() -> Iterator[str]:
    """Yields a lovecraft themed verb from a pre-defined set of options

    Yields:
        Iterator[str]: Iterator of lovecraft verbs. Use with ```next(yield_lovecraft_verb())```
    """

    yield choice(
        OrderedSet(
            [
                ...
            ]
        )
    )

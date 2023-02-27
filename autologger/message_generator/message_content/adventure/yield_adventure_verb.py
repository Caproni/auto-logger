#!
# -*- coding: utf-8 -*-

from typing import Iterator
from ordered_set import OrderedSet
from random import choice


def yield_adventure_verb() -> Iterator[str]:
    """Yields a adventure themed verb from a pre-defined set of options

    Yields:
        Iterator[str]: Iterator of adventure verbs. Use with ```next(yield_adventure_verb())```
    """

    yield choice(
        OrderedSet(
            [
                ...
            ]
        )
    )

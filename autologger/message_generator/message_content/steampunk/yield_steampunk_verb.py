#!
# -*- coding: utf-8 -*-

from typing import Iterator
from ordered_set import OrderedSet
from random import choice


def yield_steampunk_verb() -> Iterator[str]:
    """Yields a steampunk themed verb from a pre-defined set of options

    Yields:
        Iterator[str]: Iterator of steampunk verbs. Use with ```next(yield_steampunk_verb())```
    """

    yield choice(
        OrderedSet(
            [
                ...
            ]
        )
    )

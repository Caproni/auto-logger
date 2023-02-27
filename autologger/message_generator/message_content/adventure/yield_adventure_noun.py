#!
# -*- coding: utf-8 -*-

from typing import Iterator
from ordered_set import OrderedSet
from random import choice


def yield_adventure_noun() -> Iterator[str]:
    """Yields a adventure themed noun from a pre-defined set of options

    Yields:
        Iterator[str]: Iterator of adventure nouns. Use with ```next(yield_adventure_noun())```
    """

    yield choice(
        OrderedSet(
            [
                ...
            ]
        )
    )

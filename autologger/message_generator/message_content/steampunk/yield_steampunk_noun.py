#!
# -*- coding: utf-8 -*-

from typing import Iterator
from ordered_set import OrderedSet
from random import choice


def yield_steampunk_noun() -> Iterator[str]:
    """Yields a steampunk themed noun from a pre-defined set of options

    Yields:
        Iterator[str]: Iterator of steampunk nouns. Use with ```next(yield_steampunk_noun())```
    """

    yield choice(
        OrderedSet(
            [
                ...
            ]
        )
    )

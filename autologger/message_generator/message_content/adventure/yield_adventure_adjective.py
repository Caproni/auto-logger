#!
# -*- coding: utf-8 -*-

from typing import Iterator
from ordered_set import OrderedSet
from random import choice


def yield_adventure_adjective() -> Iterator[str]:
    """Yields a adventure themed adjective from a pre-defined set of options

    Yields:
        Iterator[str]: Iterator of adventure adjectives. Use with ```next(yield_adventure_adjective())```
    """

    yield choice(
        OrderedSet(
            [
                ...
            ]
        )
    )

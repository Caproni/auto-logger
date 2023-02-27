#!
# -*- coding: utf-8 -*-

from typing import Iterator
from ordered_set import OrderedSet
from random import choice


def yield_steampunk_adjective() -> Iterator[str]:
    """Yields a steampunk themed adjective from a pre-defined set of options

    Yields:
        Iterator[str]: Iterator of steampunk adjectives. Use with ```next(yield_steampunk_adjective())```
    """

    yield choice(
        OrderedSet(
            [
                ...
            ]
        )
    )

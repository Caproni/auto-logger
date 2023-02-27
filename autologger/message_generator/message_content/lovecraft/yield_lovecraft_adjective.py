#!
# -*- coding: utf-8 -*-

from typing import Iterator
from ordered_set import OrderedSet
from random import choice


def yield_lovecraft_adjective() -> Iterator[str]:
    """Yields a lovecraft themed adjective from a pre-defined set of options

    Yields:
        Iterator[str]: Iterator of lovecraft adjectives. Use with ```next(yield_lovecraft_adjective())```
    """

    yield choice(
        OrderedSet(
            [
                ...
            ]
        )
    )

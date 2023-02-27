#!
# -*- coding: utf-8 -*-

from typing import Iterator
from ordered_set import OrderedSet
from random import choice


def yield_lovecraft_noun() -> Iterator[str]:
    """Yields a lovecraft themed noun from a pre-defined set of options

    Yields:
        Iterator[str]: Iterator of lovecraft nouns. Use with ```next(yield_lovecraft_noun())```
    """

    yield choice(
        OrderedSet(
            [
                "eldrich",
                "necronomicon",
                "cthulhu",
                "yog-sothoth",
                "nyarlathotep",
            ]
        )
    )

#!
# -*- coding: utf-8 -*-

from typing import Iterator
from ordered_set import OrderedSet
from random import choice


def yield_scifi_adjective() -> Iterator[str]:
    """Yields a scifi themed adjective from a pre-defined set of options

    Yields:
        Iterator[str]: Iterator of scifi adjectives. Use with ```next(yield_scifi_adjective())```
    """

    yield choice(
        OrderedSet(
            [
                "quantum",
                "antimatter",
                "x-ray",
                "synthetic",
            ]
        )
    )

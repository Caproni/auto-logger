#!
# -*- coding: utf-8 -*-

from typing import Iterator
from ordered_set import OrderedSet
from random import choice


def yield_fantasy_adjective() -> Iterator[str]:
    """Yields a fantasy themed adjective from a pre-defined set of options

    Yields:
        Iterator[str]: Iterator of fantasy adjectives. Use with ```next(yield_fantasy_adjective())```
    """

    yield choice(
        OrderedSet(
            [
                "enchanted",
                "mystical",
                "magical",
                "otherwordly",
                "ethereal",
                "enigmatic",
                "spellbinding",
            ]
        )
    )

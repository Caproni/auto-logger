#!
# -*- coding: utf-8 -*-

from typing import Iterator
from ordered_set import OrderedSet
from random import choice


def yield_fantasy_verb() -> Iterator[str]:
    """Yields a fantasy themed verb from a pre-defined set of options

    Yields:
        Iterator[str]: Iterator of fantasy verbs. Use with ```next(yield_fantasy_verb())```
    """

    yield choice(
        OrderedSet(
            [
                "abjuring",
                "banishing",
                "bewitching",
                "charming",
                "conjuring",
                "cursing",
                "defending",
                "delving",
                "devouring",
                "enchanting",
                "incinerating",
                "levitating",
                "petrifying",
                "reanimating",
                "slaying",
                "summoning",
                "transmuting",
            ]
        )
    )

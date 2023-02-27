#!
# -*- coding: utf-8 -*-

from typing import Iterator
from ordered_set import OrderedSet
from random import choice


def yield_fantasy_noun() -> Iterator[str]:
    """Yields a fantasy themed noun from a pre-defined set of options

    Yields:
        Iterator[str]: Iterator of fantasy nouns. Use with ```next(yield_fantasy_noun())```
    """

    yield choice(
        OrderedSet(
            [
                "alchemist",
                "axe",
                "basilisk",
                "banshee",
                "centaur",
                "chimera",
                "cyclops",
                "dark fae",
                "dark knight",
                "dark prince",
                "dragon",
                "dryad",
                "fire elemental",
                "necromancer",
                "pheonix",
                "sentient shadow",
                "sorcerer",
                "unicorn",
                "goblin",
                "elf",
                "fairy",
                "turret",
            ]
        )
    )

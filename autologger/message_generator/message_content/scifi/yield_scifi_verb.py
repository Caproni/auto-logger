#!
# -*- coding: utf-8 -*-

from typing import Iterator
from ordered_set import OrderedSet
from random import choice


def yield_scifi_verb() -> Iterator[str]:
    """Yields a scifi themed verb from a pre-defined set of options

    Yields:
        Iterator[str]: Iterator of scifi verbs. Use with ```next(yield_scifi_verb())```
    """

    yield choice(
        OrderedSet(
            [
                "clone",
                "terraform",
                "realign",
                "program",
                "modulate",
                "reconfigure",
                "replicate",
                "synthesize",
                "hack",
            ]
        )
    )

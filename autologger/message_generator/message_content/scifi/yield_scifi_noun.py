#!
# -*- coding: utf-8 -*-

from typing import Iterator
from ordered_set import OrderedSet
from random import choice


def yield_scifi_noun() -> Iterator[str]:
    """Yields a scifi themed noun from a pre-defined set of options

    Yields:
        Iterator[str]: Iterator of scifi nouns. Use with ```next(yield_scifi_noun())```
    """

    yield choice(
        OrderedSet(
            [
                "trans-human",
                "android",
                "exoplanet",
                "spaceship",
                "warp core",
                "cyborg",
                "laser beams",
                "wormhole",
                "trans-variable harmonizer"
            ]
        )
    )

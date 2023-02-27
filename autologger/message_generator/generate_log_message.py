#!
# -*- coding: utf-8 -*-

from typing import Iterator
from random import uniform

from autologger.message_generator.message_content.fantasy.yield_fantasy_noun import yield_fantasy_noun
from autologger.message_generator.message_content.fantasy.yield_fantasy_verb import yield_fantasy_verb
from autologger.message_generator.message_content.fantasy.yield_fantasy_adjective import yield_fantasy_adjective

from autologger.message_generator.message_content.scifi.yield_scifi_noun import yield_scifi_noun
from autologger.message_generator.message_content.scifi.yield_scifi_verb import yield_scifi_verb
from autologger.message_generator.message_content.scifi.yield_scifi_adjective import yield_scifi_adjective

from autologger.message_generator.message_content.lovecraft.yield_lovecraft_noun import yield_lovecraft_noun
from autologger.message_generator.message_content.lovecraft.yield_lovecraft_verb import yield_lovecraft_verb
from autologger.message_generator.message_content.lovecraft.yield_lovecraft_adjective import yield_lovecraft_adjective

from autologger.message_generator.message_content.steampunk.yield_steampunk_noun import yield_steampunk_noun
from autologger.message_generator.message_content.steampunk.yield_steampunk_verb import yield_steampunk_verb
from autologger.message_generator.message_content.steampunk.yield_steampunk_adjective import yield_steampunk_adjective

from autologger.message_generator.message_content.adventure.yield_adventure_noun import yield_adventure_noun
from autologger.message_generator.message_content.adventure.yield_adventure_verb import yield_adventure_verb
from autologger.message_generator.message_content.adventure.yield_adventure_adjective import yield_adventure_adjective


def generate_log_message(
    theme: str,
) -> Iterator[str]:
    """Yields compiled message strings.
    
    Use: `from random import seed` for reproducible messages

    Args:
        theme (str): _description_

    Yields:
        Iterator[str]: An iterator of compiled messages according to the provided theme
    """

    assert theme in {
        "fantasy",
        "scifi",
        "lovecraft",
        "steampunk",
        "adventure",
    }, "Please select a theme from the available options"

    if theme == "fantasy":
        verb = yield_fantasy_verb()
        adjective = yield_fantasy_adjective()
        noun = yield_fantasy_noun()
    elif theme == "scifi":
        verb = yield_scifi_verb()
        adjective = yield_scifi_adjective()
        noun = yield_scifi_noun()
    elif theme == "lovecraft":
        verb = yield_lovecraft_verb()
        adjective = yield_lovecraft_adjective()
        noun = yield_lovecraft_noun()
    elif theme == "steampunk":
        verb = yield_steampunk_verb()
        adjective = yield_steampunk_adjective()
        noun = yield_steampunk_noun()
    elif theme == "adventure":
        verb = yield_adventure_verb()
        adjective = yield_adventure_adjective()
        noun = yield_adventure_noun()
    else:
        raise KeyError("Requested theme not implemented")
    
    adjective_component = next(adjective) + " " if uniform(0, 1) < 0.5 else ""

    yield f"{next(verb)} the {adjective_component}{next(noun)}"

#!
# -*- coding: utf-8 -*-

from autologger.message_generator.generate_log_message import generate_log_message

print(
    next(
        generate_log_message(
            theme="scifi",
        )
    )
)

"""Generated from Smithy shape ``com.amazonaws.iamtoolbox#StatementEffect``."""

from typing import Literal, TypeAlias, cast

"""<p>The effect of a matched statement.</p>"""
StatementEffect: TypeAlias = Literal[
    "ALLOW",
    "DENY",
]


# --- restJson1 ser/de ---
def serialize_json(value: StatementEffect) -> str:
    return value


def deserialize_json(data: str) -> StatementEffect:
    return cast(StatementEffect, data)

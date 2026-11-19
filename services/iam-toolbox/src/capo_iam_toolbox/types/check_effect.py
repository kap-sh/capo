"""Generated from Smithy shape ``com.amazonaws.iamtoolbox#CheckEffect``."""

from typing import Literal, TypeAlias, cast

"""<p>Whether the check allowed the request, denied it explicitly or implicitly, or did not affect the outcome.</p>"""
CheckEffect: TypeAlias = Literal[
    "ALLOW",
    "NO_IMPACT",
    "IMPLICIT_DENY",
    "EXPLICIT_DENY",
]


# --- restJson1 ser/de ---
def serialize_json(value: CheckEffect) -> str:
    return value


def deserialize_json(data: str) -> CheckEffect:
    return cast(CheckEffect, data)

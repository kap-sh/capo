"""Generated from Smithy shape ``com.amazonaws.iamtoolbox#EvaluatedEffect``."""

from typing import Literal, TypeAlias, cast

"""<p>The result of a policy evaluation.</p>"""
EvaluatedEffect: TypeAlias = Literal[
    "ALLOW",
    "EXPLICIT_DENY",
    "IMPLICIT_DENY",
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluatedEffect) -> str:
    return value


def deserialize_json(data: str) -> EvaluatedEffect:
    return cast(EvaluatedEffect, data)

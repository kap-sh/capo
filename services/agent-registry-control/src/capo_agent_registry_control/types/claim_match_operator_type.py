"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#ClaimMatchOperatorType``."""

from typing import Literal, TypeAlias, cast

"""<p>The operator used to compare a claim value against the expected value during JWT validation.</p>"""
ClaimMatchOperatorType: TypeAlias = Literal[
    "EQUALS",
    "CONTAINS",
    "CONTAINS_ANY",
]


# --- restJson1 ser/de ---
def serialize_json(value: ClaimMatchOperatorType) -> str:
    return value


def deserialize_json(data: str) -> ClaimMatchOperatorType:
    return cast(ClaimMatchOperatorType, data)

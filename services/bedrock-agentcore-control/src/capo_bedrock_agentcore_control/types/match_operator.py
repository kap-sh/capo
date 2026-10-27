"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MatchOperator``."""

from typing import Literal, TypeAlias, cast

MatchOperator: TypeAlias = Literal[
    "StringEquals",
    "StringLike",
]


# --- restJson1 ser/de ---
def serialize_json(value: MatchOperator) -> str:
    return value


def deserialize_json(data: str) -> MatchOperator:
    return cast(MatchOperator, data)

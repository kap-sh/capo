"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailContextualGroundingTierName``."""

from typing import Literal, TypeAlias, cast

GuardrailContextualGroundingTierName: TypeAlias = Literal[
    "CLASSIC",
    "STANDARD",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContextualGroundingTierName) -> str:
    return value


def deserialize_json(data: str) -> GuardrailContextualGroundingTierName:
    return cast(GuardrailContextualGroundingTierName, data)

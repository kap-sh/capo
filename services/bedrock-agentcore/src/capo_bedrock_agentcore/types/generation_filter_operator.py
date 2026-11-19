"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GenerationFilterOperator``."""

from typing import Literal, TypeAlias, cast

"""<p>How a filter compares a value.</p>"""
GenerationFilterOperator: TypeAlias = Literal[
    "Equals",
    "NotEquals",
    "GreaterThan",
    "LessThan",
    "GreaterThanOrEqual",
    "LessThanOrEqual",
    "Contains",
    "NotContains",
]


# --- restJson1 ser/de ---
def serialize_json(value: GenerationFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> GenerationFilterOperator:
    return cast(GenerationFilterOperator, data)

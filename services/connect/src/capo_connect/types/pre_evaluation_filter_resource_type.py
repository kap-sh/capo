"""Generated from Smithy shape ``com.amazonaws.connect#PreEvaluationFilterResourceType``."""

from typing import Literal, TypeAlias, cast

PreEvaluationFilterResourceType: TypeAlias = Literal[
    "CONTACT",
    "CONTACT_EVALUATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: PreEvaluationFilterResourceType) -> str:
    return value


def deserialize_json(data: str) -> PreEvaluationFilterResourceType:
    return cast(PreEvaluationFilterResourceType, data)

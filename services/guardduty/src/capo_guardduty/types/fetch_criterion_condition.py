"""Generated from Smithy shape ``com.amazonaws.guardduty#FetchCriterionCondition``."""

from typing import Literal, TypeAlias, cast

FetchCriterionCondition: TypeAlias = Literal[
    "EQUALS",
    "NOT_EQUALS",
    "GREATER_THAN",
    "GREATER_THAN_OR_EQUAL",
    "LESS_THAN",
    "LESS_THAN_OR_EQUAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: FetchCriterionCondition) -> str:
    return value


def deserialize_json(data: str) -> FetchCriterionCondition:
    return cast(FetchCriterionCondition, data)

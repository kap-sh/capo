"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormItemSourceValuesComparator``."""

from typing import Literal, TypeAlias, cast

EvaluationFormItemSourceValuesComparator: TypeAlias = Literal[
    "IN",
    "NOT_IN",
    "ALL_IN",
    "EXACT",
    "GREATER_THAN",
    "LESS_THAN",
    "GREATER_THAN_OR_EQUAL_TO",
    "LESS_THAN_OR_EQUAL_TO",
    "EQUAL_TO",
    "NOT_EQUAL_TO",
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormItemSourceValuesComparator) -> str:
    return value


def deserialize_json(data: str) -> EvaluationFormItemSourceValuesComparator:
    return cast(EvaluationFormItemSourceValuesComparator, data)

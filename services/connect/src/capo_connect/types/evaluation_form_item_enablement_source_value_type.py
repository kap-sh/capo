"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormItemEnablementSourceValueType``."""

from typing import Literal, TypeAlias, cast

EvaluationFormItemEnablementSourceValueType: TypeAlias = Literal[
    "OPTION_REF_ID",
    "STRING_VALUE",
    "NUMERIC_VALUE",
    "BOOLEAN_VALUE",
    "DATETIME_VALUE",
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormItemEnablementSourceValueType) -> str:
    return value


def deserialize_json(data: str) -> EvaluationFormItemEnablementSourceValueType:
    return cast(EvaluationFormItemEnablementSourceValueType, data)

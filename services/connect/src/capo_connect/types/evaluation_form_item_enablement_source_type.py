"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormItemEnablementSourceType``."""

from typing import Literal, TypeAlias, cast

EvaluationFormItemEnablementSourceType: TypeAlias = Literal[
    "QUESTION_REF_ID",
    "CONTACT",
    "EVALUATION_METADATA",
    "FORM_METADATA",
    "AI_METRICS",
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormItemEnablementSourceType) -> str:
    return value


def deserialize_json(data: str) -> EvaluationFormItemEnablementSourceType:
    return cast(EvaluationFormItemEnablementSourceType, data)

"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationEnablementStatus``."""

from typing import Literal, TypeAlias, cast

EvaluationEnablementStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationEnablementStatus) -> str:
    return value


def deserialize_json(data: str) -> EvaluationEnablementStatus:
    return cast(EvaluationEnablementStatus, data)

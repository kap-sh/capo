"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationItemResolutionStatus``."""

from typing import Literal, TypeAlias, cast

EvaluationItemResolutionStatus: TypeAlias = Literal[
    "PENDING",
    "RESOLVED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationItemResolutionStatus) -> str:
    return value


def deserialize_json(data: str) -> EvaluationItemResolutionStatus:
    return cast(EvaluationItemResolutionStatus, data)

"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormQuestionAutomationAnswerSourceType``."""

from typing import Literal, TypeAlias, cast

EvaluationFormQuestionAutomationAnswerSourceType: TypeAlias = Literal[
    "CONTACT_LENS_DATA",
    "GEN_AI",
    "CONDITION",
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormQuestionAutomationAnswerSourceType) -> str:
    return value


def deserialize_json(data: str) -> EvaluationFormQuestionAutomationAnswerSourceType:
    return cast(EvaluationFormQuestionAutomationAnswerSourceType, data)

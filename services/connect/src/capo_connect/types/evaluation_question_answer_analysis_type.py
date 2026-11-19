"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationQuestionAnswerAnalysisType``."""

from typing import Literal, TypeAlias, cast

EvaluationQuestionAnswerAnalysisType: TypeAlias = Literal[
    "CONTACT_LENS_DATA",
    "GEN_AI",
    "CONDITION",
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationQuestionAnswerAnalysisType) -> str:
    return value


def deserialize_json(data: str) -> EvaluationQuestionAnswerAnalysisType:
    return cast(EvaluationQuestionAnswerAnalysisType, data)

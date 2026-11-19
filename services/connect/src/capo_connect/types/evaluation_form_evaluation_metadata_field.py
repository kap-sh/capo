"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormEvaluationMetadataField``."""

from typing import Literal, TypeAlias, cast

EvaluationFormEvaluationMetadataField: TypeAlias = Literal["EVALUATION_TYPE",]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormEvaluationMetadataField) -> str:
    return value


def deserialize_json(data: str) -> EvaluationFormEvaluationMetadataField:
    return cast(EvaluationFormEvaluationMetadataField, data)

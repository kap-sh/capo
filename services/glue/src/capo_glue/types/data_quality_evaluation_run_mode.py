"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityEvaluationRunMode``."""

from typing import Literal, TypeAlias, cast

DataQualityEvaluationRunMode: TypeAlias = Literal[
    "ON_DEMAND",
    "EVALUATION_CONFIG",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityEvaluationRunMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataQualityEvaluationRunMode:
    return cast(DataQualityEvaluationRunMode, data)

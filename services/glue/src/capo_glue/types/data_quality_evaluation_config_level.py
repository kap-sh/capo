"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityEvaluationConfigLevel``."""

from typing import Literal, TypeAlias, cast

DataQualityEvaluationConfigLevel: TypeAlias = Literal[
    "CATALOG",
    "DATABASE",
    "TABLE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityEvaluationConfigLevel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataQualityEvaluationConfigLevel:
    return cast(DataQualityEvaluationConfigLevel, data)

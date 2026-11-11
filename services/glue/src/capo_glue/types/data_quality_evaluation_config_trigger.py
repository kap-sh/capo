"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityEvaluationConfigTrigger``."""

from typing import Literal, TypeAlias, cast

DataQualityEvaluationConfigTrigger: TypeAlias = Literal[
    "ONCE",
    "SCHEDULE",
    "METADATA_CHANGE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityEvaluationConfigTrigger) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataQualityEvaluationConfigTrigger:
    return cast(DataQualityEvaluationConfigTrigger, data)

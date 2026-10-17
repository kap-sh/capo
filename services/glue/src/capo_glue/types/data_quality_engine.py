"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityEngine``."""

from typing import Literal, TypeAlias, cast

DataQualityEngine: TypeAlias = Literal[
    "SPARK",
    "PYTHON",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityEngine) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataQualityEngine:
    return cast(DataQualityEngine, data)

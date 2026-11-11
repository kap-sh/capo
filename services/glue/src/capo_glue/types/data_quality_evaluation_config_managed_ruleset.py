"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityEvaluationConfigManagedRuleset``."""

from typing import Literal, TypeAlias, cast

DataQualityEvaluationConfigManagedRuleset: TypeAlias = Literal[
    "SIMPLE",
    "ADVANCED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityEvaluationConfigManagedRuleset) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataQualityEvaluationConfigManagedRuleset:
    return cast(DataQualityEvaluationConfigManagedRuleset, data)

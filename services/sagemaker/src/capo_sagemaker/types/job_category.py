"""Generated from Smithy shape ``com.amazonaws.sagemaker#JobCategory``."""

from typing import Literal, TypeAlias, cast

JobCategory: TypeAlias = Literal[
    "AgentRFT",
    "SyntheticDataGeneration",
    "DataQualityEvaluation",
    "AgentRFTEvaluation",
    "DataTransformation",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobCategory) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> JobCategory:
    return cast(JobCategory, data)

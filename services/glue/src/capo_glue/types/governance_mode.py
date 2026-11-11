"""Generated from Smithy shape ``com.amazonaws.glue#GovernanceMode``."""

from typing import Literal, TypeAlias, cast

GovernanceMode: TypeAlias = Literal[
    "IAM_ONLY",
    "LAKE_FORMATION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GovernanceMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GovernanceMode:
    return cast(GovernanceMode, data)

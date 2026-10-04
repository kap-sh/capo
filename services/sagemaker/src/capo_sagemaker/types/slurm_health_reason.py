"""Generated from Smithy shape ``com.amazonaws.sagemaker#SlurmHealthReason``."""

from typing import Literal, TypeAlias, cast

SlurmHealthReason: TypeAlias = Literal[
    "DaemonDown",
    "DaemonDisabled",
    "DbUnreachable",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SlurmHealthReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SlurmHealthReason:
    return cast(SlurmHealthReason, data)

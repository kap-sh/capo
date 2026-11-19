"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ReplicaRestrictionType``."""

from typing import Literal, TypeAlias, cast

ReplicaRestrictionType: TypeAlias = Literal[
    "SameOrg",
    "NoRestriction",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicaRestrictionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReplicaRestrictionType:
    return cast(ReplicaRestrictionType, data)

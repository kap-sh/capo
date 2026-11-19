"""Generated from Smithy shape ``com.amazonaws.shield#ProactiveEngagementStatus``."""

from typing import Literal, TypeAlias, cast

ProactiveEngagementStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "PENDING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProactiveEngagementStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProactiveEngagementStatus:
    return cast(ProactiveEngagementStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProactiveEngagementStatus) -> str:
    return value


def deserialize_cbor(data: str) -> ProactiveEngagementStatus:
    return cast(ProactiveEngagementStatus, data)

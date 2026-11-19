"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#InstanceInterruptionBehaviorEnum``."""

from typing import Literal, TypeAlias, cast

InstanceInterruptionBehaviorEnum: TypeAlias = Literal[
    "hibernate",
    "stop",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceInterruptionBehaviorEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InstanceInterruptionBehaviorEnum:
    return cast(InstanceInterruptionBehaviorEnum, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InstanceInterruptionBehaviorEnum) -> str:
    return value


def deserialize_cbor(data: str) -> InstanceInterruptionBehaviorEnum:
    return cast(InstanceInterruptionBehaviorEnum, data)

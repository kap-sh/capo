"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#AutoRecoveryEnum``."""

from typing import Literal, TypeAlias, cast

AutoRecoveryEnum: TypeAlias = Literal[
    "disabled",
    "default",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutoRecoveryEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AutoRecoveryEnum:
    return cast(AutoRecoveryEnum, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AutoRecoveryEnum) -> str:
    return value


def deserialize_cbor(data: str) -> AutoRecoveryEnum:
    return cast(AutoRecoveryEnum, data)

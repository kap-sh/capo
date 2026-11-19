"""Generated from Smithy shape ``com.amazonaws.gamelift#ProtectionPolicy``."""

from typing import Literal, TypeAlias, cast

ProtectionPolicy: TypeAlias = Literal[
    "NoProtection",
    "FullProtection",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtectionPolicy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProtectionPolicy:
    return cast(ProtectionPolicy, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProtectionPolicy) -> str:
    return value


def deserialize_cbor(data: str) -> ProtectionPolicy:
    return cast(ProtectionPolicy, data)

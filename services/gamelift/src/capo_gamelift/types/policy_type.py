"""Generated from Smithy shape ``com.amazonaws.gamelift#PolicyType``."""

from typing import Literal, TypeAlias, cast

PolicyType: TypeAlias = Literal[
    "RuleBased",
    "TargetBased",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PolicyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PolicyType:
    return cast(PolicyType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PolicyType) -> str:
    return value


def deserialize_cbor(data: str) -> PolicyType:
    return cast(PolicyType, data)

"""Generated from Smithy shape ``com.amazonaws.codedeploy#TargetLabel``."""

from typing import Literal, TypeAlias, cast

TargetLabel: TypeAlias = Literal[
    "Blue",
    "Green",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetLabel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TargetLabel:
    return cast(TargetLabel, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TargetLabel) -> str:
    return value


def deserialize_cbor(data: str) -> TargetLabel:
    return cast(TargetLabel, data)

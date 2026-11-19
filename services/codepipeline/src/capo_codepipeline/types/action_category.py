"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionCategory``."""

from typing import Literal, TypeAlias, cast

ActionCategory: TypeAlias = Literal[
    "Source",
    "Build",
    "Deploy",
    "Test",
    "Invoke",
    "Approval",
    "Compute",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionCategory) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ActionCategory:
    return cast(ActionCategory, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ActionCategory) -> str:
    return value


def deserialize_cbor(data: str) -> ActionCategory:
    return cast(ActionCategory, data)

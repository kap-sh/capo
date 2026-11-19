"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionOwner``."""

from typing import Literal, TypeAlias, cast

ActionOwner: TypeAlias = Literal[
    "AWS",
    "ThirdParty",
    "Custom",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionOwner) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ActionOwner:
    return cast(ActionOwner, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ActionOwner) -> str:
    return value


def deserialize_cbor(data: str) -> ActionOwner:
    return cast(ActionOwner, data)

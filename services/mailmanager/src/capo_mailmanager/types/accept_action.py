"""Generated from Smithy shape ``com.amazonaws.mailmanager#AcceptAction``."""

from typing import Literal, TypeAlias, cast

AcceptAction: TypeAlias = Literal[
    "ALLOW",
    "DENY",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AcceptAction) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AcceptAction:
    return cast(AcceptAction, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AcceptAction) -> str:
    return value


def deserialize_cbor(data: str) -> AcceptAction:
    return cast(AcceptAction, data)

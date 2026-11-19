"""Generated from Smithy shape ``com.amazonaws.shield#AutoRenew``."""

from typing import Literal, TypeAlias, cast

AutoRenew: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoRenew) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoRenew:
    return cast(AutoRenew, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AutoRenew) -> str:
    return value


def deserialize_cbor(data: str) -> AutoRenew:
    return cast(AutoRenew, data)

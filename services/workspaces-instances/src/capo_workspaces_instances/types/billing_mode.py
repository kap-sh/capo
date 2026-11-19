"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#BillingMode``."""

from typing import Literal, TypeAlias, cast

BillingMode: TypeAlias = Literal[
    "MONTHLY",
    "HOURLY",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BillingMode:
    return cast(BillingMode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BillingMode) -> str:
    return value


def deserialize_cbor(data: str) -> BillingMode:
    return cast(BillingMode, data)

"""Generated from Smithy shape ``com.amazonaws.directconnect#RequestBillingMode``."""

from typing import Literal, TypeAlias, cast

RequestBillingMode: TypeAlias = Literal[
    "PayAsYouGo",
    "FlatRateTier1",
    "FlatRateTier2",
    "FlatRateTier3",
    "FlatRateTier4",
    "FlatRateTier5",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RequestBillingMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RequestBillingMode:
    return cast(RequestBillingMode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RequestBillingMode) -> str:
    return value


def deserialize_cbor(data: str) -> RequestBillingMode:
    return cast(RequestBillingMode, data)

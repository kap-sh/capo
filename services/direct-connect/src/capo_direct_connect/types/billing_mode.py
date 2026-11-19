"""Generated from Smithy shape ``com.amazonaws.directconnect#BillingMode``."""

from typing import Literal, TypeAlias, cast

BillingMode: TypeAlias = Literal[
    "PayAsYouGo",
    "FlatRateTier1",
    "FlatRateTier2",
    "FlatRateTier3",
    "FlatRateTier4",
    "FlatRateTier5",
    "PortPairFlatRateTier1",
    "PortPairFlatRateTier2",
    "PortPairFlatRateTier3",
    "PortPairFlatRateTier4",
    "PortPairFlatRateTier5",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BillingMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BillingMode:
    return cast(BillingMode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BillingMode) -> str:
    return value


def deserialize_cbor(data: str) -> BillingMode:
    return cast(BillingMode, data)

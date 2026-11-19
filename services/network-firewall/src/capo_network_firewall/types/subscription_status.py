"""Generated from Smithy shape ``com.amazonaws.networkfirewall#SubscriptionStatus``."""

from typing import Literal, TypeAlias, cast

SubscriptionStatus: TypeAlias = Literal[
    "NOT_SUBSCRIBED",
    "SUBSCRIBED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SubscriptionStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SubscriptionStatus:
    return cast(SubscriptionStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SubscriptionStatus) -> str:
    return value


def deserialize_cbor(data: str) -> SubscriptionStatus:
    return cast(SubscriptionStatus, data)

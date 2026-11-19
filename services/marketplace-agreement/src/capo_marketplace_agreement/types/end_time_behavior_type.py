"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#EndTimeBehaviorType``."""

from typing import Literal, TypeAlias, cast

EndTimeBehaviorType: TypeAlias = Literal[
    "RENEW",
    "REPLACE",
    "EXPIRE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EndTimeBehaviorType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EndTimeBehaviorType:
    return cast(EndTimeBehaviorType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EndTimeBehaviorType) -> str:
    return value


def deserialize_cbor(data: str) -> EndTimeBehaviorType:
    return cast(EndTimeBehaviorType, data)

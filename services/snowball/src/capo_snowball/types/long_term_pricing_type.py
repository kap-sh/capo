"""Generated from Smithy shape ``com.amazonaws.snowball#LongTermPricingType``."""

from typing import Literal, TypeAlias, cast

LongTermPricingType: TypeAlias = Literal[
    "OneYear",
    "ThreeYear",
    "OneMonth",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LongTermPricingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LongTermPricingType:
    return cast(LongTermPricingType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LongTermPricingType) -> str:
    return value


def deserialize_cbor(data: str) -> LongTermPricingType:
    return cast(LongTermPricingType, data)

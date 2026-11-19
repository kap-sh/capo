"""Generated from Smithy shape ``com.amazonaws.snowball#LongTermPricingIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_snowball.types.long_term_pricing_id

LongTermPricingIdList: TypeAlias = list[
    "capo_snowball.types.long_term_pricing_id.LongTermPricingId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LongTermPricingIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> LongTermPricingIdList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LongTermPricingIdList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> LongTermPricingIdList:
    return [item for item in data if item is not None]

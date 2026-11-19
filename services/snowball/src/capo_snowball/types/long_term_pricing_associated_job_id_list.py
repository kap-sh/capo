"""Generated from Smithy shape ``com.amazonaws.snowball#LongTermPricingAssociatedJobIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_snowball.types.job_id

LongTermPricingAssociatedJobIdList: TypeAlias = list["capo_snowball.types.job_id.JobId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LongTermPricingAssociatedJobIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> LongTermPricingAssociatedJobIdList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LongTermPricingAssociatedJobIdList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> LongTermPricingAssociatedJobIdList:
    return [item for item in data if item is not None]

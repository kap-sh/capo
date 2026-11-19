"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#BillingAdjustmentErrorCode``."""

from typing import Literal, TypeAlias, cast

BillingAdjustmentErrorCode: TypeAlias = Literal[
    "CONFLICT_EXCEPTION",
    "VALIDATION_EXCEPTION",
    "RESOURCE_NOT_FOUND_EXCEPTION",
    "INTERNAL_FAILURE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingAdjustmentErrorCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BillingAdjustmentErrorCode:
    return cast(BillingAdjustmentErrorCode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BillingAdjustmentErrorCode) -> str:
    return value


def deserialize_cbor(data: str) -> BillingAdjustmentErrorCode:
    return cast(BillingAdjustmentErrorCode, data)

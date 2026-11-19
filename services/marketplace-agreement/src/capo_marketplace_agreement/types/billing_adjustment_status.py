"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#BillingAdjustmentStatus``."""

from typing import Literal, TypeAlias, cast

BillingAdjustmentStatus: TypeAlias = Literal[
    "PENDING",
    "VALIDATION_FAILED",
    "COMPLETED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingAdjustmentStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BillingAdjustmentStatus:
    return cast(BillingAdjustmentStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BillingAdjustmentStatus) -> str:
    return value


def deserialize_cbor(data: str) -> BillingAdjustmentStatus:
    return cast(BillingAdjustmentStatus, data)

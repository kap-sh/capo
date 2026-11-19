"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#BillingAdjustmentReasonCode``."""

from typing import Literal, TypeAlias, cast

BillingAdjustmentReasonCode: TypeAlias = Literal[
    "INCORRECT_TERMS_ACCEPTED",
    "INCORRECT_METERING",
    "TEST_ENVIRONMENT_CHARGES",
    "ALTERNATIVE_PROCUREMENT_CHANNEL",
    "UNINTENDED_RENEWAL",
    "BUYER_DISSATISFACTION",
    "OTHER",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingAdjustmentReasonCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BillingAdjustmentReasonCode:
    return cast(BillingAdjustmentReasonCode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BillingAdjustmentReasonCode) -> str:
    return value


def deserialize_cbor(data: str) -> BillingAdjustmentReasonCode:
    return cast(BillingAdjustmentReasonCode, data)

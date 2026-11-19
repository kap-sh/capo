"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#PaymentRequestApprovalStrategy``."""

from typing import Literal, TypeAlias, cast

PaymentRequestApprovalStrategy: TypeAlias = Literal[
    "AUTO_APPROVE_ON_EXPIRATION",
    "WAIT_FOR_APPROVAL",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PaymentRequestApprovalStrategy) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PaymentRequestApprovalStrategy:
    return cast(PaymentRequestApprovalStrategy, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PaymentRequestApprovalStrategy) -> str:
    return value


def deserialize_cbor(data: str) -> PaymentRequestApprovalStrategy:
    return cast(PaymentRequestApprovalStrategy, data)

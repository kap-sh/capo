"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#PaymentRequestStatus``."""

from typing import Literal, TypeAlias, cast

PaymentRequestStatus: TypeAlias = Literal[
    "VALIDATING",
    "VALIDATION_FAILED",
    "PENDING_APPROVAL",
    "APPROVED",
    "REJECTED",
    "CANCELLED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PaymentRequestStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PaymentRequestStatus:
    return cast(PaymentRequestStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PaymentRequestStatus) -> str:
    return value


def deserialize_cbor(data: str) -> PaymentRequestStatus:
    return cast(PaymentRequestStatus, data)

"""Generated from Smithy shape ``com.amazonaws.route53domains#StatusFlag``."""

from typing import Literal, TypeAlias, cast

StatusFlag: TypeAlias = Literal[
    "PENDING_ACCEPTANCE",
    "PENDING_CUSTOMER_ACTION",
    "PENDING_AUTHORIZATION",
    "PENDING_PAYMENT_VERIFICATION",
    "PENDING_SUPPORT_CASE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StatusFlag) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StatusFlag:
    return cast(StatusFlag, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StatusFlag) -> str:
    return value


def deserialize_cbor(data: str) -> StatusFlag:
    return cast(StatusFlag, data)

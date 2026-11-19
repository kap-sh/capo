"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AccessDeniedExceptionReason``."""

from typing import Literal, TypeAlias, cast

AccessDeniedExceptionReason: TypeAlias = Literal[
    "INVALID_ACCOUNT_STATE",
    "DENIED_BY_PRIVATE_MARKETPLACE_POLICY",
    "FAILED_KYC_COMPLIANCE",
    "MISSING_MFA",
    "INVALID_ACCESS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccessDeniedExceptionReason) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AccessDeniedExceptionReason:
    return cast(AccessDeniedExceptionReason, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AccessDeniedExceptionReason) -> str:
    return value


def deserialize_cbor(data: str) -> AccessDeniedExceptionReason:
    return cast(AccessDeniedExceptionReason, data)

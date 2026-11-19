"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementEntitlementStatusReasonCode``."""

from typing import Literal, TypeAlias, cast

AgreementEntitlementStatusReasonCode: TypeAlias = Literal[
    "PROVISIONING_IN_PROGRESS",
    "FUTURE_START_DATE",
    "INVALID_PAYMENT_INSTRUMENT",
    "INCOMPATIBLE_CURRENCY",
    "ACCOUNT_SUSPENDED",
    "UNSUPPORTED_OPERATION",
    "AGREEMENT_INACTIVE",
    "AGREEMENT_ACTIVE",
    "PRODUCT_RESTRICTED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgreementEntitlementStatusReasonCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AgreementEntitlementStatusReasonCode:
    return cast(AgreementEntitlementStatusReasonCode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AgreementEntitlementStatusReasonCode) -> str:
    return value


def deserialize_cbor(data: str) -> AgreementEntitlementStatusReasonCode:
    return cast(AgreementEntitlementStatusReasonCode, data)

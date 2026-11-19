"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementCancellationRequestReasonCode``."""

from typing import Literal, TypeAlias, cast

AgreementCancellationRequestReasonCode: TypeAlias = Literal[
    "INCORRECT_TERMS_ACCEPTED",
    "REPLACING_AGREEMENT",
    "TEST_AGREEMENT",
    "ALTERNATIVE_PROCUREMENT_CHANNEL",
    "PRODUCT_DISCONTINUED",
    "UNINTENDED_RENEWAL",
    "BUYER_DISSATISFACTION",
    "OTHER",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgreementCancellationRequestReasonCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AgreementCancellationRequestReasonCode:
    return cast(AgreementCancellationRequestReasonCode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AgreementCancellationRequestReasonCode) -> str:
    return value


def deserialize_cbor(data: str) -> AgreementCancellationRequestReasonCode:
    return cast(AgreementCancellationRequestReasonCode, data)

"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementApprovalType``."""

from typing import Literal, TypeAlias, cast

AgreementApprovalType: TypeAlias = Literal["BUYER_AGREEMENT_APPROVAL",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgreementApprovalType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AgreementApprovalType:
    return cast(AgreementApprovalType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AgreementApprovalType) -> str:
    return value


def deserialize_cbor(data: str) -> AgreementApprovalType:
    return cast(AgreementApprovalType, data)

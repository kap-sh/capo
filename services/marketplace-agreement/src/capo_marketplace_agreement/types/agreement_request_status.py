"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementRequestStatus``."""

from typing import Literal, TypeAlias, cast

AgreementRequestStatus: TypeAlias = Literal[
    "DRAFT",
    "PENDING_APPROVAL",
    "APPROVED",
    "ACCEPTED",
    "REJECTED",
    "CANCELLED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgreementRequestStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AgreementRequestStatus:
    return cast(AgreementRequestStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AgreementRequestStatus) -> str:
    return value


def deserialize_cbor(data: str) -> AgreementRequestStatus:
    return cast(AgreementRequestStatus, data)

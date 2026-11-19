"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementCancellationRequestStatus``."""

from typing import Literal, TypeAlias, cast

AgreementCancellationRequestStatus: TypeAlias = Literal[
    "PENDING_APPROVAL",
    "APPROVED",
    "REJECTED",
    "CANCELLED",
    "VALIDATION_FAILED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgreementCancellationRequestStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AgreementCancellationRequestStatus:
    return cast(AgreementCancellationRequestStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AgreementCancellationRequestStatus) -> str:
    return value


def deserialize_cbor(data: str) -> AgreementCancellationRequestStatus:
    return cast(AgreementCancellationRequestStatus, data)

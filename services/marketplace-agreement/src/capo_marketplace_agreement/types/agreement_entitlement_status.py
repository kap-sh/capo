"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementEntitlementStatus``."""

from typing import Literal, TypeAlias, cast

AgreementEntitlementStatus: TypeAlias = Literal[
    "PROVISIONED",
    "SCHEDULED",
    "PENDING",
    "FAILED",
    "DEPROVISIONED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgreementEntitlementStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AgreementEntitlementStatus:
    return cast(AgreementEntitlementStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AgreementEntitlementStatus) -> str:
    return value


def deserialize_cbor(data: str) -> AgreementEntitlementStatus:
    return cast(AgreementEntitlementStatus, data)

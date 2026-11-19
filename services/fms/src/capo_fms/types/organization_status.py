"""Generated from Smithy shape ``com.amazonaws.fms#OrganizationStatus``."""

from typing import Literal, TypeAlias, cast

OrganizationStatus: TypeAlias = Literal[
    "ONBOARDING",
    "ONBOARDING_COMPLETE",
    "OFFBOARDING",
    "OFFBOARDING_COMPLETE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OrganizationStatus:
    return cast(OrganizationStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OrganizationStatus) -> str:
    return value


def deserialize_cbor(data: str) -> OrganizationStatus:
    return cast(OrganizationStatus, data)

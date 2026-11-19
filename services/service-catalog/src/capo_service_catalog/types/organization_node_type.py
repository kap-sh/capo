"""Generated from Smithy shape ``com.amazonaws.servicecatalog#OrganizationNodeType``."""

from typing import Literal, TypeAlias, cast

OrganizationNodeType: TypeAlias = Literal[
    "ORGANIZATION",
    "ORGANIZATIONAL_UNIT",
    "ACCOUNT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationNodeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OrganizationNodeType:
    return cast(OrganizationNodeType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OrganizationNodeType) -> str:
    return value


def deserialize_cbor(data: str) -> OrganizationNodeType:
    return cast(OrganizationNodeType, data)

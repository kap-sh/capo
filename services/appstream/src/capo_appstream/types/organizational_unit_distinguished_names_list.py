"""Generated from Smithy shape ``com.amazonaws.appstream#OrganizationalUnitDistinguishedNamesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.organizational_unit_distinguished_name

OrganizationalUnitDistinguishedNamesList: TypeAlias = list[
    "capo_appstream.types.organizational_unit_distinguished_name.OrganizationalUnitDistinguishedName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationalUnitDistinguishedNamesList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> OrganizationalUnitDistinguishedNamesList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OrganizationalUnitDistinguishedNamesList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> OrganizationalUnitDistinguishedNamesList:
    return [item for item in data if item is not None]

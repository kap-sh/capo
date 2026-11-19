"""Generated from Smithy shape ``com.amazonaws.fms#OrganizationalUnitIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.organizational_unit_id

OrganizationalUnitIdList: TypeAlias = list[
    "capo_fms.types.organizational_unit_id.OrganizationalUnitId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationalUnitIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> OrganizationalUnitIdList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OrganizationalUnitIdList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> OrganizationalUnitIdList:
    return [item for item in data if item is not None]

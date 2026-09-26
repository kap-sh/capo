"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#OrganizationalUnitIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_security_manager.types.organizational_unit_id

OrganizationalUnitIdList: TypeAlias = list[
    "capo_network_security_manager.types.organizational_unit_id.OrganizationalUnitId"
]


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationalUnitIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> OrganizationalUnitIdList:
    return [item for item in data if item is not None]

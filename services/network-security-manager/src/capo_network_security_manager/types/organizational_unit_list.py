"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#OrganizationalUnitList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_security_manager.types.organizational_unit

OrganizationalUnitList: TypeAlias = list[
    "capo_network_security_manager.types.organizational_unit.OrganizationalUnit"
]


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationalUnitList) -> list:
    return list(value)


def deserialize_json(data: list) -> OrganizationalUnitList:
    return [item for item in data if item is not None]

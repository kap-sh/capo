"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#OrganizationalUnitReferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_security_manager.types.organizational_unit_reference

OrganizationalUnitReferenceList: TypeAlias = list[
    "capo_network_security_manager.types.organizational_unit_reference.OrganizationalUnitReference"
]


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationalUnitReferenceList) -> list:
    import capo_network_security_manager.types.organizational_unit_reference

    out: list = []
    for item in value:
        out.append(
            capo_network_security_manager.types.organizational_unit_reference.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> OrganizationalUnitReferenceList:
    import capo_network_security_manager.types.organizational_unit_reference

    out: OrganizationalUnitReferenceList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_security_manager.types.organizational_unit_reference.deserialize_json(
                item
            )
        )
    return out

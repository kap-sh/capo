"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ResourceAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_security_manager.types.resource_association

ResourceAssociationList: TypeAlias = list[
    "capo_network_security_manager.types.resource_association.ResourceAssociation"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceAssociationList) -> list:
    import capo_network_security_manager.types.resource_association

    out: list = []
    for item in value:
        out.append(
            capo_network_security_manager.types.resource_association.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ResourceAssociationList:
    import capo_network_security_manager.types.resource_association

    out: ResourceAssociationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_security_manager.types.resource_association.deserialize_json(
                item
            )
        )
    return out

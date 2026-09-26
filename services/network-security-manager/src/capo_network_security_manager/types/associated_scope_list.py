"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#AssociatedScopeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_security_manager.types.associated_scope

AssociatedScopeList: TypeAlias = list[
    "capo_network_security_manager.types.associated_scope.AssociatedScope"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedScopeList) -> list:
    import capo_network_security_manager.types.associated_scope

    out: list = []
    for item in value:
        out.append(
            capo_network_security_manager.types.associated_scope.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AssociatedScopeList:
    import capo_network_security_manager.types.associated_scope

    out: AssociatedScopeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_security_manager.types.associated_scope.deserialize_json(item)
        )
    return out

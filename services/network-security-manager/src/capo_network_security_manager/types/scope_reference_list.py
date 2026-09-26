"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ScopeReferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_security_manager.types.scope_reference

ScopeReferenceList: TypeAlias = list[
    "capo_network_security_manager.types.scope_reference.ScopeReference"
]


# --- restJson1 ser/de ---
def serialize_json(value: ScopeReferenceList) -> list:
    import capo_network_security_manager.types.scope_reference

    out: list = []
    for item in value:
        out.append(
            capo_network_security_manager.types.scope_reference.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ScopeReferenceList:
    import capo_network_security_manager.types.scope_reference

    out: ScopeReferenceList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_security_manager.types.scope_reference.deserialize_json(item)
        )
    return out

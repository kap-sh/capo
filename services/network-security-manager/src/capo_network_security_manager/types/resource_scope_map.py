"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ResourceScopeMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_security_manager.types.resource_scope
    import capo_network_security_manager.types.scope_resource_type

ResourceScopeMap: TypeAlias = dict[
    "capo_network_security_manager.types.scope_resource_type.ScopeResourceType",
    "capo_network_security_manager.types.resource_scope.ResourceScope",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ResourceScopeMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_network_security_manager.types.resource_scope
        import capo_network_security_manager.types.scope_resource_type

        out[
            capo_network_security_manager.types.scope_resource_type.serialize_json(key)
        ] = capo_network_security_manager.types.resource_scope.serialize_json(value)
    return out


def deserialize_json(data: dict) -> ResourceScopeMap:
    out: ResourceScopeMap = {}
    for key, value in data.items():
        import capo_network_security_manager.types.scope_resource_type

        if value is None:
            continue
        import capo_network_security_manager.types.resource_scope

        out[
            capo_network_security_manager.types.scope_resource_type.deserialize_json(
                key
            )
        ] = capo_network_security_manager.types.resource_scope.deserialize_json(value)
    return out

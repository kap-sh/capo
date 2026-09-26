"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#DeploymentResourceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_security_manager.types.scope_resource_type

DeploymentResourceTypeList: TypeAlias = list[
    "capo_network_security_manager.types.scope_resource_type.ScopeResourceType"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentResourceTypeList) -> list:
    import capo_network_security_manager.types.scope_resource_type

    out: list = []
    for item in value:
        out.append(
            capo_network_security_manager.types.scope_resource_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DeploymentResourceTypeList:
    import capo_network_security_manager.types.scope_resource_type

    out: DeploymentResourceTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_security_manager.types.scope_resource_type.deserialize_json(
                item
            )
        )
    return out

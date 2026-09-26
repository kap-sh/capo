"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#DeploymentWarningList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_security_manager.types.deployment_warning_entry

DeploymentWarningList: TypeAlias = list[
    "capo_network_security_manager.types.deployment_warning_entry.DeploymentWarningEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentWarningList) -> list:
    import capo_network_security_manager.types.deployment_warning_entry

    out: list = []
    for item in value:
        out.append(
            capo_network_security_manager.types.deployment_warning_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DeploymentWarningList:
    import capo_network_security_manager.types.deployment_warning_entry

    out: DeploymentWarningList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_security_manager.types.deployment_warning_entry.deserialize_json(
                item
            )
        )
    return out

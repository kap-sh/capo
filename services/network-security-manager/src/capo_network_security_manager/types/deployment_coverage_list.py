"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#DeploymentCoverageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_security_manager.types.deployment_coverage_entry

DeploymentCoverageList: TypeAlias = list[
    "capo_network_security_manager.types.deployment_coverage_entry.DeploymentCoverageEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentCoverageList) -> list:
    import capo_network_security_manager.types.deployment_coverage_entry

    out: list = []
    for item in value:
        out.append(
            capo_network_security_manager.types.deployment_coverage_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DeploymentCoverageList:
    import capo_network_security_manager.types.deployment_coverage_entry

    out: DeploymentCoverageList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_security_manager.types.deployment_coverage_entry.deserialize_json(
                item
            )
        )
    return out

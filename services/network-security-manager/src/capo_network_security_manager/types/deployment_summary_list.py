"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#DeploymentSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_security_manager.types.deployment_summary

DeploymentSummaryList: TypeAlias = list[
    "capo_network_security_manager.types.deployment_summary.DeploymentSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentSummaryList) -> list:
    import capo_network_security_manager.types.deployment_summary

    out: list = []
    for item in value:
        out.append(
            capo_network_security_manager.types.deployment_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DeploymentSummaryList:
    import capo_network_security_manager.types.deployment_summary

    out: DeploymentSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_security_manager.types.deployment_summary.deserialize_json(
                item
            )
        )
    return out

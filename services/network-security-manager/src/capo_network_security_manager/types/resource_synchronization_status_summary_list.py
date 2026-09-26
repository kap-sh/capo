"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ResourceSynchronizationStatusSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_security_manager.types.resource_synchronization_status_summary

ResourceSynchronizationStatusSummaryList: TypeAlias = list[
    "capo_network_security_manager.types.resource_synchronization_status_summary.ResourceSynchronizationStatusSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceSynchronizationStatusSummaryList) -> list:
    import capo_network_security_manager.types.resource_synchronization_status_summary

    out: list = []
    for item in value:
        out.append(
            capo_network_security_manager.types.resource_synchronization_status_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ResourceSynchronizationStatusSummaryList:
    import capo_network_security_manager.types.resource_synchronization_status_summary

    out: ResourceSynchronizationStatusSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_security_manager.types.resource_synchronization_status_summary.deserialize_json(
                item
            )
        )
    return out

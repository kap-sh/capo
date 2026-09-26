"""Generated from Smithy shape ``com.amazonaws.agentregistry#DiscoverableRegistryRecordSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_agent_registry.types.discoverable_registry_record_summary

DiscoverableRegistryRecordSummaryList: TypeAlias = list[
    "capo_agent_registry.types.discoverable_registry_record_summary.DiscoverableRegistryRecordSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DiscoverableRegistryRecordSummaryList) -> list:
    import capo_agent_registry.types.discoverable_registry_record_summary

    out: list = []
    for item in value:
        out.append(
            capo_agent_registry.types.discoverable_registry_record_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DiscoverableRegistryRecordSummaryList:
    import capo_agent_registry.types.discoverable_registry_record_summary

    out: DiscoverableRegistryRecordSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_agent_registry.types.discoverable_registry_record_summary.deserialize_json(
                item
            )
        )
    return out

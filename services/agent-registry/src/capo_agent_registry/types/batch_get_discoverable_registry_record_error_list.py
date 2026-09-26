"""Generated from Smithy shape ``com.amazonaws.agentregistry#BatchGetDiscoverableRegistryRecordErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_agent_registry.types.batch_get_discoverable_registry_record_error

BatchGetDiscoverableRegistryRecordErrorList: TypeAlias = list[
    "capo_agent_registry.types.batch_get_discoverable_registry_record_error.BatchGetDiscoverableRegistryRecordError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetDiscoverableRegistryRecordErrorList) -> list:
    import capo_agent_registry.types.batch_get_discoverable_registry_record_error

    out: list = []
    for item in value:
        out.append(
            capo_agent_registry.types.batch_get_discoverable_registry_record_error.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchGetDiscoverableRegistryRecordErrorList:
    import capo_agent_registry.types.batch_get_discoverable_registry_record_error

    out: BatchGetDiscoverableRegistryRecordErrorList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_agent_registry.types.batch_get_discoverable_registry_record_error.deserialize_json(
                item
            )
        )
    return out

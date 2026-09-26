"""Generated from Smithy shape ``com.amazonaws.agentregistry#BatchGetDiscoverableRegistryRecordRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_agent_registry.errors import DeserializationError

if TYPE_CHECKING:
    import capo_agent_registry.types.registry_records_entry_list


class BatchGetDiscoverableRegistryRecordRequest(TypedDict, closed=True):
    entries: (
        "capo_agent_registry.types.registry_records_entry_list.RegistryRecordsEntryList"
    )
    """<p> The registry-scoped groups of record IDs to retrieve. Currently, you can specify exactly one entry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetDiscoverableRegistryRecordRequest) -> dict:
    out: dict = {}
    import capo_agent_registry.types.registry_records_entry_list

    out["entries"] = (
        capo_agent_registry.types.registry_records_entry_list.serialize_json(
            value["entries"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetDiscoverableRegistryRecordRequest:
    out: BatchGetDiscoverableRegistryRecordRequest = {}  # type: ignore[typeddict-item]
    if data.get("entries") is not None:
        import capo_agent_registry.types.registry_records_entry_list

        out["entries"] = (
            capo_agent_registry.types.registry_records_entry_list.deserialize_json(
                data["entries"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetDiscoverableRegistryRecordRequest.entries required"
        )
    return out

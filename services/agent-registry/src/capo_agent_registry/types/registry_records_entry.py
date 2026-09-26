"""Generated from Smithy shape ``com.amazonaws.agentregistry#RegistryRecordsEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_agent_registry.errors import DeserializationError

if TYPE_CHECKING:
    import capo_agent_registry.types.registry_identifier
    import capo_agent_registry.types.registry_record_id_list


class RegistryRecordsEntry(TypedDict, closed=True):
    registry_id: "capo_agent_registry.types.registry_identifier.RegistryIdentifier"
    """<p> The identifier of the registry to retrieve the records from. You can provide either the full Amazon Resource Name (ARN) or the registry ID.</p>"""
    record_ids: "capo_agent_registry.types.registry_record_id_list.RegistryRecordIdList"
    """<p> The record IDs to retrieve from the registry. You can specify 1 through 100 record IDs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegistryRecordsEntry) -> dict:
    out: dict = {}
    out["registryId"] = value["registry_id"]
    import capo_agent_registry.types.registry_record_id_list

    out["recordIds"] = capo_agent_registry.types.registry_record_id_list.serialize_json(
        value["record_ids"]
    )
    return out


def deserialize_json(data: dict) -> RegistryRecordsEntry:
    out: RegistryRecordsEntry = {}  # type: ignore[typeddict-item]
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    else:
        raise DeserializationError("RegistryRecordsEntry.registry_id required")
    if data.get("recordIds") is not None:
        import capo_agent_registry.types.registry_record_id_list

        out["record_ids"] = (
            capo_agent_registry.types.registry_record_id_list.deserialize_json(
                data["recordIds"]
            )
        )
    else:
        raise DeserializationError("RegistryRecordsEntry.record_ids required")
    return out

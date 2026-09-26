"""Generated from Smithy shape ``com.amazonaws.agentregistry#BatchGetDiscoverableRegistryRecordResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_agent_registry.errors import DeserializationError

if TYPE_CHECKING:
    import capo_agent_registry.types.batch_get_discoverable_registry_record_error_list
    import capo_agent_registry.types.registry_record_summary_list


class BatchGetDiscoverableRegistryRecordResponse(TypedDict, closed=True):
    registry_records: "capo_agent_registry.types.registry_record_summary_list.RegistryRecordSummaryList"
    """<p> The records that were successfully retrieved. Each record correlates to the request by its <code>recordId</code>.</p>"""
    errors: "capo_agent_registry.types.batch_get_discoverable_registry_record_error_list.BatchGetDiscoverableRegistryRecordErrorList"
    """<p> The per-record errors for records that could not be retrieved. This list is empty when all requested records were returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetDiscoverableRegistryRecordResponse) -> dict:
    out: dict = {}
    import capo_agent_registry.types.registry_record_summary_list

    out["registryRecords"] = (
        capo_agent_registry.types.registry_record_summary_list.serialize_json(
            value["registry_records"]
        )
    )
    import capo_agent_registry.types.batch_get_discoverable_registry_record_error_list

    out["errors"] = (
        capo_agent_registry.types.batch_get_discoverable_registry_record_error_list.serialize_json(
            value["errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetDiscoverableRegistryRecordResponse:
    out: BatchGetDiscoverableRegistryRecordResponse = {}  # type: ignore[typeddict-item]
    if data.get("registryRecords") is not None:
        import capo_agent_registry.types.registry_record_summary_list

        out["registry_records"] = (
            capo_agent_registry.types.registry_record_summary_list.deserialize_json(
                data["registryRecords"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetDiscoverableRegistryRecordResponse.registry_records required"
        )
    if data.get("errors") is not None:
        import capo_agent_registry.types.batch_get_discoverable_registry_record_error_list

        out["errors"] = (
            capo_agent_registry.types.batch_get_discoverable_registry_record_error_list.deserialize_json(
                data["errors"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetDiscoverableRegistryRecordResponse.errors required"
        )
    return out

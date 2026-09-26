"""Generated from Smithy shape ``com.amazonaws.agentregistry#SearchDiscoverableRegistryRecordsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_agent_registry.errors import DeserializationError

if TYPE_CHECKING:
    import capo_agent_registry.types.registry_record_summary_list


class SearchDiscoverableRegistryRecordsResponse(TypedDict, closed=True):
    registry_records: "capo_agent_registry.types.registry_record_summary_list.RegistryRecordSummaryList"
    """<p> The registry records that match the search query, ordered by relevance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchDiscoverableRegistryRecordsResponse) -> dict:
    out: dict = {}
    import capo_agent_registry.types.registry_record_summary_list

    out["registryRecords"] = (
        capo_agent_registry.types.registry_record_summary_list.serialize_json(
            value["registry_records"]
        )
    )
    return out


def deserialize_json(data: dict) -> SearchDiscoverableRegistryRecordsResponse:
    out: SearchDiscoverableRegistryRecordsResponse = {}  # type: ignore[typeddict-item]
    if data.get("registryRecords") is not None:
        import capo_agent_registry.types.registry_record_summary_list

        out["registry_records"] = (
            capo_agent_registry.types.registry_record_summary_list.deserialize_json(
                data["registryRecords"]
            )
        )
    else:
        raise DeserializationError(
            "SearchDiscoverableRegistryRecordsResponse.registry_records required"
        )
    return out

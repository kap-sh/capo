"""Generated from Smithy shape ``com.amazonaws.agentregistry#SearchDiscoverableRegistryRecordsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

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
        out["registry_records"] = []
    return out


def redact_sensitive(
    value: SearchDiscoverableRegistryRecordsResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "registry_records" in value:
        import capo_agent_registry.types.registry_record_summary_list

        out["registry_records"] = (
            capo_agent_registry.types.registry_record_summary_list.redact_sensitive(
                value["registry_records"]
            )
        )
    return out

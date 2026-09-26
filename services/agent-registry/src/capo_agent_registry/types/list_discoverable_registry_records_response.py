"""Generated from Smithy shape ``com.amazonaws.agentregistry#ListDiscoverableRegistryRecordsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_agent_registry.errors import DeserializationError

if TYPE_CHECKING:
    import capo_agent_registry.types.discoverable_registry_record_summary_list


class ListDiscoverableRegistryRecordsResponse(TypedDict, closed=True):
    registry_records: "capo_agent_registry.types.discoverable_registry_record_summary_list.DiscoverableRegistryRecordSummaryList"
    """<p> The page of discoverable registry record summaries.</p>"""
    next_token: NotRequired["str"]
    """<p> The pagination token to pass to a subsequent request to retrieve the next page of results. This field is absent when there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDiscoverableRegistryRecordsResponse) -> dict:
    out: dict = {}
    import capo_agent_registry.types.discoverable_registry_record_summary_list

    out["registryRecords"] = (
        capo_agent_registry.types.discoverable_registry_record_summary_list.serialize_json(
            value["registry_records"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDiscoverableRegistryRecordsResponse:
    out: ListDiscoverableRegistryRecordsResponse = {}  # type: ignore[typeddict-item]
    if data.get("registryRecords") is not None:
        import capo_agent_registry.types.discoverable_registry_record_summary_list

        out["registry_records"] = (
            capo_agent_registry.types.discoverable_registry_record_summary_list.deserialize_json(
                data["registryRecords"]
            )
        )
    else:
        raise DeserializationError(
            "ListDiscoverableRegistryRecordsResponse.registry_records required"
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

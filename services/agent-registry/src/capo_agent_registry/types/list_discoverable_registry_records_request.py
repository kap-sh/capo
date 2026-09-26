"""Generated from Smithy shape ``com.amazonaws.agentregistry#ListDiscoverableRegistryRecordsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry.types.registry_identifier
    import capo_agent_registry.types.registry_record_filter_list


class ListDiscoverableRegistryRecordsRequest(TypedDict, closed=True):
    registry_id: "capo_agent_registry.types.registry_identifier.RegistryIdentifier"
    """<p> The identifier of the registry whose discoverable records are listed. You can provide either the full Amazon Resource Name (ARN) or the registry ID.</p>"""
    max_results: NotRequired["int"]
    """<p> The maximum number of records to return in a single page. Valid values are 1 through 100.</p>"""
    next_token: NotRequired["str"]
    """<p> The pagination token returned by a previous request. Use this value to retrieve the next page of results.</p>"""
    filters: NotRequired[
        "capo_agent_registry.types.registry_record_filter_list.RegistryRecordFilterList"
    ]
    """<p> The filters to apply to the discoverable registry record list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDiscoverableRegistryRecordsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "filters" in value:
        import capo_agent_registry.types.registry_record_filter_list

        out["filters"] = (
            capo_agent_registry.types.registry_record_filter_list.serialize_json(
                value["filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListDiscoverableRegistryRecordsRequest:
    out: ListDiscoverableRegistryRecordsRequest = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("filters") is not None:
        import capo_agent_registry.types.registry_record_filter_list

        out["filters"] = (
            capo_agent_registry.types.registry_record_filter_list.deserialize_json(
                data["filters"]
            )
        )
    return out

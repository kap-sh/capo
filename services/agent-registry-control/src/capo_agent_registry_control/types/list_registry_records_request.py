"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#ListRegistryRecordsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.max_results
    import capo_agent_registry_control.types.next_token
    import capo_agent_registry_control.types.registry_identifier
    import capo_agent_registry_control.types.registry_record_filter_list


class ListRegistryRecordsRequest(TypedDict, closed=True):
    registry_id: (
        "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier"
    )
    """<p>The identifier of the registry to list records from (ARN or ID)</p>"""
    max_results: NotRequired["capo_agent_registry_control.types.max_results.MaxResults"]
    """<p>Maximum number of records to return</p>"""
    next_token: NotRequired["capo_agent_registry_control.types.next_token.NextToken"]
    """<p>Token for pagination</p>"""
    filters: NotRequired[
        "capo_agent_registry_control.types.registry_record_filter_list.RegistryRecordFilterList"
    ]
    """<p>Filters to apply to the registry record list</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRegistryRecordsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "filters" in value:
        import capo_agent_registry_control.types.registry_record_filter_list

        out["filters"] = (
            capo_agent_registry_control.types.registry_record_filter_list.serialize_json(
                value["filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListRegistryRecordsRequest:
    out: ListRegistryRecordsRequest = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("filters") is not None:
        import capo_agent_registry_control.types.registry_record_filter_list

        out["filters"] = (
            capo_agent_registry_control.types.registry_record_filter_list.deserialize_json(
                data["filters"]
            )
        )
    return out

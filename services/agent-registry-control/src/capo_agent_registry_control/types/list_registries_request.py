"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#ListRegistriesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.max_results
    import capo_agent_registry_control.types.next_token
    import capo_agent_registry_control.types.registry_filter_list


class ListRegistriesRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_agent_registry_control.types.max_results.MaxResults"]
    """<p>Maximum number of results to return</p>"""
    next_token: NotRequired["capo_agent_registry_control.types.next_token.NextToken"]
    """<p>Token for pagination</p>"""
    filters: NotRequired[
        "capo_agent_registry_control.types.registry_filter_list.RegistryFilterList"
    ]
    """<p>Filters to apply to the registry list</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRegistriesRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "filters" in value:
        import capo_agent_registry_control.types.registry_filter_list

        out["filters"] = (
            capo_agent_registry_control.types.registry_filter_list.serialize_json(
                value["filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListRegistriesRequest:
    out: ListRegistriesRequest = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("filters") is not None:
        import capo_agent_registry_control.types.registry_filter_list

        out["filters"] = (
            capo_agent_registry_control.types.registry_filter_list.deserialize_json(
                data["filters"]
            )
        )
    return out

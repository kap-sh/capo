"""Generated from Smithy shape ``com.amazonaws.drs#ListLaunchActionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.launch_action_resource_id
    import capo_drs.types.launch_actions_request_filters
    import capo_drs.types.max_results_type
    import capo_drs.types.pagination_token


class ListLaunchActionsRequest(TypedDict, closed=True):
    resource_id: "capo_drs.types.launch_action_resource_id.LaunchActionResourceId"
    filters: NotRequired[
        "capo_drs.types.launch_actions_request_filters.LaunchActionsRequestFilters"
    ]
    """<p>Filters to apply when listing resource launch actions.</p>"""
    max_results: NotRequired["capo_drs.types.max_results_type.MaxResultsType"]
    """<p>Maximum amount of items to return when listing resource launch actions.</p>"""
    next_token: NotRequired["capo_drs.types.pagination_token.PaginationToken"]
    """<p>Next token to use when listing resource launch actions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLaunchActionsRequest) -> dict:
    out: dict = {}
    out["resourceId"] = value["resource_id"]
    if "filters" in value:
        import capo_drs.types.launch_actions_request_filters

        out["filters"] = capo_drs.types.launch_actions_request_filters.serialize_json(
            value["filters"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLaunchActionsRequest:
    out: ListLaunchActionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    else:
        out["resource_id"] = ""
    if data.get("filters") is not None:
        import capo_drs.types.launch_actions_request_filters

        out["filters"] = capo_drs.types.launch_actions_request_filters.deserialize_json(
            data["filters"]
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

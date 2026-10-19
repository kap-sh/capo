"""Generated from Smithy shape ``com.amazonaws.mgn#ListTemplateActionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.launch_configuration_template_id
    import capo_mgn.types.max_results_type
    import capo_mgn.types.pagination_token
    import capo_mgn.types.template_actions_request_filters


class ListTemplateActionsRequest(TypedDict, closed=True):
    launch_configuration_template_id: (
        "capo_mgn.types.launch_configuration_template_id.LaunchConfigurationTemplateID"
    )
    """<p>Launch configuration template ID.</p>"""
    filters: NotRequired[
        "capo_mgn.types.template_actions_request_filters.TemplateActionsRequestFilters"
    ]
    """<p>Filters to apply when listing template post migration custom actions.</p>"""
    max_results: NotRequired["capo_mgn.types.max_results_type.MaxResultsType"]
    """<p>Maximum amount of items to return when listing template post migration custom actions.</p>"""
    next_token: NotRequired["capo_mgn.types.pagination_token.PaginationToken"]
    """<p>Next token to use when listing template post migration custom actions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTemplateActionsRequest) -> dict:
    out: dict = {}
    out["launchConfigurationTemplateID"] = value["launch_configuration_template_id"]
    if "filters" in value:
        import capo_mgn.types.template_actions_request_filters

        out["filters"] = capo_mgn.types.template_actions_request_filters.serialize_json(
            value["filters"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTemplateActionsRequest:
    out: ListTemplateActionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("launchConfigurationTemplateID") is not None:
        out["launch_configuration_template_id"] = data["launchConfigurationTemplateID"]
    else:
        out["launch_configuration_template_id"] = ""
    if data.get("filters") is not None:
        import capo_mgn.types.template_actions_request_filters

        out["filters"] = (
            capo_mgn.types.template_actions_request_filters.deserialize_json(
                data["filters"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

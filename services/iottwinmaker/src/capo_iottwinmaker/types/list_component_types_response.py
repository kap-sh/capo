"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ListComponentTypesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.component_type_summaries
    import capo_iottwinmaker.types.id
    import capo_iottwinmaker.types.max_results
    import capo_iottwinmaker.types.next_token


class ListComponentTypesResponse(TypedDict, closed=True):
    workspace_id: "capo_iottwinmaker.types.id.Id"
    """<p>The ID of the workspace.</p>"""
    component_type_summaries: (
        "capo_iottwinmaker.types.component_type_summaries.ComponentTypeSummaries"
    )
    """<p>A list of objects that contain information about the component types.</p>"""
    next_token: NotRequired["capo_iottwinmaker.types.next_token.NextToken"]
    """<p>The string that specifies the next page of results.</p>"""
    max_results: NotRequired["capo_iottwinmaker.types.max_results.MaxResults"]
    """<p>Specifies the maximum number of results to display.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListComponentTypesResponse) -> dict:
    out: dict = {}
    out["workspaceId"] = value["workspace_id"]
    import capo_iottwinmaker.types.component_type_summaries

    out["componentTypeSummaries"] = (
        capo_iottwinmaker.types.component_type_summaries.serialize_json(
            value["component_type_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListComponentTypesResponse:
    out: ListComponentTypesResponse = {}  # type: ignore[typeddict-item]
    if data.get("workspaceId") is not None:
        out["workspace_id"] = data["workspaceId"]
    else:
        out["workspace_id"] = ""
    if data.get("componentTypeSummaries") is not None:
        import capo_iottwinmaker.types.component_type_summaries

        out["component_type_summaries"] = (
            capo_iottwinmaker.types.component_type_summaries.deserialize_json(
                data["componentTypeSummaries"]
            )
        )
    else:
        out["component_type_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out

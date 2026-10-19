"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ListPropertiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.component_path
    import capo_iottwinmaker.types.entity_id
    import capo_iottwinmaker.types.id
    import capo_iottwinmaker.types.max_results
    import capo_iottwinmaker.types.name
    import capo_iottwinmaker.types.next_token


class ListPropertiesRequest(TypedDict, closed=True):
    workspace_id: "capo_iottwinmaker.types.id.Id"
    """<p>The workspace ID.</p>"""
    component_name: NotRequired["capo_iottwinmaker.types.name.Name"]
    """<p>The name of the component whose properties are returned by the operation.</p>"""
    component_path: NotRequired["capo_iottwinmaker.types.component_path.ComponentPath"]
    """<p>This string specifies the path to the composite component, starting from the top-level component.</p>"""
    entity_id: "capo_iottwinmaker.types.entity_id.EntityId"
    """<p>The ID for the entity whose metadata (component/properties) is returned by the operation.</p>"""
    max_results: NotRequired["capo_iottwinmaker.types.max_results.MaxResults"]
    """<p>The maximum number of results returned at one time. The default is 25.</p>"""
    next_token: NotRequired["capo_iottwinmaker.types.next_token.NextToken"]
    """<p>The string that specifies the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPropertiesRequest) -> dict:
    out: dict = {}
    if "component_name" in value:
        out["componentName"] = value["component_name"]
    if "component_path" in value:
        out["componentPath"] = value["component_path"]
    out["entityId"] = value["entity_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPropertiesRequest:
    out: ListPropertiesRequest = {}  # type: ignore[typeddict-item]
    if data.get("componentName") is not None:
        out["component_name"] = data["componentName"]
    if data.get("componentPath") is not None:
        out["component_path"] = data["componentPath"]
    if data.get("entityId") is not None:
        out["entity_id"] = data["entityId"]
    else:
        out["entity_id"] = ""
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

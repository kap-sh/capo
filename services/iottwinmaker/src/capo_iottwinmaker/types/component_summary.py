"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ComponentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iottwinmaker.types.component_path
    import capo_iottwinmaker.types.component_property_group_responses
    import capo_iottwinmaker.types.component_type_id
    import capo_iottwinmaker.types.description
    import capo_iottwinmaker.types.name
    import capo_iottwinmaker.types.status
    import capo_iottwinmaker.types.string
    import capo_iottwinmaker.types.sync_source


class ComponentSummary(TypedDict, closed=True):
    component_name: "capo_iottwinmaker.types.name.Name"
    """<p>The name of the component.</p>"""
    component_type_id: "capo_iottwinmaker.types.component_type_id.ComponentTypeId"
    """<p>The ID of the component type.</p>"""
    defined_in: NotRequired["capo_iottwinmaker.types.string.String"]
    """<p>The name of the property definition set in the request.</p>"""
    description: NotRequired["capo_iottwinmaker.types.description.Description"]
    """<p>The description of the component request.</p>"""
    property_groups: NotRequired[
        "capo_iottwinmaker.types.component_property_group_responses.ComponentPropertyGroupResponses"
    ]
    """<p>The property groups.</p>"""
    status: "capo_iottwinmaker.types.status.Status"
    """<p>The status of the component type.</p>"""
    sync_source: NotRequired["capo_iottwinmaker.types.sync_source.SyncSource"]
    """<p>The <code>syncSource</code> of the sync job, if this entity was created by a sync job.</p>"""
    component_path: NotRequired["capo_iottwinmaker.types.component_path.ComponentPath"]
    """<p>This string specifies the path to the composite component, starting from the top-level component.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentSummary) -> dict:
    out: dict = {}
    out["componentName"] = value["component_name"]
    out["componentTypeId"] = value["component_type_id"]
    if "defined_in" in value:
        out["definedIn"] = value["defined_in"]
    if "description" in value:
        out["description"] = value["description"]
    if "property_groups" in value:
        import capo_iottwinmaker.types.component_property_group_responses

        out["propertyGroups"] = (
            capo_iottwinmaker.types.component_property_group_responses.serialize_json(
                value["property_groups"]
            )
        )
    import capo_iottwinmaker.types.status

    out["status"] = capo_iottwinmaker.types.status.serialize_json(value["status"])
    if "sync_source" in value:
        out["syncSource"] = value["sync_source"]
    if "component_path" in value:
        out["componentPath"] = value["component_path"]
    return out


def deserialize_json(data: dict) -> ComponentSummary:
    out: ComponentSummary = {}  # type: ignore[typeddict-item]
    if data.get("componentName") is not None:
        out["component_name"] = data["componentName"]
    else:
        out["component_name"] = ""
    if data.get("componentTypeId") is not None:
        out["component_type_id"] = data["componentTypeId"]
    else:
        out["component_type_id"] = ""
    if data.get("definedIn") is not None:
        out["defined_in"] = data["definedIn"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("propertyGroups") is not None:
        import capo_iottwinmaker.types.component_property_group_responses

        out["property_groups"] = (
            capo_iottwinmaker.types.component_property_group_responses.deserialize_json(
                data["propertyGroups"]
            )
        )
    if data.get("status") is not None:
        import capo_iottwinmaker.types.status

        out["status"] = capo_iottwinmaker.types.status.deserialize_json(data["status"])
    else:
        raise DeserializationError("ComponentSummary.status required")
    if data.get("syncSource") is not None:
        out["sync_source"] = data["syncSource"]
    if data.get("componentPath") is not None:
        out["component_path"] = data["componentPath"]
    return out

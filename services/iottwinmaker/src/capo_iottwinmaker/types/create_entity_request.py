"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#CreateEntityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.components_map_request
    import capo_iottwinmaker.types.composite_components_map_request
    import capo_iottwinmaker.types.description
    import capo_iottwinmaker.types.entity_id
    import capo_iottwinmaker.types.entity_name
    import capo_iottwinmaker.types.id
    import capo_iottwinmaker.types.parent_entity_id
    import capo_iottwinmaker.types.tag_map


class CreateEntityRequest(TypedDict, closed=True):
    workspace_id: "capo_iottwinmaker.types.id.Id"
    """<p>The ID of the workspace that contains the entity.</p>"""
    entity_id: NotRequired["capo_iottwinmaker.types.entity_id.EntityId"]
    """<p>The ID of the entity.</p>"""
    entity_name: "capo_iottwinmaker.types.entity_name.EntityName"
    """<p>The name of the entity.</p>"""
    description: NotRequired["capo_iottwinmaker.types.description.Description"]
    """<p>The description of the entity.</p>"""
    components: NotRequired[
        "capo_iottwinmaker.types.components_map_request.ComponentsMapRequest"
    ]
    """<p>An object that maps strings to the components in the entity. Each string in the mapping must be unique to this object.</p>"""
    composite_components: NotRequired[
        "capo_iottwinmaker.types.composite_components_map_request.CompositeComponentsMapRequest"
    ]
    """<p>This is an object that maps strings to <code>compositeComponent</code> updates in the request. Each key of the map represents the <code>componentPath</code> of the <code>compositeComponent</code>.</p>"""
    parent_entity_id: NotRequired[
        "capo_iottwinmaker.types.parent_entity_id.ParentEntityId"
    ]
    """<p>The ID of the entity's parent entity.</p>"""
    tags: NotRequired["capo_iottwinmaker.types.tag_map.TagMap"]
    """<p>Metadata that you can use to manage the entity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEntityRequest) -> dict:
    out: dict = {}
    if "entity_id" in value:
        out["entityId"] = value["entity_id"]
    out["entityName"] = value["entity_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "components" in value:
        import capo_iottwinmaker.types.components_map_request

        out["components"] = (
            capo_iottwinmaker.types.components_map_request.serialize_json(
                value["components"]
            )
        )
    if "composite_components" in value:
        import capo_iottwinmaker.types.composite_components_map_request

        out["compositeComponents"] = (
            capo_iottwinmaker.types.composite_components_map_request.serialize_json(
                value["composite_components"]
            )
        )
    if "parent_entity_id" in value:
        out["parentEntityId"] = value["parent_entity_id"]
    if "tags" in value:
        import capo_iottwinmaker.types.tag_map

        out["tags"] = capo_iottwinmaker.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateEntityRequest:
    out: CreateEntityRequest = {}  # type: ignore[typeddict-item]
    if data.get("entityId") is not None:
        out["entity_id"] = data["entityId"]
    if data.get("entityName") is not None:
        out["entity_name"] = data["entityName"]
    else:
        out["entity_name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("components") is not None:
        import capo_iottwinmaker.types.components_map_request

        out["components"] = (
            capo_iottwinmaker.types.components_map_request.deserialize_json(
                data["components"]
            )
        )
    if data.get("compositeComponents") is not None:
        import capo_iottwinmaker.types.composite_components_map_request

        out["composite_components"] = (
            capo_iottwinmaker.types.composite_components_map_request.deserialize_json(
                data["compositeComponents"]
            )
        )
    if data.get("parentEntityId") is not None:
        out["parent_entity_id"] = data["parentEntityId"]
    if data.get("tags") is not None:
        import capo_iottwinmaker.types.tag_map

        out["tags"] = capo_iottwinmaker.types.tag_map.deserialize_json(data["tags"])
    return out

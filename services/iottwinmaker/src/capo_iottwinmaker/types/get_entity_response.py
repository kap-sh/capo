"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#GetEntityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iottwinmaker.types.boolean
    import capo_iottwinmaker.types.components_map
    import capo_iottwinmaker.types.description
    import capo_iottwinmaker.types.entity_id
    import capo_iottwinmaker.types.entity_name
    import capo_iottwinmaker.types.id
    import capo_iottwinmaker.types.parent_entity_id
    import capo_iottwinmaker.types.status
    import capo_iottwinmaker.types.sync_source
    import capo_iottwinmaker.types.timestamp
    import capo_iottwinmaker.types.twin_maker_arn


class GetEntityResponse(TypedDict, closed=True):
    entity_id: "capo_iottwinmaker.types.entity_id.EntityId"
    """<p>The ID of the entity.</p>"""
    entity_name: "capo_iottwinmaker.types.entity_name.EntityName"
    """<p>The name of the entity.</p>"""
    arn: "capo_iottwinmaker.types.twin_maker_arn.TwinMakerArn"
    """<p>The ARN of the entity.</p>"""
    status: "capo_iottwinmaker.types.status.Status"
    """<p>The current status of the entity.</p>"""
    workspace_id: "capo_iottwinmaker.types.id.Id"
    """<p>The ID of the workspace.</p>"""
    description: NotRequired["capo_iottwinmaker.types.description.Description"]
    """<p>The description of the entity.</p>"""
    components: NotRequired["capo_iottwinmaker.types.components_map.ComponentsMap"]
    """<p>An object that maps strings to the components in the entity. Each string in the mapping must be unique to this object.</p>"""
    parent_entity_id: "capo_iottwinmaker.types.parent_entity_id.ParentEntityId"
    """<p>The ID of the parent entity for this entity.</p>"""
    has_child_entities: "capo_iottwinmaker.types.boolean.Boolean"
    """<p>A Boolean value that specifies whether the entity has associated child entities.</p>"""
    creation_date_time: "capo_iottwinmaker.types.timestamp.Timestamp"
    """<p>The date and time when the entity was created.</p>"""
    update_date_time: "capo_iottwinmaker.types.timestamp.Timestamp"
    """<p>The date and time when the entity was last updated.</p>"""
    sync_source: NotRequired["capo_iottwinmaker.types.sync_source.SyncSource"]
    """<p>The syncSource of the sync job, if this entity was created by a sync job.</p>"""
    are_all_components_returned: NotRequired["capo_iottwinmaker.types.boolean.Boolean"]
    """<p>This flag notes whether all components are returned in the API response. The maximum number of components returned is 30.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEntityResponse) -> dict:
    out: dict = {}
    out["entityId"] = value["entity_id"]
    out["entityName"] = value["entity_name"]
    out["arn"] = value["arn"]
    import capo_iottwinmaker.types.status

    out["status"] = capo_iottwinmaker.types.status.serialize_json(value["status"])
    out["workspaceId"] = value["workspace_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "components" in value:
        import capo_iottwinmaker.types.components_map

        out["components"] = capo_iottwinmaker.types.components_map.serialize_json(
            value["components"]
        )
    out["parentEntityId"] = value["parent_entity_id"]
    out["hasChildEntities"] = value["has_child_entities"]
    import capo_iottwinmaker.types.timestamp

    out["creationDateTime"] = capo_iottwinmaker.types.timestamp.serialize_json(
        value["creation_date_time"]
    )
    import capo_iottwinmaker.types.timestamp

    out["updateDateTime"] = capo_iottwinmaker.types.timestamp.serialize_json(
        value["update_date_time"]
    )
    if "sync_source" in value:
        out["syncSource"] = value["sync_source"]
    if "are_all_components_returned" in value:
        out["areAllComponentsReturned"] = value["are_all_components_returned"]
    return out


def deserialize_json(data: dict) -> GetEntityResponse:
    out: GetEntityResponse = {}  # type: ignore[typeddict-item]
    if data.get("entityId") is not None:
        out["entity_id"] = data["entityId"]
    else:
        out["entity_id"] = ""
    if data.get("entityName") is not None:
        out["entity_name"] = data["entityName"]
    else:
        out["entity_name"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("status") is not None:
        import capo_iottwinmaker.types.status

        out["status"] = capo_iottwinmaker.types.status.deserialize_json(data["status"])
    else:
        raise DeserializationError("GetEntityResponse.status required")
    if data.get("workspaceId") is not None:
        out["workspace_id"] = data["workspaceId"]
    else:
        out["workspace_id"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("components") is not None:
        import capo_iottwinmaker.types.components_map

        out["components"] = capo_iottwinmaker.types.components_map.deserialize_json(
            data["components"]
        )
    if data.get("parentEntityId") is not None:
        out["parent_entity_id"] = data["parentEntityId"]
    else:
        out["parent_entity_id"] = ""
    if data.get("hasChildEntities") is not None:
        out["has_child_entities"] = data["hasChildEntities"]
    else:
        out["has_child_entities"] = False
    if data.get("creationDateTime") is not None:
        import capo_iottwinmaker.types.timestamp

        out["creation_date_time"] = capo_iottwinmaker.types.timestamp.deserialize_json(
            data["creationDateTime"]
        )
    else:
        import datetime

        out["creation_date_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("updateDateTime") is not None:
        import capo_iottwinmaker.types.timestamp

        out["update_date_time"] = capo_iottwinmaker.types.timestamp.deserialize_json(
            data["updateDateTime"]
        )
    else:
        import datetime

        out["update_date_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("syncSource") is not None:
        out["sync_source"] = data["syncSource"]
    if data.get("areAllComponentsReturned") is not None:
        out["are_all_components_returned"] = data["areAllComponentsReturned"]
    return out

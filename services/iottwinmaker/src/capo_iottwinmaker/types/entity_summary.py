"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#EntitySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iottwinmaker.types.boolean
    import capo_iottwinmaker.types.description
    import capo_iottwinmaker.types.entity_id
    import capo_iottwinmaker.types.entity_name
    import capo_iottwinmaker.types.parent_entity_id
    import capo_iottwinmaker.types.status
    import capo_iottwinmaker.types.timestamp
    import capo_iottwinmaker.types.twin_maker_arn


class EntitySummary(TypedDict, closed=True):
    entity_id: "capo_iottwinmaker.types.entity_id.EntityId"
    """<p>The ID of the entity.</p>"""
    entity_name: "capo_iottwinmaker.types.entity_name.EntityName"
    """<p>The name of the entity.</p>"""
    arn: "capo_iottwinmaker.types.twin_maker_arn.TwinMakerArn"
    """<p>The ARN of the entity.</p>"""
    parent_entity_id: NotRequired[
        "capo_iottwinmaker.types.parent_entity_id.ParentEntityId"
    ]
    """<p>The ID of the parent entity.</p>"""
    status: "capo_iottwinmaker.types.status.Status"
    """<p>The current status of the entity.</p>"""
    description: NotRequired["capo_iottwinmaker.types.description.Description"]
    """<p>The description of the entity.</p>"""
    has_child_entities: NotRequired["capo_iottwinmaker.types.boolean.Boolean"]
    """<p>An <b>eventual</b> Boolean value that specifies whether the entity has child entities or not.</p>"""
    creation_date_time: "capo_iottwinmaker.types.timestamp.Timestamp"
    """<p>The date and time when the entity was created.</p>"""
    update_date_time: "capo_iottwinmaker.types.timestamp.Timestamp"
    """<p>The last date and time when the entity was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EntitySummary) -> dict:
    out: dict = {}
    out["entityId"] = value["entity_id"]
    out["entityName"] = value["entity_name"]
    out["arn"] = value["arn"]
    if "parent_entity_id" in value:
        out["parentEntityId"] = value["parent_entity_id"]
    import capo_iottwinmaker.types.status

    out["status"] = capo_iottwinmaker.types.status.serialize_json(value["status"])
    if "description" in value:
        out["description"] = value["description"]
    if "has_child_entities" in value:
        out["hasChildEntities"] = value["has_child_entities"]
    import capo_iottwinmaker.types.timestamp

    out["creationDateTime"] = capo_iottwinmaker.types.timestamp.serialize_json(
        value["creation_date_time"]
    )
    import capo_iottwinmaker.types.timestamp

    out["updateDateTime"] = capo_iottwinmaker.types.timestamp.serialize_json(
        value["update_date_time"]
    )
    return out


def deserialize_json(data: dict) -> EntitySummary:
    out: EntitySummary = {}  # type: ignore[typeddict-item]
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
    if data.get("parentEntityId") is not None:
        out["parent_entity_id"] = data["parentEntityId"]
    if data.get("status") is not None:
        import capo_iottwinmaker.types.status

        out["status"] = capo_iottwinmaker.types.status.deserialize_json(data["status"])
    else:
        raise DeserializationError("EntitySummary.status required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("hasChildEntities") is not None:
        out["has_child_entities"] = data["hasChildEntities"]
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
    return out

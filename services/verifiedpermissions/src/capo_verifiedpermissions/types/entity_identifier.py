"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#EntityIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.entity_id
    import capo_verifiedpermissions.types.entity_type


class EntityIdentifier(TypedDict, closed=True):
    entity_type: "capo_verifiedpermissions.types.entity_type.EntityType"
    """<p>The type of an entity.</p> <p>Example: <code>"entityType":"<i>typeName</i>"</code> </p>"""
    entity_id: "capo_verifiedpermissions.types.entity_id.EntityId"
    """<p>The identifier of an entity.</p> <p> <code>"entityId":"<i>identifier</i>"</code> </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EntityIdentifier) -> dict:
    out: dict = {}
    out["entityType"] = value["entity_type"]
    out["entityId"] = value["entity_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EntityIdentifier:
    out: EntityIdentifier = {}  # type: ignore[typeddict-item]
    if data.get("entityType") is not None:
        out["entity_type"] = data["entityType"]
    else:
        raise DeserializationError("EntityIdentifier.entity_type required")
    if data.get("entityId") is not None:
        out["entity_id"] = data["entityId"]
    else:
        raise DeserializationError("EntityIdentifier.entity_id required")
    return out

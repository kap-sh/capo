"""Generated from Smithy shape ``com.amazonaws.frauddetector#Entity``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.entity_restricted_string
    import capo_frauddetector.types.string


class Entity(TypedDict, closed=True):
    entity_type: "capo_frauddetector.types.string.string"
    """<p>The entity type.</p>"""
    entity_id: (
        "capo_frauddetector.types.entity_restricted_string.entityRestrictedString"
    )
    """<p>The entity ID. If you do not know the <code>entityId</code>, you can pass <code>unknown</code>, which is areserved string literal.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Entity) -> dict:
    out: dict = {}
    out["entityType"] = value["entity_type"]
    out["entityId"] = value["entity_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Entity:
    out: Entity = {}  # type: ignore[typeddict-item]
    if data.get("entityType") is not None:
        out["entity_type"] = data["entityType"]
    else:
        out["entity_type"] = ""
    if data.get("entityId") is not None:
        out["entity_id"] = data["entityId"]
    else:
        out["entity_id"] = ""
    return out

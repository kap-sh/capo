"""Generated from Smithy shape ``com.amazonaws.socialmessaging#MetaFlowHealthEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.meta_flow_health_entity_type
    import capo_socialmessaging.types.meta_flow_health_status_availability


class MetaFlowHealthEntity(TypedDict, closed=True):
    entity_type: "capo_socialmessaging.types.meta_flow_health_entity_type.MetaFlowHealthEntityType"
    """<p>The type of entity (for example, FLOW, WABA, BUSINESS, or APP).</p>"""
    id: "str"
    """<p>The unique identifier of the entity.</p>"""
    can_send_message: "capo_socialmessaging.types.meta_flow_health_status_availability.MetaFlowHealthStatusAvailability"
    """<p>The messaging availability status for this entity (for example, AVAILABLE, LIMITED, or BLOCKED).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetaFlowHealthEntity) -> dict:
    out: dict = {}
    out["entityType"] = value["entity_type"]
    out["id"] = value["id"]
    out["canSendMessage"] = value["can_send_message"]
    return out


def deserialize_json(data: dict) -> MetaFlowHealthEntity:
    out: MetaFlowHealthEntity = {}  # type: ignore[typeddict-item]
    if data.get("entityType") is not None:
        out["entity_type"] = data["entityType"]
    else:
        out["entity_type"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("canSendMessage") is not None:
        out["can_send_message"] = data["canSendMessage"]
    else:
        out["can_send_message"] = ""
    return out

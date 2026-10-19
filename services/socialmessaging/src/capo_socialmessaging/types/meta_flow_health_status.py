"""Generated from Smithy shape ``com.amazonaws.socialmessaging#MetaFlowHealthStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.meta_flow_health_entity_list
    import capo_socialmessaging.types.meta_flow_health_status_availability


class MetaFlowHealthStatus(TypedDict, closed=True):
    can_send_message: "capo_socialmessaging.types.meta_flow_health_status_availability.MetaFlowHealthStatusAvailability"
    """<p>The overall messaging availability status (for example, AVAILABLE, LIMITED, or BLOCKED).</p>"""
    entities: NotRequired[
        "capo_socialmessaging.types.meta_flow_health_entity_list.MetaFlowHealthEntityList"
    ]
    """<p>A list of health status entities with per-entity availability information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetaFlowHealthStatus) -> dict:
    out: dict = {}
    out["canSendMessage"] = value["can_send_message"]
    if "entities" in value:
        import capo_socialmessaging.types.meta_flow_health_entity_list

        out["entities"] = (
            capo_socialmessaging.types.meta_flow_health_entity_list.serialize_json(
                value["entities"]
            )
        )
    return out


def deserialize_json(data: dict) -> MetaFlowHealthStatus:
    out: MetaFlowHealthStatus = {}  # type: ignore[typeddict-item]
    if data.get("canSendMessage") is not None:
        out["can_send_message"] = data["canSendMessage"]
    else:
        out["can_send_message"] = ""
    if data.get("entities") is not None:
        import capo_socialmessaging.types.meta_flow_health_entity_list

        out["entities"] = (
            capo_socialmessaging.types.meta_flow_health_entity_list.deserialize_json(
                data["entities"]
            )
        )
    return out

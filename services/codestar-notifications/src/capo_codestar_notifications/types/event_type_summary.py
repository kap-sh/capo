"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#EventTypeSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codestar_notifications.types.event_type_id
    import capo_codestar_notifications.types.event_type_name
    import capo_codestar_notifications.types.resource_type
    import capo_codestar_notifications.types.service_name


class EventTypeSummary(TypedDict, closed=True):
    event_type_id: NotRequired[
        "capo_codestar_notifications.types.event_type_id.EventTypeId"
    ]
    """<p>The system-generated ID of the event. For a complete list of event types and IDs, see <a href="https://docs.aws.amazon.com/codestar-notifications/latest/userguide/concepts.html#concepts-api">Notification concepts</a> in the <i>Developer Tools Console User Guide</i>.</p>"""
    service_name: NotRequired[
        "capo_codestar_notifications.types.service_name.ServiceName"
    ]
    """<p>The name of the service for which the event applies.</p>"""
    event_type_name: NotRequired[
        "capo_codestar_notifications.types.event_type_name.EventTypeName"
    ]
    """<p>The name of the event.</p>"""
    resource_type: NotRequired[
        "capo_codestar_notifications.types.resource_type.ResourceType"
    ]
    """<p>The resource type of the event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventTypeSummary) -> dict:
    out: dict = {}
    if "event_type_id" in value:
        out["EventTypeId"] = value["event_type_id"]
    if "service_name" in value:
        out["ServiceName"] = value["service_name"]
    if "event_type_name" in value:
        out["EventTypeName"] = value["event_type_name"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> EventTypeSummary:
    out: EventTypeSummary = {}  # type: ignore[typeddict-item]
    if data.get("EventTypeId") is not None:
        out["event_type_id"] = data["EventTypeId"]
    if data.get("ServiceName") is not None:
        out["service_name"] = data["ServiceName"]
    if data.get("EventTypeName") is not None:
        out["event_type_name"] = data["EventTypeName"]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    return out

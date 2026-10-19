"""Generated from Smithy shape ``com.amazonaws.ivschat#SendEventRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivschat.types.event_attributes
    import capo_ivschat.types.event_name
    import capo_ivschat.types.room_identifier


class SendEventRequest(TypedDict, closed=True):
    room_identifier: "capo_ivschat.types.room_identifier.RoomIdentifier"
    """<p>Identifier of the room to which the event will be sent. Currently this must be an ARN.</p>"""
    event_name: "capo_ivschat.types.event_name.EventName"
    """<p>Application-defined name of the event to send to clients.</p>"""
    attributes: NotRequired["capo_ivschat.types.event_attributes.EventAttributes"]
    """<p>Application-defined metadata to attach to the event sent to clients. The maximum length of the metadata is 1 KB total.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendEventRequest) -> dict:
    out: dict = {}
    out["roomIdentifier"] = value["room_identifier"]
    out["eventName"] = value["event_name"]
    if "attributes" in value:
        import capo_ivschat.types.event_attributes

        out["attributes"] = capo_ivschat.types.event_attributes.serialize_json(
            value["attributes"]
        )
    return out


def deserialize_json(data: dict) -> SendEventRequest:
    out: SendEventRequest = {}  # type: ignore[typeddict-item]
    if data.get("roomIdentifier") is not None:
        out["room_identifier"] = data["roomIdentifier"]
    else:
        out["room_identifier"] = ""
    if data.get("eventName") is not None:
        out["event_name"] = data["eventName"]
    else:
        out["event_name"] = ""
    if data.get("attributes") is not None:
        import capo_ivschat.types.event_attributes

        out["attributes"] = capo_ivschat.types.event_attributes.deserialize_json(
            data["attributes"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.iotevents#IotEventsAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.input_name
    import capo_iot_events.types.payload


class IotEventsAction(TypedDict, closed=True):
    input_name: "capo_iot_events.types.input_name.InputName"
    """<p>The name of the AWS IoT Events input where the data is sent.</p>"""
    payload: NotRequired["capo_iot_events.types.payload.Payload"]
    """<p>You can configure the action payload when you send a message to an AWS IoT Events input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IotEventsAction) -> dict:
    out: dict = {}
    out["inputName"] = value["input_name"]
    if "payload" in value:
        import capo_iot_events.types.payload

        out["payload"] = capo_iot_events.types.payload.serialize_json(value["payload"])
    return out


def deserialize_json(data: dict) -> IotEventsAction:
    out: IotEventsAction = {}  # type: ignore[typeddict-item]
    if data.get("inputName") is not None:
        out["input_name"] = data["inputName"]
    else:
        out["input_name"] = ""
    if data.get("payload") is not None:
        import capo_iot_events.types.payload

        out["payload"] = capo_iot_events.types.payload.deserialize_json(data["payload"])
    return out

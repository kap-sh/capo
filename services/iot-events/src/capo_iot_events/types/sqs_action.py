"""Generated from Smithy shape ``com.amazonaws.iotevents#SqsAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.payload
    import capo_iot_events.types.queue_url
    import capo_iot_events.types.use_base64


class SqsAction(TypedDict, closed=True):
    queue_url: "capo_iot_events.types.queue_url.QueueUrl"
    """<p>The URL of the SQS queue where the data is written.</p>"""
    use_base64: NotRequired["capo_iot_events.types.use_base64.UseBase64"]
    """<p>Set this to TRUE if you want the data to be base-64 encoded before it is written to the queue. Otherwise, set this to FALSE.</p>"""
    payload: NotRequired["capo_iot_events.types.payload.Payload"]
    """<p>You can configure the action payload when you send a message to an Amazon SQS queue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SqsAction) -> dict:
    out: dict = {}
    out["queueUrl"] = value["queue_url"]
    if "use_base64" in value:
        out["useBase64"] = value["use_base64"]
    if "payload" in value:
        import capo_iot_events.types.payload

        out["payload"] = capo_iot_events.types.payload.serialize_json(value["payload"])
    return out


def deserialize_json(data: dict) -> SqsAction:
    out: SqsAction = {}  # type: ignore[typeddict-item]
    if data.get("queueUrl") is not None:
        out["queue_url"] = data["queueUrl"]
    else:
        out["queue_url"] = ""
    if data.get("useBase64") is not None:
        out["use_base64"] = data["useBase64"]
    if data.get("payload") is not None:
        import capo_iot_events.types.payload

        out["payload"] = capo_iot_events.types.payload.deserialize_json(data["payload"])
    return out

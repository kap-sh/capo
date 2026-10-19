"""Generated from Smithy shape ``com.amazonaws.iotevents#FirehoseAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.delivery_stream_name
    import capo_iot_events.types.firehose_separator
    import capo_iot_events.types.payload


class FirehoseAction(TypedDict, closed=True):
    delivery_stream_name: (
        "capo_iot_events.types.delivery_stream_name.DeliveryStreamName"
    )
    """<p>The name of the Kinesis Data Firehose delivery stream where the data is written.</p>"""
    separator: NotRequired["capo_iot_events.types.firehose_separator.FirehoseSeparator"]
    r"""<p>A character separator that is used to separate records written to the Kinesis Data Firehose delivery stream. Valid values are: '\n' (newline), '\t' (tab), '\r\n' (Windows newline), ',' (comma).</p>"""
    payload: NotRequired["capo_iot_events.types.payload.Payload"]
    """<p>You can configure the action payload when you send a message to an Amazon Kinesis Data Firehose delivery stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FirehoseAction) -> dict:
    out: dict = {}
    out["deliveryStreamName"] = value["delivery_stream_name"]
    if "separator" in value:
        out["separator"] = value["separator"]
    if "payload" in value:
        import capo_iot_events.types.payload

        out["payload"] = capo_iot_events.types.payload.serialize_json(value["payload"])
    return out


def deserialize_json(data: dict) -> FirehoseAction:
    out: FirehoseAction = {}  # type: ignore[typeddict-item]
    if data.get("deliveryStreamName") is not None:
        out["delivery_stream_name"] = data["deliveryStreamName"]
    else:
        out["delivery_stream_name"] = ""
    if data.get("separator") is not None:
        out["separator"] = data["separator"]
    if data.get("payload") is not None:
        import capo_iot_events.types.payload

        out["payload"] = capo_iot_events.types.payload.deserialize_json(data["payload"])
    return out

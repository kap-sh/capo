"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#BatchPutMessageErrorEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events_data.types.error_code
    import capo_iot_events_data.types.error_message
    import capo_iot_events_data.types.message_id


class BatchPutMessageErrorEntry(TypedDict, closed=True):
    message_id: NotRequired["capo_iot_events_data.types.message_id.MessageId"]
    """<p>The ID of the message that caused the error. (See the value corresponding to the <code>"messageId"</code> key in the <code>"message"</code> object.)</p>"""
    error_code: NotRequired["capo_iot_events_data.types.error_code.ErrorCode"]
    """<p>The error code.</p>"""
    error_message: NotRequired["capo_iot_events_data.types.error_message.ErrorMessage"]
    """<p>A message that describes the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutMessageErrorEntry) -> dict:
    out: dict = {}
    if "message_id" in value:
        out["messageId"] = value["message_id"]
    if "error_code" in value:
        import capo_iot_events_data.types.error_code

        out["errorCode"] = capo_iot_events_data.types.error_code.serialize_json(
            value["error_code"]
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> BatchPutMessageErrorEntry:
    out: BatchPutMessageErrorEntry = {}  # type: ignore[typeddict-item]
    if data.get("messageId") is not None:
        out["message_id"] = data["messageId"]
    if data.get("errorCode") is not None:
        import capo_iot_events_data.types.error_code

        out["error_code"] = capo_iot_events_data.types.error_code.deserialize_json(
            data["errorCode"]
        )
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    return out

"""Generated from Smithy shape ``com.amazonaws.cloudtraildata#ResultErrorEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail_data.types.error_code
    import capo_cloudtrail_data.types.error_message
    import capo_cloudtrail_data.types.uuid


class ResultErrorEntry(TypedDict, closed=True):
    id: "capo_cloudtrail_data.types.uuid.Uuid"
    """<p>The original event ID from the source event that could not be ingested by CloudTrail.</p>"""
    error_code: "capo_cloudtrail_data.types.error_code.ErrorCode"
    """<p>The error code for events that could not be ingested by CloudTrail. Possible error codes include: <code>FieldTooLong</code>, <code>FieldNotFound</code>, <code>InvalidChecksum</code>, <code>InvalidData</code>, <code>InvalidRecipient</code>, <code>InvalidEventSource</code>, <code>AccountNotSubscribed</code>, <code>Throttling</code>, and <code>InternalFailure</code>.</p>"""
    error_message: "capo_cloudtrail_data.types.error_message.ErrorMessage"
    """<p>The message that describes the error for events that could not be ingested by CloudTrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResultErrorEntry) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["errorCode"] = value["error_code"]
    out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> ResultErrorEntry:
    out: ResultErrorEntry = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    else:
        out["error_code"] = ""
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    else:
        out["error_message"] = ""
    return out

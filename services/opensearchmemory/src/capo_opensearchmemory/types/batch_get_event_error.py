"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#BatchGetEventError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.batch_get_event_error_code
    import capo_opensearchmemory.types.event_id


class BatchGetEventError(TypedDict, closed=True):
    event_id: "capo_opensearchmemory.types.event_id.EventId"
    """<p>The ID of the requested event.</p>"""
    error_code: (
        "capo_opensearchmemory.types.batch_get_event_error_code.BatchGetEventErrorCode"
    )
    """<p>The reason that the call didn't return the event.</p>"""
    message: "str"
    """<p>A human-readable description.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchGetEventError) -> dict:
    out: dict = {}
    out["eventId"] = value["event_id"]
    import capo_opensearchmemory.types.batch_get_event_error_code

    out["errorCode"] = (
        capo_opensearchmemory.types.batch_get_event_error_code.serialize_aws_json_1_0(
            value["error_code"]
        )
    )
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchGetEventError:
    out: BatchGetEventError = {}  # type: ignore[typeddict-item]
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    else:
        out["event_id"] = ""
    if data.get("errorCode") is not None:
        import capo_opensearchmemory.types.batch_get_event_error_code

        out["error_code"] = (
            capo_opensearchmemory.types.batch_get_event_error_code.deserialize_aws_json_1_0(
                data["errorCode"]
            )
        )
    else:
        import typing

        out["error_code"] = typing.cast(
            "capo_opensearchmemory.types.batch_get_event_error_code.BatchGetEventErrorCode",
            "",
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out

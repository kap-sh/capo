"""Generated from Smithy shape ``com.amazonaws.lambda#InvocationCompletedDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda.types.event_error
    import capo_lambda.types.execution_timestamp
    import capo_lambda.types.string


class InvocationCompletedDetails(TypedDict, closed=True):
    start_timestamp: "capo_lambda.types.execution_timestamp.ExecutionTimestamp"
    """<p>The date and time when the invocation started, in <a href="https://www.w3.org/TR/NOTE-datetime">ISO-8601 format</a> (YYYY-MM-DDThh:mm:ss.sTZD).</p>"""
    end_timestamp: "capo_lambda.types.execution_timestamp.ExecutionTimestamp"
    """<p>The date and time when the invocation ended, in <a href="https://www.w3.org/TR/NOTE-datetime">ISO-8601 format</a> (YYYY-MM-DDThh:mm:ss.sTZD).</p>"""
    request_id: "capo_lambda.types.string.String"
    """<p>The request ID for the invocation.</p>"""
    error: NotRequired["capo_lambda.types.event_error.EventError"]
    """<p>Details about the invocation failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvocationCompletedDetails) -> dict:
    out: dict = {}
    import capo_lambda.types.execution_timestamp

    out["StartTimestamp"] = capo_lambda.types.execution_timestamp.serialize_json(
        value["start_timestamp"]
    )
    import capo_lambda.types.execution_timestamp

    out["EndTimestamp"] = capo_lambda.types.execution_timestamp.serialize_json(
        value["end_timestamp"]
    )
    out["RequestId"] = value["request_id"]
    if "error" in value:
        import capo_lambda.types.event_error

        out["Error"] = capo_lambda.types.event_error.serialize_json(value["error"])
    return out


def deserialize_json(data: dict) -> InvocationCompletedDetails:
    out: InvocationCompletedDetails = {}  # type: ignore[typeddict-item]
    if data.get("StartTimestamp") is not None:
        import capo_lambda.types.execution_timestamp

        out["start_timestamp"] = capo_lambda.types.execution_timestamp.deserialize_json(
            data["StartTimestamp"]
        )
    else:
        raise DeserializationError(
            "InvocationCompletedDetails.start_timestamp required"
        )
    if data.get("EndTimestamp") is not None:
        import capo_lambda.types.execution_timestamp

        out["end_timestamp"] = capo_lambda.types.execution_timestamp.deserialize_json(
            data["EndTimestamp"]
        )
    else:
        raise DeserializationError("InvocationCompletedDetails.end_timestamp required")
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    else:
        raise DeserializationError("InvocationCompletedDetails.request_id required")
    if data.get("Error") is not None:
        import capo_lambda.types.event_error

        out["error"] = capo_lambda.types.event_error.deserialize_json(data["Error"])
    return out

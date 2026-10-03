"""Generated from Smithy shape ``com.amazonaws.lambda#WaitStartedDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda.types.duration_seconds
    import capo_lambda.types.execution_timestamp


class WaitStartedDetails(TypedDict, closed=True):
    duration: "capo_lambda.types.duration_seconds.DurationSeconds"
    """<p>The duration to wait, in seconds.</p>"""
    scheduled_end_timestamp: "capo_lambda.types.execution_timestamp.ExecutionTimestamp"
    """<p>The date and time when the wait operation is scheduled to complete, in <a href="https://www.w3.org/TR/NOTE-datetime">ISO-8601 format</a> (YYYY-MM-DDThh:mm:ss.sTZD).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaitStartedDetails) -> dict:
    out: dict = {}
    out["Duration"] = value["duration"]
    import capo_lambda.types.execution_timestamp

    out["ScheduledEndTimestamp"] = capo_lambda.types.execution_timestamp.serialize_json(
        value["scheduled_end_timestamp"]
    )
    return out


def deserialize_json(data: dict) -> WaitStartedDetails:
    out: WaitStartedDetails = {}  # type: ignore[typeddict-item]
    if data.get("Duration") is not None:
        out["duration"] = data["Duration"]
    else:
        raise DeserializationError("WaitStartedDetails.duration required")
    if data.get("ScheduledEndTimestamp") is not None:
        import capo_lambda.types.execution_timestamp

        out["scheduled_end_timestamp"] = (
            capo_lambda.types.execution_timestamp.deserialize_json(
                data["ScheduledEndTimestamp"]
            )
        )
    else:
        raise DeserializationError(
            "WaitStartedDetails.scheduled_end_timestamp required"
        )
    return out

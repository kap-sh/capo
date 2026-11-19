"""Generated from Smithy shape ``com.amazonaws.lambda#ExecutionPausedDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.event_pause_reason
    import capo_lambda.types.execution_timeout_paused
    import capo_lambda.types.execution_timestamp


class ExecutionPausedDetails(TypedDict, closed=True):
    pause_request_timestamp: "capo_lambda.types.execution_timestamp.ExecutionTimestamp"
    """<p>The date and time when you requested the pause, in <a href="https://www.w3.org/TR/NOTE-datetime">ISO-8601 format</a> (YYYY-MM-DDThh:mm:ss.sTZD).</p>"""
    reason: NotRequired["capo_lambda.types.event_pause_reason.EventPauseReason"]
    """<p>The reason that you provided when you paused the execution.</p>"""
    execution_timeout_paused: (
        "capo_lambda.types.execution_timeout_paused.ExecutionTimeoutPaused"
    )
    """<p>Specifies whether the pause also paused the execution timeout.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionPausedDetails) -> dict:
    out: dict = {}
    import capo_lambda.types.execution_timestamp

    out["PauseRequestTimestamp"] = capo_lambda.types.execution_timestamp.serialize_json(
        value["pause_request_timestamp"]
    )
    if "reason" in value:
        import capo_lambda.types.event_pause_reason

        out["Reason"] = capo_lambda.types.event_pause_reason.serialize_json(
            value["reason"]
        )
    out["ExecutionTimeoutPaused"] = value["execution_timeout_paused"]
    return out


def deserialize_json(data: dict) -> ExecutionPausedDetails:
    out: ExecutionPausedDetails = {}  # type: ignore[typeddict-item]
    if data.get("PauseRequestTimestamp") is not None:
        import capo_lambda.types.execution_timestamp

        out["pause_request_timestamp"] = (
            capo_lambda.types.execution_timestamp.deserialize_json(
                data["PauseRequestTimestamp"]
            )
        )
    else:
        import datetime

        out["pause_request_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("Reason") is not None:
        import capo_lambda.types.event_pause_reason

        out["reason"] = capo_lambda.types.event_pause_reason.deserialize_json(
            data["Reason"]
        )
    if data.get("ExecutionTimeoutPaused") is not None:
        out["execution_timeout_paused"] = data["ExecutionTimeoutPaused"]
    else:
        out["execution_timeout_paused"] = False
    return out


def redact_sensitive(value: ExecutionPausedDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "reason" in value:
        import capo_lambda.types.event_pause_reason

        out["reason"] = capo_lambda.types.event_pause_reason.redact_sensitive(
            value["reason"]
        )
    return out

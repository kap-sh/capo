"""Generated from Smithy shape ``com.amazonaws.lambda#PauseDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.execution_timeout_paused
    import capo_lambda.types.execution_timestamp
    import capo_lambda.types.pause_reason


class PauseDetails(TypedDict, closed=True):
    pause_request_timestamp: "capo_lambda.types.execution_timestamp.ExecutionTimestamp"
    """<p>The date and time when you requested the pause, in <a href="https://www.w3.org/TR/NOTE-datetime">ISO-8601 format</a> (YYYY-MM-DDThh:mm:ss.sTZD).</p>"""
    reason: NotRequired["capo_lambda.types.pause_reason.PauseReason"]
    """<p>The reason that you provided when you paused the execution. This field is only present if you set <code>IncludeExecutionData</code> to <code>true</code> in the request.</p>"""
    execution_timeout_paused: (
        "capo_lambda.types.execution_timeout_paused.ExecutionTimeoutPaused"
    )
    """<p>Specifies whether the pause also pauses the execution timeout.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PauseDetails) -> dict:
    out: dict = {}
    import capo_lambda.types.execution_timestamp

    out["PauseRequestTimestamp"] = capo_lambda.types.execution_timestamp.serialize_json(
        value["pause_request_timestamp"]
    )
    if "reason" in value:
        out["Reason"] = value["reason"]
    out["ExecutionTimeoutPaused"] = value["execution_timeout_paused"]
    return out


def deserialize_json(data: dict) -> PauseDetails:
    out: PauseDetails = {}  # type: ignore[typeddict-item]
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
        out["reason"] = data["Reason"]
    if data.get("ExecutionTimeoutPaused") is not None:
        out["execution_timeout_paused"] = data["ExecutionTimeoutPaused"]
    else:
        out["execution_timeout_paused"] = False
    return out


def redact_sensitive(value: PauseDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "reason" in value:
        out["reason"] = "*** Sensitive Data Redacted ***"
    return out

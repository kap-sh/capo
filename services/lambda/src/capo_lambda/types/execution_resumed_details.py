"""Generated from Smithy shape ``com.amazonaws.lambda#ExecutionResumedDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.event_resume_reason
    import capo_lambda.types.execution_timestamp


class ExecutionResumedDetails(TypedDict, closed=True):
    resume_request_timestamp: "capo_lambda.types.execution_timestamp.ExecutionTimestamp"
    """<p>The date and time when you requested the resume, in <a href="https://www.w3.org/TR/NOTE-datetime">ISO-8601 format</a> (YYYY-MM-DDThh:mm:ss.sTZD).</p>"""
    reason: NotRequired["capo_lambda.types.event_resume_reason.EventResumeReason"]
    """<p>The reason that you provided when you resumed the execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionResumedDetails) -> dict:
    out: dict = {}
    import capo_lambda.types.execution_timestamp

    out["ResumeRequestTimestamp"] = (
        capo_lambda.types.execution_timestamp.serialize_json(
            value["resume_request_timestamp"]
        )
    )
    if "reason" in value:
        import capo_lambda.types.event_resume_reason

        out["Reason"] = capo_lambda.types.event_resume_reason.serialize_json(
            value["reason"]
        )
    return out


def deserialize_json(data: dict) -> ExecutionResumedDetails:
    out: ExecutionResumedDetails = {}  # type: ignore[typeddict-item]
    if data.get("ResumeRequestTimestamp") is not None:
        import capo_lambda.types.execution_timestamp

        out["resume_request_timestamp"] = (
            capo_lambda.types.execution_timestamp.deserialize_json(
                data["ResumeRequestTimestamp"]
            )
        )
    else:
        import datetime

        out["resume_request_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("Reason") is not None:
        import capo_lambda.types.event_resume_reason

        out["reason"] = capo_lambda.types.event_resume_reason.deserialize_json(
            data["Reason"]
        )
    return out


def redact_sensitive(value: ExecutionResumedDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "reason" in value:
        import capo_lambda.types.event_resume_reason

        out["reason"] = capo_lambda.types.event_resume_reason.redact_sensitive(
            value["reason"]
        )
    return out

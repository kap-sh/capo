"""Generated from Smithy shape ``com.amazonaws.lambda#EventResumeReason``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.resume_reason
    import capo_lambda.types.truncated


class EventResumeReason(TypedDict, closed=True):
    payload: NotRequired["capo_lambda.types.resume_reason.ResumeReason"]
    """<p>The reason that you provided when you resumed the execution. This field is only present if you set <code>IncludeExecutionData</code> to <code>true</code> in the request.</p>"""
    truncated: NotRequired["capo_lambda.types.truncated.Truncated"]
    """<p>Specifies whether Lambda omitted the reason from the response because <code>IncludeExecutionData</code> is <code>false</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventResumeReason) -> dict:
    out: dict = {}
    if "payload" in value:
        out["Payload"] = value["payload"]
    if "truncated" in value:
        out["Truncated"] = value["truncated"]
    return out


def deserialize_json(data: dict) -> EventResumeReason:
    out: EventResumeReason = {}  # type: ignore[typeddict-item]
    if data.get("Payload") is not None:
        out["payload"] = data["Payload"]
    if data.get("Truncated") is not None:
        out["truncated"] = data["Truncated"]
    return out


def redact_sensitive(value: EventResumeReason) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "payload" in value:
        out["payload"] = "*** Sensitive Data Redacted ***"
    return out

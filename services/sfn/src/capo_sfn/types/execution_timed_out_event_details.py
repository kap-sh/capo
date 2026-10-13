"""Generated from Smithy shape ``com.amazonaws.sfn#ExecutionTimedOutEventDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.sensitive_cause
    import capo_sfn.types.sensitive_error


class ExecutionTimedOutEventDetails(TypedDict, closed=True):
    error: NotRequired["capo_sfn.types.sensitive_error.SensitiveError"]
    """<p>The error code of the failure.</p>"""
    cause: NotRequired["capo_sfn.types.sensitive_cause.SensitiveCause"]
    """<p>A more detailed explanation of the cause of the timeout.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExecutionTimedOutEventDetails) -> dict:
    out: dict = {}
    if "error" in value:
        out["error"] = value["error"]
    if "cause" in value:
        out["cause"] = value["cause"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ExecutionTimedOutEventDetails:
    out: ExecutionTimedOutEventDetails = {}  # type: ignore[typeddict-item]
    if data.get("error") is not None:
        out["error"] = data["error"]
    if data.get("cause") is not None:
        out["cause"] = data["cause"]
    return out


def redact_sensitive(value: ExecutionTimedOutEventDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "error" in value:
        out["error"] = "*** Sensitive Data Redacted ***"
    if "cause" in value:
        out["cause"] = "*** Sensitive Data Redacted ***"
    return out

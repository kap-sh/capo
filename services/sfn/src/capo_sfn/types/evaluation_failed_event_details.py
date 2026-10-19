"""Generated from Smithy shape ``com.amazonaws.sfn#EvaluationFailedEventDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.evaluation_failure_location
    import capo_sfn.types.sensitive_cause
    import capo_sfn.types.sensitive_error
    import capo_sfn.types.state_name


class EvaluationFailedEventDetails(TypedDict, closed=True):
    error: NotRequired["capo_sfn.types.sensitive_error.SensitiveError"]
    """<p>The error code of the failure.</p>"""
    cause: NotRequired["capo_sfn.types.sensitive_cause.SensitiveCause"]
    """<p>A more detailed explanation of the cause of the failure.</p>"""
    location: NotRequired[
        "capo_sfn.types.evaluation_failure_location.EvaluationFailureLocation"
    ]
    """<p>The location of the field in the state in which the evaluation error occurred.</p>"""
    state: "capo_sfn.types.state_name.StateName"
    """<p>The name of the state in which the evaluation error occurred.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EvaluationFailedEventDetails) -> dict:
    out: dict = {}
    if "error" in value:
        out["error"] = value["error"]
    if "cause" in value:
        out["cause"] = value["cause"]
    if "location" in value:
        out["location"] = value["location"]
    out["state"] = value["state"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EvaluationFailedEventDetails:
    out: EvaluationFailedEventDetails = {}  # type: ignore[typeddict-item]
    if data.get("error") is not None:
        out["error"] = data["error"]
    if data.get("cause") is not None:
        out["cause"] = data["cause"]
    if data.get("location") is not None:
        out["location"] = data["location"]
    if data.get("state") is not None:
        out["state"] = data["state"]
    else:
        out["state"] = ""
    return out


def redact_sensitive(value: EvaluationFailedEventDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "error" in value:
        out["error"] = "*** Sensitive Data Redacted ***"
    if "cause" in value:
        out["cause"] = "*** Sensitive Data Redacted ***"
    if "location" in value:
        out["location"] = "*** Sensitive Data Redacted ***"
    return out

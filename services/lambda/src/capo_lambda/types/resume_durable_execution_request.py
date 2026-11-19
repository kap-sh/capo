"""Generated from Smithy shape ``com.amazonaws.lambda#ResumeDurableExecutionRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.client_token
    import capo_lambda.types.durable_execution_arn
    import capo_lambda.types.resume_reason


class ResumeDurableExecutionRequest(TypedDict, closed=True):
    durable_execution_arn: "capo_lambda.types.durable_execution_arn.DurableExecutionArn"
    """<p>The Amazon Resource Name (ARN) of the durable execution.</p>"""
    client_token: NotRequired["capo_lambda.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide so that the request completes no more than one time. If you repeat a request with the same client token and parameters within 15 minutes, Lambda doesn't resume the execution again and returns a successful response instead of an error.</p>"""
    reason: NotRequired["capo_lambda.types.resume_reason.ResumeReason"]
    """<p>A description of why you're resuming the execution. Lambda records the reason in the execution history.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResumeDurableExecutionRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "reason" in value:
        out["Reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> ResumeDurableExecutionRequest:
    out: ResumeDurableExecutionRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Reason") is not None:
        out["reason"] = data["Reason"]
    return out


def redact_sensitive(value: ResumeDurableExecutionRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "reason" in value:
        out["reason"] = "*** Sensitive Data Redacted ***"
    return out

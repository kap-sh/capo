"""Generated from Smithy shape ``com.amazonaws.lambda#PauseDurableExecutionRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.client_token
    import capo_lambda.types.durable_execution_arn
    import capo_lambda.types.execution_timeout_paused
    import capo_lambda.types.pause_reason


class PauseDurableExecutionRequest(TypedDict, closed=True):
    durable_execution_arn: "capo_lambda.types.durable_execution_arn.DurableExecutionArn"
    """<p>The Amazon Resource Name (ARN) of the durable execution.</p>"""
    client_token: NotRequired["capo_lambda.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide so that the request completes no more than one time. If you repeat a request with the same client token and parameters within 15 minutes, Lambda doesn't pause the execution again and returns a successful response instead of an error.</p>"""
    reason: NotRequired["capo_lambda.types.pause_reason.PauseReason"]
    """<p>A description of why you're pausing the execution. Lambda records the reason in the execution history.</p>"""
    execution_timeout_paused: NotRequired[
        "capo_lambda.types.execution_timeout_paused.ExecutionTimeoutPaused"
    ]
    """<p>Specifies whether to pause the execution timeout while the execution is paused. If <code>true</code>, Lambda extends the execution timeout by the time the execution spends paused. An execution with a paused timeout still times out 366 days after it started. The default value is <code>true</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PauseDurableExecutionRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "reason" in value:
        out["Reason"] = value["reason"]
    if "execution_timeout_paused" in value:
        out["ExecutionTimeoutPaused"] = value["execution_timeout_paused"]
    return out


def deserialize_json(data: dict) -> PauseDurableExecutionRequest:
    out: PauseDurableExecutionRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Reason") is not None:
        out["reason"] = data["Reason"]
    if data.get("ExecutionTimeoutPaused") is not None:
        out["execution_timeout_paused"] = data["ExecutionTimeoutPaused"]
    return out


def redact_sensitive(value: PauseDurableExecutionRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "reason" in value:
        out["reason"] = "*** Sensitive Data Redacted ***"
    return out

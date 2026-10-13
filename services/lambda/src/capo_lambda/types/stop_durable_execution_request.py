"""Generated from Smithy shape ``com.amazonaws.lambda#StopDurableExecutionRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.durable_execution_arn
    import capo_lambda.types.error_object


class StopDurableExecutionRequest(TypedDict, closed=True):
    durable_execution_arn: "capo_lambda.types.durable_execution_arn.DurableExecutionArn"
    """<p>The Amazon Resource Name (ARN) of the durable execution.</p>"""
    error: NotRequired["capo_lambda.types.error_object.ErrorObject"]
    """<p>Optional error details explaining why the execution is being stopped.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopDurableExecutionRequest) -> dict:
    out: dict = {}
    if "error" in value:
        import capo_lambda.types.error_object

        out["Error"] = capo_lambda.types.error_object.serialize_json(value["error"])
    return out


def deserialize_json(data: dict) -> StopDurableExecutionRequest:
    out: StopDurableExecutionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Error") is not None:
        import capo_lambda.types.error_object

        out["error"] = capo_lambda.types.error_object.deserialize_json(data["Error"])
    return out


def redact_sensitive(value: StopDurableExecutionRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "error" in value:
        import capo_lambda.types.error_object

        out["error"] = capo_lambda.types.error_object.redact_sensitive(value["error"])
    return out

"""Generated from Smithy shape ``com.amazonaws.lambda#CheckpointDurableExecutionRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.checkpoint_token
    import capo_lambda.types.client_token
    import capo_lambda.types.durable_execution_arn
    import capo_lambda.types.operation_updates


class CheckpointDurableExecutionRequest(TypedDict, closed=True):
    durable_execution_arn: "capo_lambda.types.durable_execution_arn.DurableExecutionArn"
    """<p>The Amazon Resource Name (ARN) of the durable execution.</p>"""
    checkpoint_token: "capo_lambda.types.checkpoint_token.CheckpointToken"
    """<p>A unique token that identifies the current checkpoint state. This token is provided by the Lambda runtime and must be used to ensure checkpoints are applied in the correct order. Each checkpoint operation consumes this token and returns a new one.</p>"""
    updates: NotRequired["capo_lambda.types.operation_updates.OperationUpdates"]
    """<p>An array of state updates to apply during this checkpoint. Each update represents a change to the execution state, such as completing a step, starting a callback, or scheduling a timer. Updates are applied atomically as part of the checkpoint operation.</p>"""
    client_token: NotRequired["capo_lambda.types.client_token.ClientToken"]
    """<p>An optional idempotency token to ensure that duplicate checkpoint requests are handled correctly. If provided, Lambda uses this token to detect and handle duplicate requests within a 15-minute window.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CheckpointDurableExecutionRequest) -> dict:
    out: dict = {}
    out["CheckpointToken"] = value["checkpoint_token"]
    if "updates" in value:
        import capo_lambda.types.operation_updates

        out["Updates"] = capo_lambda.types.operation_updates.serialize_json(
            value["updates"]
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CheckpointDurableExecutionRequest:
    out: CheckpointDurableExecutionRequest = {}  # type: ignore[typeddict-item]
    if data.get("CheckpointToken") is not None:
        out["checkpoint_token"] = data["CheckpointToken"]
    else:
        out["checkpoint_token"] = ""
    if data.get("Updates") is not None:
        import capo_lambda.types.operation_updates

        out["updates"] = capo_lambda.types.operation_updates.deserialize_json(
            data["Updates"]
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out


def redact_sensitive(value: CheckpointDurableExecutionRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "updates" in value:
        import capo_lambda.types.operation_updates

        out["updates"] = capo_lambda.types.operation_updates.redact_sensitive(
            value["updates"]
        )
    return out

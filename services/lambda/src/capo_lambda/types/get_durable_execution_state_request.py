"""Generated from Smithy shape ``com.amazonaws.lambda#GetDurableExecutionStateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.checkpoint_token
    import capo_lambda.types.durable_execution_arn
    import capo_lambda.types.item_count
    import capo_lambda.types.string


class GetDurableExecutionStateRequest(TypedDict, closed=True):
    durable_execution_arn: "capo_lambda.types.durable_execution_arn.DurableExecutionArn"
    """<p>The Amazon Resource Name (ARN) of the durable execution.</p>"""
    checkpoint_token: "capo_lambda.types.checkpoint_token.CheckpointToken"
    """<p>A checkpoint token that identifies the current state of the execution. This token is provided by the Lambda runtime and ensures that state retrieval is consistent with the current execution context.</p>"""
    marker: NotRequired["capo_lambda.types.string.String"]
    """<p>If <code>NextMarker</code> was returned from a previous request, use this value to retrieve the next page of operations. Each pagination token expires after 24 hours.</p>"""
    max_items: NotRequired["capo_lambda.types.item_count.ItemCount"]
    """<p>The maximum number of operations to return per call. You can use <code>Marker</code> to retrieve additional pages of results. The default is 100 and the maximum allowed is 1000. A value of 0 uses the default.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDurableExecutionStateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDurableExecutionStateRequest:
    out: GetDurableExecutionStateRequest = {}  # type: ignore[typeddict-item]
    return out

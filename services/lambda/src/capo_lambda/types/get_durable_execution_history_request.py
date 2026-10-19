"""Generated from Smithy shape ``com.amazonaws.lambda#GetDurableExecutionHistoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.durable_execution_arn
    import capo_lambda.types.include_execution_data
    import capo_lambda.types.item_count
    import capo_lambda.types.reverse_order
    import capo_lambda.types.string


class GetDurableExecutionHistoryRequest(TypedDict, closed=True):
    durable_execution_arn: "capo_lambda.types.durable_execution_arn.DurableExecutionArn"
    """<p>The Amazon Resource Name (ARN) of the durable execution.</p>"""
    include_execution_data: NotRequired[
        "capo_lambda.types.include_execution_data.IncludeExecutionData"
    ]
    """<p>Specifies whether to include execution data such as step results and callback payloads in the history events. Set to <code>true</code> to include data, or <code>false</code> to exclude it for a more compact response. The default is <code>true</code>.</p>"""
    max_items: NotRequired["capo_lambda.types.item_count.ItemCount"]
    """<p>The maximum number of history events to return per call. You can use <code>Marker</code> to retrieve additional pages of results. The default is 100 and the maximum allowed is 1000. A value of 0 uses the default.</p>"""
    marker: NotRequired["capo_lambda.types.string.String"]
    """<p>If <code>NextMarker</code> was returned from a previous request, use this value to retrieve the next page of results. Each pagination token expires after 24 hours.</p>"""
    reverse_order: NotRequired["capo_lambda.types.reverse_order.ReverseOrder"]
    """<p>When set to <code>true</code>, returns the history events in reverse chronological order (newest first). By default, events are returned in chronological order (oldest first).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDurableExecutionHistoryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDurableExecutionHistoryRequest:
    out: GetDurableExecutionHistoryRequest = {}  # type: ignore[typeddict-item]
    return out

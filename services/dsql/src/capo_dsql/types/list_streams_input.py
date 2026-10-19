"""Generated from Smithy shape ``com.amazonaws.dsql#ListStreamsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dsql.types.cluster_id
    import capo_dsql.types.max_results
    import capo_dsql.types.next_token


class ListStreamsInput(TypedDict, closed=True):
    cluster_identifier: "capo_dsql.types.cluster_id.ClusterId"
    """<p>The ID of the cluster for which to list streams.</p>"""
    max_results: NotRequired["capo_dsql.types.max_results.MaxResults"]
    """<p>An optional parameter that specifies the maximum number of results to return. You can use nextToken to display the next page of results. Default: 10.</p>"""
    next_token: NotRequired["capo_dsql.types.next_token.NextToken"]
    """<p>If your initial ListStreams operation returns a nextToken, you can include the returned nextToken in following ListStreams operations, which returns results in the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStreamsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListStreamsInput:
    out: ListStreamsInput = {}  # type: ignore[typeddict-item]
    return out

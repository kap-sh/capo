"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListDependenciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.max_results
    import capo_resiliencehubv2.types.next_token
    import capo_resiliencehubv2.types.query_granularity


class ListDependenciesRequest(TypedDict, closed=True):
    service_arn: NotRequired["capo_resiliencehubv2.types.arn.Arn"]
    query_range_start_time: NotRequired["datetime.datetime"]
    """<p>The start time for the dependency query range.</p>"""
    query_range_end_time: NotRequired["datetime.datetime"]
    """<p>The end time for the dependency query range.</p>"""
    query_range_granularity: NotRequired[
        "capo_resiliencehubv2.types.query_granularity.QueryGranularity"
    ]
    """<p>The granularity for the dependency query range.</p>"""
    max_results: NotRequired["capo_resiliencehubv2.types.max_results.MaxResults"]
    next_token: NotRequired["capo_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListDependenciesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDependenciesRequest:
    out: ListDependenciesRequest = {}  # type: ignore[typeddict-item]
    return out

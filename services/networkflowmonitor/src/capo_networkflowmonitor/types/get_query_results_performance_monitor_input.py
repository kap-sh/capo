"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#GetQueryResultsPerformanceMonitorInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.query_max_results
    import capo_networkflowmonitor.types.resource_name


class GetQueryResultsPerformanceMonitorInput(TypedDict, closed=True):
    monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName"
    """<p>The name of the performance monitor.</p>"""
    query_id: "str"
    """<p>The identifier for the query. A query ID is an internally-generated identifier for a specific query returned from an API call to start a query.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""
    max_results: NotRequired[
        "capo_networkflowmonitor.types.query_max_results.QueryMaxResults"
    ]
    """<p>The number of query results that you want to return with this call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQueryResultsPerformanceMonitorInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetQueryResultsPerformanceMonitorInput:
    out: GetQueryResultsPerformanceMonitorInput = {}  # type: ignore[typeddict-item]
    return out

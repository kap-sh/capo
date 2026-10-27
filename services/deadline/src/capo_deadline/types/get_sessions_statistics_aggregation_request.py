"""Generated from Smithy shape ``com.amazonaws.deadline#GetSessionsStatisticsAggregationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.aggregation_id
    import capo_deadline.types.farm_id
    import capo_deadline.types.max_results
    import capo_deadline.types.next_token


class GetSessionsStatisticsAggregationRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The identifier of the farm to include in the statistics. This should be the same as the farm ID used in the call to the <code>StartSessionsStatisticsAggregation</code> operation."""
    next_token: NotRequired["capo_deadline.types.next_token.NextToken"]
    """The token for the next set of results, or <code>null</code> to start from the beginning."""
    max_results: NotRequired["capo_deadline.types.max_results.MaxResults"]
    """The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages."""
    aggregation_id: "capo_deadline.types.aggregation_id.AggregationId"
    """The identifier returned by the <code>StartSessionsStatisticsAggregation</code> operation that identifies the aggregated statistics."""


# --- restJson1 ser/de ---
def serialize_json(value: GetSessionsStatisticsAggregationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSessionsStatisticsAggregationRequest:
    out: GetSessionsStatisticsAggregationRequest = {}  # type: ignore[typeddict-item]
    return out

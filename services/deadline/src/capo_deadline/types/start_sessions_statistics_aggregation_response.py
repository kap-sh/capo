"""Generated from Smithy shape ``com.amazonaws.deadline#StartSessionsStatisticsAggregationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.aggregation_id


class StartSessionsStatisticsAggregationResponse(TypedDict, closed=True):
    aggregation_id: "capo_deadline.types.aggregation_id.AggregationId"
    """A unique identifier for the aggregated statistics. Use this identifier with the <code>GetAggregatedStatisticsForSessions</code> operation to return the statistics."""


# --- restJson1 ser/de ---
def serialize_json(value: StartSessionsStatisticsAggregationResponse) -> dict:
    out: dict = {}
    out["aggregationId"] = value["aggregation_id"]
    return out


def deserialize_json(data: dict) -> StartSessionsStatisticsAggregationResponse:
    out: StartSessionsStatisticsAggregationResponse = {}  # type: ignore[typeddict-item]
    if data.get("aggregationId") is not None:
        out["aggregation_id"] = data["aggregationId"]
    else:
        out["aggregation_id"] = ""
    return out

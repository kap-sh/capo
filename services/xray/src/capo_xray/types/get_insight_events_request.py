"""Generated from Smithy shape ``com.amazonaws.xray#GetInsightEventsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.get_insight_events_max_results
    import capo_xray.types.insight_id
    import capo_xray.types.token


class GetInsightEventsRequest(TypedDict, closed=True):
    insight_id: "capo_xray.types.insight_id.InsightId"
    """<p>The insight's unique identifier. Use the GetInsightSummaries action to retrieve an InsightId.</p>"""
    max_results: NotRequired[
        "capo_xray.types.get_insight_events_max_results.GetInsightEventsMaxResults"
    ]
    """<p>Used to retrieve at most the specified value of events.</p>"""
    next_token: NotRequired["capo_xray.types.token.Token"]
    """<p>Specify the pagination token returned by a previous request to retrieve the next page of events. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInsightEventsRequest) -> dict:
    out: dict = {}
    out["InsightId"] = value["insight_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetInsightEventsRequest:
    out: GetInsightEventsRequest = {}  # type: ignore[typeddict-item]
    if data.get("InsightId") is not None:
        out["insight_id"] = data["InsightId"]
    else:
        out["insight_id"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out

"""Generated from Smithy shape ``com.amazonaws.xray#GetInsightRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_xray.types.insight_id


class GetInsightRequest(TypedDict, closed=True):
    insight_id: "capo_xray.types.insight_id.InsightId"
    """<p>The insight's unique identifier. Use the GetInsightSummaries action to retrieve an InsightId.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInsightRequest) -> dict:
    out: dict = {}
    out["InsightId"] = value["insight_id"]
    return out


def deserialize_json(data: dict) -> GetInsightRequest:
    out: GetInsightRequest = {}  # type: ignore[typeddict-item]
    if data.get("InsightId") is not None:
        out["insight_id"] = data["InsightId"]
    else:
        out["insight_id"] = ""
    return out

"""Generated from Smithy shape ``com.amazonaws.xray#GetInsightImpactGraphRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.insight_id
    import capo_xray.types.timestamp
    import capo_xray.types.token


class GetInsightImpactGraphRequest(TypedDict, closed=True):
    insight_id: "capo_xray.types.insight_id.InsightId"
    """<p>The insight's unique identifier. Use the GetInsightSummaries action to retrieve an InsightId.</p>"""
    start_time: "capo_xray.types.timestamp.Timestamp"
    """<p>The estimated start time of the insight, in Unix time seconds. The StartTime is inclusive of the value provided and can't be more than 30 days old.</p>"""
    end_time: "capo_xray.types.timestamp.Timestamp"
    """<p>The estimated end time of the insight, in Unix time seconds. The EndTime is exclusive of the value provided. The time range between the start time and end time can't be more than six hours. </p>"""
    next_token: NotRequired["capo_xray.types.token.Token"]
    """<p>Specify the pagination token returned by a previous request to retrieve the next page of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInsightImpactGraphRequest) -> dict:
    out: dict = {}
    out["InsightId"] = value["insight_id"]
    import capo_xray.types.timestamp

    out["StartTime"] = capo_xray.types.timestamp.serialize_json(value["start_time"])
    import capo_xray.types.timestamp

    out["EndTime"] = capo_xray.types.timestamp.serialize_json(value["end_time"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetInsightImpactGraphRequest:
    out: GetInsightImpactGraphRequest = {}  # type: ignore[typeddict-item]
    if data.get("InsightId") is not None:
        out["insight_id"] = data["InsightId"]
    else:
        out["insight_id"] = ""
    if data.get("StartTime") is not None:
        import capo_xray.types.timestamp

        out["start_time"] = capo_xray.types.timestamp.deserialize_json(
            data["StartTime"]
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("EndTime") is not None:
        import capo_xray.types.timestamp

        out["end_time"] = capo_xray.types.timestamp.deserialize_json(data["EndTime"])
    else:
        import datetime

        out["end_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out

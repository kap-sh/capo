"""Generated from Smithy shape ``com.amazonaws.xray#GetInsightSummariesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.get_insight_summaries_max_results
    import capo_xray.types.group_arn
    import capo_xray.types.group_name
    import capo_xray.types.insight_state_list
    import capo_xray.types.timestamp
    import capo_xray.types.token


class GetInsightSummariesRequest(TypedDict, closed=True):
    states: NotRequired["capo_xray.types.insight_state_list.InsightStateList"]
    """<p>The list of insight states. </p>"""
    group_arn: NotRequired["capo_xray.types.group_arn.GroupARN"]
    """<p>The Amazon Resource Name (ARN) of the group. Required if the GroupName isn't provided.</p>"""
    group_name: NotRequired["capo_xray.types.group_name.GroupName"]
    """<p>The name of the group. Required if the GroupARN isn't provided.</p>"""
    start_time: "capo_xray.types.timestamp.Timestamp"
    """<p>The beginning of the time frame in which the insights started. The start time can't be more than 30 days old.</p>"""
    end_time: "capo_xray.types.timestamp.Timestamp"
    """<p>The end of the time frame in which the insights ended. The end time can't be more than 30 days old.</p>"""
    max_results: NotRequired[
        "capo_xray.types.get_insight_summaries_max_results.GetInsightSummariesMaxResults"
    ]
    """<p>The maximum number of results to display.</p>"""
    next_token: NotRequired["capo_xray.types.token.Token"]
    """<p>Pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInsightSummariesRequest) -> dict:
    out: dict = {}
    if "states" in value:
        import capo_xray.types.insight_state_list

        out["States"] = capo_xray.types.insight_state_list.serialize_json(
            value["states"]
        )
    if "group_arn" in value:
        out["GroupARN"] = value["group_arn"]
    if "group_name" in value:
        out["GroupName"] = value["group_name"]
    import capo_xray.types.timestamp

    out["StartTime"] = capo_xray.types.timestamp.serialize_json(value["start_time"])
    import capo_xray.types.timestamp

    out["EndTime"] = capo_xray.types.timestamp.serialize_json(value["end_time"])
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetInsightSummariesRequest:
    out: GetInsightSummariesRequest = {}  # type: ignore[typeddict-item]
    if data.get("States") is not None:
        import capo_xray.types.insight_state_list

        out["states"] = capo_xray.types.insight_state_list.deserialize_json(
            data["States"]
        )
    if data.get("GroupARN") is not None:
        out["group_arn"] = data["GroupARN"]
    if data.get("GroupName") is not None:
        out["group_name"] = data["GroupName"]
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
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out

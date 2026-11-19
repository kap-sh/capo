"""Generated from Smithy shape ``com.amazonaws.guardduty#Trend``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.count
    import capo_guardduty.types.time_granularity
    import capo_guardduty.types.time_window_groups
    import capo_guardduty.types.timestamp


class Trend(TypedDict, closed=True):
    granularity: NotRequired["capo_guardduty.types.time_granularity.TimeGranularity"]
    """<p>The length of each time window in the trend. Possible values are <code>DAY</code>, <code>WEEK</code>, and <code>MONTH</code>.</p>"""
    started_at: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp at which the period of the trend starts.</p>"""
    ended_at: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp at which the period of the trend ends.</p>"""
    total_findings: NotRequired["capo_guardduty.types.count.Count"]
    """<p>The total number of findings in the period.</p>"""
    by_time_window: NotRequired[
        "capo_guardduty.types.time_window_groups.TimeWindowGroups"
    ]
    """<p>The number of findings in each time window.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Trend) -> dict:
    out: dict = {}
    if "granularity" in value:
        import capo_guardduty.types.time_granularity

        out["granularity"] = capo_guardduty.types.time_granularity.serialize_json(
            value["granularity"]
        )
    if "started_at" in value:
        import capo_guardduty.types.timestamp

        out["startTime"] = capo_guardduty.types.timestamp.serialize_json(
            value["started_at"]
        )
    if "ended_at" in value:
        import capo_guardduty.types.timestamp

        out["endTime"] = capo_guardduty.types.timestamp.serialize_json(
            value["ended_at"]
        )
    if "total_findings" in value:
        out["totalFindings"] = value["total_findings"]
    if "by_time_window" in value:
        import capo_guardduty.types.time_window_groups

        out["byTimeWindow"] = capo_guardduty.types.time_window_groups.serialize_json(
            value["by_time_window"]
        )
    return out


def deserialize_json(data: dict) -> Trend:
    out: Trend = {}  # type: ignore[typeddict-item]
    if data.get("granularity") is not None:
        import capo_guardduty.types.time_granularity

        out["granularity"] = capo_guardduty.types.time_granularity.deserialize_json(
            data["granularity"]
        )
    if data.get("startTime") is not None:
        import capo_guardduty.types.timestamp

        out["started_at"] = capo_guardduty.types.timestamp.deserialize_json(
            data["startTime"]
        )
    if data.get("endTime") is not None:
        import capo_guardduty.types.timestamp

        out["ended_at"] = capo_guardduty.types.timestamp.deserialize_json(
            data["endTime"]
        )
    if data.get("totalFindings") is not None:
        out["total_findings"] = data["totalFindings"]
    if data.get("byTimeWindow") is not None:
        import capo_guardduty.types.time_window_groups

        out["by_time_window"] = (
            capo_guardduty.types.time_window_groups.deserialize_json(
                data["byTimeWindow"]
            )
        )
    return out

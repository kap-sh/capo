"""Generated from Smithy shape ``com.amazonaws.guardduty#TimeWindowGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.integer
    import capo_guardduty.types.timestamp


class TimeWindowGroup(TypedDict, closed=True):
    start_time: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp at which the time window starts.</p>"""
    end_time: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp at which the time window ends.</p>"""
    finding_count: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>The number of findings in the time window.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeWindowGroup) -> dict:
    out: dict = {}
    if "start_time" in value:
        import capo_guardduty.types.timestamp

        out["startTime"] = capo_guardduty.types.timestamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_guardduty.types.timestamp

        out["endTime"] = capo_guardduty.types.timestamp.serialize_json(
            value["end_time"]
        )
    if "finding_count" in value:
        out["findingCount"] = value["finding_count"]
    return out


def deserialize_json(data: dict) -> TimeWindowGroup:
    out: TimeWindowGroup = {}  # type: ignore[typeddict-item]
    if data.get("startTime") is not None:
        import capo_guardduty.types.timestamp

        out["start_time"] = capo_guardduty.types.timestamp.deserialize_json(
            data["startTime"]
        )
    if data.get("endTime") is not None:
        import capo_guardduty.types.timestamp

        out["end_time"] = capo_guardduty.types.timestamp.deserialize_json(
            data["endTime"]
        )
    if data.get("findingCount") is not None:
        out["finding_count"] = data["findingCount"]
    return out

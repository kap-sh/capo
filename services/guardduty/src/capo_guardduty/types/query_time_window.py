"""Generated from Smithy shape ``com.amazonaws.guardduty#QueryTimeWindow``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.timestamp


class QueryTimeWindow(TypedDict, closed=True):
    start_time: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp at which the time window starts.</p>"""
    end_time: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp at which the time window ends.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryTimeWindow) -> dict:
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
    return out


def deserialize_json(data: dict) -> QueryTimeWindow:
    out: QueryTimeWindow = {}  # type: ignore[typeddict-item]
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
    return out

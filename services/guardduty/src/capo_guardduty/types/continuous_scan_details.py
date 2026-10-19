"""Generated from Smithy shape ``com.amazonaws.guardduty#ContinuousScanDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.timestamp


class ContinuousScanDetails(TypedDict, closed=True):
    start_time: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp representing the start of the time range to scan. Reserved for internal use.</p>"""
    end_time: "capo_guardduty.types.timestamp.Timestamp"
    """<p>The timestamp representing the end of the time range to scan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContinuousScanDetails) -> dict:
    out: dict = {}
    if "start_time" in value:
        import capo_guardduty.types.timestamp

        out["startTime"] = capo_guardduty.types.timestamp.serialize_json(
            value["start_time"]
        )
    import capo_guardduty.types.timestamp

    out["endTime"] = capo_guardduty.types.timestamp.serialize_json(value["end_time"])
    return out


def deserialize_json(data: dict) -> ContinuousScanDetails:
    out: ContinuousScanDetails = {}  # type: ignore[typeddict-item]
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
    else:
        import datetime

        out["end_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out

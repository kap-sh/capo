"""Generated from Smithy shape ``com.amazonaws.iot#ViolationEventOccurrenceRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.timestamp


class ViolationEventOccurrenceRange(TypedDict, closed=True):
    start_time: "capo_iot.types.timestamp.Timestamp"
    """<p> The start date and time of a time period in which violation events occurred. </p>"""
    end_time: "capo_iot.types.timestamp.Timestamp"
    """<p> The end date and time of a time period in which violation events occurred. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ViolationEventOccurrenceRange) -> dict:
    out: dict = {}
    import capo_iot.types.timestamp

    out["startTime"] = capo_iot.types.timestamp.serialize_json(value["start_time"])
    import capo_iot.types.timestamp

    out["endTime"] = capo_iot.types.timestamp.serialize_json(value["end_time"])
    return out


def deserialize_json(data: dict) -> ViolationEventOccurrenceRange:
    out: ViolationEventOccurrenceRange = {}  # type: ignore[typeddict-item]
    if data.get("startTime") is not None:
        import capo_iot.types.timestamp

        out["start_time"] = capo_iot.types.timestamp.deserialize_json(data["startTime"])
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("endTime") is not None:
        import capo_iot.types.timestamp

        out["end_time"] = capo_iot.types.timestamp.deserialize_json(data["endTime"])
    else:
        import datetime

        out["end_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out

"""Generated from Smithy shape ``com.amazonaws.frauddetector#IngestedEventsTimeWindow``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.time


class IngestedEventsTimeWindow(TypedDict, closed=True):
    start_time: "capo_frauddetector.types.time.time"
    """<p>Timestamp of the first ingensted event.</p>"""
    end_time: "capo_frauddetector.types.time.time"
    """<p>Timestamp of the final ingested event.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IngestedEventsTimeWindow) -> dict:
    out: dict = {}
    out["startTime"] = value["start_time"]
    out["endTime"] = value["end_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IngestedEventsTimeWindow:
    out: IngestedEventsTimeWindow = {}  # type: ignore[typeddict-item]
    if data.get("startTime") is not None:
        out["start_time"] = data["startTime"]
    else:
        out["start_time"] = ""
    if data.get("endTime") is not None:
        out["end_time"] = data["endTime"]
    else:
        out["end_time"] = ""
    return out

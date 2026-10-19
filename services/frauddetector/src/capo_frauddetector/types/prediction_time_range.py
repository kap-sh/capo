"""Generated from Smithy shape ``com.amazonaws.frauddetector#PredictionTimeRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.time


class PredictionTimeRange(TypedDict, closed=True):
    start_time: "capo_frauddetector.types.time.time"
    """<p> The start time of the time period for when the predictions were generated. </p>"""
    end_time: "capo_frauddetector.types.time.time"
    """<p> The end time of the time period for when the predictions were generated. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredictionTimeRange) -> dict:
    out: dict = {}
    out["startTime"] = value["start_time"]
    out["endTime"] = value["end_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PredictionTimeRange:
    out: PredictionTimeRange = {}  # type: ignore[typeddict-item]
    if data.get("startTime") is not None:
        out["start_time"] = data["startTime"]
    else:
        out["start_time"] = ""
    if data.get("endTime") is not None:
        out["end_time"] = data["endTime"]
    else:
        out["end_time"] = ""
    return out
